#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Freepoet
"""Refresh the readable BOM and checksums without modifying hardware assets."""

import argparse
import csv
import hashlib
import io
from pathlib import Path
import posixpath
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
ASSETS = [
    "BOM.xlsx",
    "Gerber/Norns Shield Pro Gerber.zip",
    "Schematic/Schematic20250606.pdf",
    "Top cover/20250523.ai",
    *(f"Top cover/part{i}.stl" for i in range(1, 5)),
]


def bom_csv():
    """Extract source cell values, including repeated identifiers and blanks."""
    with ZipFile(ROOT / "BOM.xlsx") as archive:
        strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            tree = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            strings = [
                "".join(t.text or "" for t in node.findall(".//s:t", NS))
                for node in tree.findall("s:si", NS)
            ]
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        sheet = workbook.find("s:sheets/s:sheet", NS)
        if sheet is None:
            raise ValueError("Workbook has no worksheets")
        relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        relationship = next(
            item for item in relationships if item.get("Id") == sheet.get(f"{{{REL}}}id")
        )
        if relationship.get("TargetMode") == "External":
            raise ValueError("External worksheet targets are unsupported")
        target = relationship.attrib["Target"]
        target = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/" + target)
        worksheet = ET.fromstring(archive.read(target))
        rows = []
        for source_row in worksheet.findall("s:sheetData/s:row", NS):
            values = [""] * 5
            for cell in source_row.findall("s:c", NS):
                if cell.find("s:f", NS) is not None:
                    raise ValueError(f"Formula at {cell.get('r')}: review the export manually")
                letters = "".join(c for c in cell.attrib["r"] if c.isalpha())
                column = 0
                for letter in letters:
                    column = column * 26 + ord(letter) - ord("A") + 1
                value = cell.findtext("s:v", default="", namespaces=NS)
                kind = cell.get("t")
                if kind == "s":
                    value = strings[int(value)]
                elif kind == "inlineStr":
                    value = "".join(t.text or "" for t in cell.findall(".//s:t", NS))
                elif kind in ("b", "e", "d"):
                    raise ValueError(f"Unsupported cell type {kind} at {cell.get('r')}")
                if column > 5:
                    if value:
                        raise ValueError("BOM has columns beyond the supported five-column layout")
                    continue
                values[column - 1] = value
            if any(values):
                rows.append(values)
        if not rows or rows[0] != ["No.", "Quantity", "Comment", "Designator", "Footprint"]:
            raise ValueError("BOM headers changed; review the exporter before proceeding")
    buffer = io.StringIO(newline="")
    csv.writer(buffer, lineterminator="\n").writerows(rows)
    return buffer.getvalue().encode("utf-8")


def outputs():
    manifest = "".join(
        f"{hashlib.sha256((ROOT / name).read_bytes()).hexdigest()}  {name}\n"
        for name in ASSETS
    )
    return {"docs/BOM.csv": bom_csv(), "docs/assets.sha256": manifest.encode("utf-8")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check freshness without writing files")
    args = parser.parse_args()
    stale = []
    for name, expected in outputs().items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_bytes() != expected:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(expected)
            print(f"Updated {name}")
    if stale:
        print("Out of date: " + ", ".join(stale), file=sys.stderr)
        return 1
    if args.check:
        print("BOM CSV and asset checksums match the current source files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

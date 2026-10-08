# Contributing

Thank you for helping make the hardware files easier to reproduce and maintain.

## Report an issue

Use the repository's [Issues page](https://github.com/FreepoetOfficial/Norns-Shield-Pro/issues). Include:

- The Git commit ID and affected file.
- A component designator, spreadsheet row, schematic section, or STL filename.
- What you observed and what you expected, with a photo or screenshot where useful.
- For a hardware problem, the board revision, populated parts, supply, software/image version, and measurements you actually took.

Use the file dates and Git revision to identify your copy. Matching filenames alone do not establish that two exports belong to the same hardware revision.

## Propose a change

Make documentation edits in both [README.md](README.md) and [README.zh-CN.md](README.zh-CN.md) when they affect shared instructions. Keep all other public prose and figure labels in English. Keep asset links relative so they work in forks and downloaded copies.

For electrical changes, include the editable design source and synchronized exports. Explain the affected circuits, component references, footprints, and any manufacturing or assembly consequences. State exactly what was checked; do not present a file-format check as a successful hardware test.

For mechanical changes, identify the part, units, material assumptions, tolerances, and fit checks. Update the model previews and dimension table when necessary.

After changing the BOM or original hardware assets, refresh generated metadata:

```sh
python3 scripts/refresh_metadata.py
python3 scripts/refresh_metadata.py --check
```

Keep screenshots, temporary renders, local backups, and personal manufacturing orders out of the repository unless they are intentionally part of its documentation. Do not add a license or change upstream attribution without the repository owner's decision.

## Licenses and attribution

Follow the scope in [LICENSE.md](LICENSE.md): GPLv3 for electronic design materials and MIT for Freepoet's independent mechanical designs, original prose, and maintenance utilities. A schematic rendering retains the schematic's GPLv3 scope. Preserve all third-party notices and document new external material in [NOTICE.md](NOTICE.md).

Include corresponding editable sources with design changes. Mark renderings as design previews; do not present them as product photographs or proof of fit. The [gallery](docs/GALLERY.md) records the source and license of each published preview.

# Attribution and provenance

## Upstream electronic designs

**Norns Shield** was designed by monome / Brian Crabtree (`tehn`).

- Project: <https://github.com/monome/norns-shield>
- License: [GNU GPL version 3](https://github.com/monome/norns-shield/blob/main/LICENSE)

**shieldXL** is a rework of Norns Shield by Steven Noreyko / denki-oto (`okyeron`). Its published KiCad documentation identifies the 210330 Norns Shield design as its basis and describes the redesign as originating in March 2023.

- Project: <https://github.com/okyeron/shieldXL>
- Design provenance: [KiCad README](https://github.com/okyeron/shieldXL/blob/main/kicad/README.md)
- License: [GNU GPL version 3](https://github.com/okyeron/shieldXL/blob/main/kicad/LICENSE.txt)

Norns Shield Pro is based on both projects. The precise upstream files and revisions used for Freepoet's electronic design have not yet been recorded. The shieldXL provenance above is an upstream statement, not a claim that Freepoet used that exact revision. Existing upstream copyright and license notices must be preserved when the editable design sources are added.

## Freepoet contributions

Copyright (c) 2026 Freepoet for its original contributions.

- **Electronic design modifications:** the supplied design includes battery/power circuitry and other changes to the upstream-based design. Freepoet describes noise reduction as a design goal. A complete source-level change list and comparative measurements are not yet supplied.
- **Mechanical design:** Freepoet confirms that `Top cover/part1.stl` through `part4.stl` and `Top cover/20250523.ai` were independently drawn/modelled by Freepoet. These files are licensed under MIT. Visual similarity to shieldXL does not make its enclosure authors the authors of these files.
- **Documentation and utilities:** Freepoet's original explanatory text, metadata utility, and mechanical previews are licensed under MIT. Renderings of electronic design material remain under GPLv3 as specified in [LICENSE.md](LICENSE.md).

## Published documentation changes

On 2026-10-08, the public documentation was expanded with file navigation, a hardware guide, generated BOM data, checksums, design previews, license scope, and attribution notices. The schematic's USB-C input annotation and the panel's descriptive title metadata were localized to English. No component values, nets, board geometry, or enclosure geometry were intentionally changed by that update.

The Gerber archive also includes GPLv3 and attribution notices; the 17 original manufacturing/test file contents were preserved. The USB-C annotation translation is a presentation change, not a new electrical revision. Confirm the current files using [docs/assets.sha256](docs/assets.sha256).

## Support and external materials

Norns Shield Pro is a Freepoet project. It is not presented as an official monome or denki-oto product, and neither upstream project is responsible for supporting these modifications. Report issues through [this repository](https://github.com/FreepoetOfficial/Norns-Shield-Pro/issues).

The names and logos of other projects remain associated with their respective owners. External datasheets and linked documents remain subject to their publishers' terms. No upstream product photographs or enclosure model files are included as Freepoet work.

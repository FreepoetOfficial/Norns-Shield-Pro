# Licensing

This repository contains separately licensed materials. Use the file scope below rather than assuming one license covers every asset.

| Material | Scope | License |
| --- | --- | --- |
| Electronic design and manufacturing data | `Gerber/`, `Schematic/`, `BOM.xlsx`, `docs/BOM.csv` | GNU General Public License version 3 ([full text](LICENSES/GPL-3.0-only.txt)) |
| Schematic preview | `docs/images/schematic.png` | GNU General Public License version 3, as a rendering of the schematic |
| Original enclosure and panel designs | `Top cover/part1.stl` through `part4.stl`, `Top cover/20250523.ai` | MIT ([full text](LICENSES/MIT.txt)) |
| Mechanical previews | `docs/images/enclosure-parts.png`, `docs/images/panel.png` | MIT, as renderings of Freepoet's original designs |
| Original documentation and maintenance utilities | Root and `docs/` Markdown files, `scripts/`, `docs/assets.sha256`, `.gitignore`, `.gitattributes` | MIT, except embedded or linked materials with their own license |

Copyright (c) 2026 Freepoet for its original contributions. Upstream authors retain copyright in their contributions. See [NOTICE.md](NOTICE.md) for attribution and provenance. The license texts in `LICENSES/` retain their own notices and are not relicensed by this table.

## Electronic design

The electronic design is based on monome's Norns Shield and denki-oto's shieldXL. The covered electronic design materials and Freepoet's modifications are distributed under GNU GPL version 3 (`GPL-3.0-only`). Preserve upstream notices and any separately granted upstream permissions. This statement does not claim ownership of upstream work or remove any rights its authors granted separately.

When distributing covered modified design files, retain applicable copyright and license notices, identify modifications and their dates, and meet GPLv3's corresponding-source requirements for distributed non-source forms. Commercial distribution is permitted subject to those terms.

**Source availability:** the repository currently includes manufacturing exports and a schematic PDF, but not the editable EDA project and libraries used to generate them. Those source materials still need to be supplied for the corresponding design revision. This notice and the exported files do not substitute for corresponding source or claim that all source-delivery obligations have been fulfilled.

## Original mechanical designs and documentation

Freepoet confirms that the STL enclosure models and AI panel drawing were independently created by Freepoet. They are licensed under MIT as original design materials; no shieldXL enclosure model is identified as their source. For this grant, the MIT license applies to these design files and associated documentation as well as the original utilities and prose listed above.

MIT permits commercial use, modification, redistribution, and sublicensing, provided its copyright and permission notice accompanies copies or substantial portions. Include [LICENSES/MIT.txt](LICENSES/MIT.txt) when redistributing these materials.

## Separate materials and names

Placing independently licensed files in this repository does not change their listed license. A screenshot or rendering of GPL-covered circuit material remains in the GPL scope even when embedded in an MIT-licensed document. Third-party software, linked datasheets, external websites, and future dependencies retain their own terms.

No software image or firmware is distributed here. A future bundled image needs its own component-level license and source review. Project names identify provenance and compatibility; this repository does not imply endorsement or support by monome or denki-oto.

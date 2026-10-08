# Norns Shield Pro

Freepoet 的 Norns Shield Pro 硬件资料仓库。项目基于原版 Norns Shield 和 Norns Shield XL，包含用于树莓派乐器的音频电路、实体控制器、OLED 接口及电池/供电电路。

[English](README.md) · [硬件指南](docs/HARDWARE.md) · [设计图库](docs/GALLERY.md) · [许可说明](LICENSE.md)

![根据四个原始 STL 文件分别渲染的外壳模型](docs/images/enclosure-parts.png)

*各模型分别居中并缩放展示，不代表装配关系，也不是成品照片。[设计图库](docs/GALLERY.md)中还提供面板及原理图预览。除本中文 README 外，公开说明文档使用英文。*

## 当前状态

仓库提供的是一套硬件资料快照，包括生产导出文件、原理图 PDF、物料清单和外壳文件。尚未包含可编辑的 PCB/原理图工程或固件。

这些文件用于设计参考。制作前，请确认对应电路版本、元件规格和生产参数；仓库目前尚未提供完整装配及验证指南。

原项目说明将降低噪声干扰作为设计目标，但仓库没有对比测量数据，因此不宣称已验证的降噪幅度。套件信息可查看 [Freepoet 商店](https://freepoet.co.uk/)。

## 文件导航

| 文件 | 内容与用途 |
| --- | --- |
| [BOM.xlsx](BOM.xlsx) | 原始物料清单，用于查看电子元件、结构件及配件的规格和数量 |
| [BOM.csv](docs/BOM.csv) | 便于 GitHub 在线浏览和搜索的文本副本，保留原表的值，包括尚未修正的条目 |
| [Gerber 压缩包](Gerber/Norns%20Shield%20Pro%20Gerber.zip) | 四层铜层、阻焊、钢网、丝印、板框、钻孔及飞针测试数据 |
| [原理图 PDF](Schematic/Schematic20250606.pdf) | 单页原理图，包括电源、主功能、按键/编码器、接口和 OLED；输入图注已翻译为英文 |
| [面板 AI 文件](Top%20cover/20250523.ai) | 面板轮廓及开孔图，带有兼容 PDF 的预览内容 |
| [外壳文件目录](Top%20cover/) | `part1.stl` 至 `part4.stl` 四个独立网格；尺寸和限制见硬件指南 |

原始文件路径保持不变，已有下载链接仍可使用。

## 配置概览

原始 BOM 列出了 Raspberry Pi 4B 1 GB、32 GB microSD 卡、2.7 英寸 OLED 及盖板、三个旋转编码器和三个主按键。这是当前清单中的配置，不等同于已经测试过的兼容性列表。

- **音频：** BOM 列出的编解码器为 `CS4270-CZZ`，电路包含音频输入/输出和 12.288 MHz 时钟。
- **控制：** 三个 `PEC11R-4015F-S0024` 编码器、三个 `CPG135001D01` 按键，以及供电/控制开关。
- **显示：** OLED 接口、30 位连接器及相关电源电路。
- **供电：** USB-C 输入、18650 电池座及充电/转换电路。电芯要求、电流上限和续航尚未记录。
- **接口：** 音频连接器及带光耦的 TX/RX 相关电路。外接线材接法和接口约定仍需补充。

## 如何使用这套资料

1. 通过[硬件指南](docs/HARDWARE.md)找到所需文件。
2. 打开原始 BOM 或网页版副本，查看元件和数量。
3. 将原理图与 Gerber 对照查看，确认实际制作所需的元件规格和生产参数。
4. 在网格查看器或切片软件中查看外壳，确认单位、配合间隙和硬件尺寸后再加工。
5. 再分发设计文件或修改版本前，查看[许可范围](LICENSE.md)和[来源署名](NOTICE.md)。

## 版本与维护

- 使用 Git 提交编号识别当前资料快照；本次整理没有指定新的硬件版本号。
- 原始文件名日期、文件内部导出日期和入库日期可能不同，详见[硬件指南](docs/HARDWARE.md)。
- 修改硬件时，先改设计源文件，再同步导出原理图、BOM 和生产文件。
- 更新文件后，运行 `python3 scripts/refresh_metadata.py`，刷新网页版 BOM 和校验清单；用 `--check` 检查是否过期。
- 硬件指南和预览图需要随设计变化更新，脚本不会自动验证电路或重做预览。

提交问题或改动时，请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 来源与许可

电路设计基于 monome / Brian Crabtree 的 [Norns Shield](https://github.com/monome/norns-shield)，以及 Steven Noreyko / denki-oto 的 [shieldXL](https://github.com/okyeron/shieldXL)。STL 外壳和 AI 面板由 Freepoet 独立设计。

- **电路设计、BOM 和生产导出文件：** GPLv3。
- **原创外壳、面板、机械预览、文档和维护脚本：** MIT。
- **原理图预览：** 作为电路资料的渲染图，使用 GPLv3。

完整文件范围及许可证见 [LICENSE.md](LICENSE.md)，来源署名及修改记录见 [NOTICE.md](NOTICE.md)。Freepoet 对其原创贡献保留版权，上游作者的权利和声明继续保留。

对应版本的可编辑 EDA 源工程仍需补充；添加许可证不能替代源文件交付义务。本项目不表示获得 monome 或 denki-oto 的官方背书或支持。

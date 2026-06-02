# 黑曲霉密码子评审网页 SOP

适用文件：[`aniger_codon_review.html`](aniger_codon_review.html)（单文件、双击即用，无需安装 Python / Streamlit）。详细示例见 **附录 A**。

---

## 1. 这个工具是干什么的？

在 **不改变氨基酸序列** 的前提下，把多条 **DNA（CDS）** 当作「同一蛋白、不同密码子写法」的候选，用 **黑曲霉（*Aspergillus niger*）Kazusa 密码子使用表（taxid 5061）** 做：

- 指标：GC%、GC1/2/3、CAI/CSI 风格分数、CFD%、与宿主频率距离、酶切位点、均聚物等，并给一个 **综合排名分**；
- 校验：每条候选翻译后是否 **与目标蛋白完全一致**；
- 对比：**逐密码子**看各版本用的是什么三联体、是否「稀有」、是否与原始序列相同；
- 导出：CSV / JSON / FASTA，方便留档或给合成公司。

**频率表数据文件**：同目录 [`aspergillus_niger_5061.csv`](aspergillus_niger_5061.csv) 为 Kazusa taxid **5061** 的原始计数（列 `amino_acid`, `codon`, `observed_count`）；本页内嵌数据与此一致，脚本在载入时按氨基酸簇归一化为相对频率。溯源与重建步骤见 [`aspergillus_niger_5061_SOURCE.md`](aspergillus_niger_5061_SOURCE.md)、[`generate_kazusa5061_table.py`](generate_kazusa5061_table.py)。

---

## 2. 你需要准备什么（导入什么）？

### 2.1 原始 / 目标序列（左侧第一块，必填）

任选一种形式即可：

| 形式 | 说明 |
|------|------|
| **CDS（DNA）** | 标准编码区：仅 A/C/G/T，长度为 3 的倍数；**建议**含起始 ATG 与末尾终止子 TAA/TAG/TGA。程序用它推出 **目标蛋白序列**，并作为「参考 DNA」参与逐位对比（Ref 列）。 |
| **仅蛋白序列** | 一行或多行氨基酸单字母（无 DNA 时）。程序 **没有** 原始 DNA 对照，热图里 **Ref** 列为空，但仍可比较各候选之间密码子差异。 |

**导入方式：**

- 在文本框里 **粘贴**；或  
- 点 **选择文件** 上传 `.fa` / `.fasta` / `.fna` / `.txt` 等（内容可以是 FASTA 或纯序列）。

**注意：** 若文件带 UTF-8 BOM，页面已做兼容；多条 FASTA 时 **只取第一条** 作为参考。

### 2.2 候选序列（左侧第二块，可选但常用）

来自：**自己改序列**、**IDT / GenScript / JCat**、**基因合成公司** 等返回的多条 DNA。

**支持格式：**

| 格式 | 要求 |
|------|------|
| **FASTA** | 多条 `>名称` + 序列；名称里可写 `IDT`、`GenScript` 等关键词，程序会粗分类 **source**。 |
| **CSV** | 第一行为表头，必须有一列名为 **`sequence`**（小写）；可选列 **`name`** / **`id`**、**`source`** / **`provider`**。 |
| **纯 DNA 长串** | 粘贴的文本里若有一段 ≥30 的连续 ACGT，会自动抽 **最长** 的一段当作一条候选（适合从邮件里复制）。 |

**导入方式：**

- **粘贴**到「候选序列」文本框；和/或  
- **多选文件**（多个 FASTA/CSV 会 **拼接** 再解析）。

**本页不支持：** `.xlsx`。请在公司网站导出 **FASTA 或 CSV**，或在 Excel 里「另存为 CSV」并保证有 `sequence` 列。

### 2.3 参数（左侧下方）

- **CFD 稀有阈值**：默认 0.3；低于该「相对适应性」的密码子计为稀有（热图偏红、CFD% 升高）。  
- **随机种子**：仅影响程序自动生成的两条随机/平衡候选，固定种子可复现。  
- **生成本地候选**：勾选后会自动加入 3 条：**最高频（HFC）**、**按 Kazusa 频率加权随机**、**兼顾 GC/GC3 的贪心平衡**；可与外部候选一起排名。

### 2.4 候选来源与「接口」（如何接到本工具）

**候选**指：与目标蛋白一致、但密码子写法不同的 CDS。常见来源如下（均需 **人工导出或复制** 后粘贴/上传；本页 **不** 携带密钥、**不** 自动请求第三方 API，避免 CORS 与合规问题）。

| 来源 | 说明 | 推荐导入方式 |
|------|------|----------------|
| **本页「生成本地候选」** | 基于 Kazusa 黑曲霉 5061 的 HFC / 加权随机 / GC-GC3 平衡 | 勾选后随分析自动生成 |
| **[JCat](https://www.jcat.de/)** | 在线密码子优化（常见为原核默认；真菌宿主请核对物种/表是否适用） | 网页结果复制或导出 → FASTA/纯序列 →「候选」 |
| **[IDT](https://www.idtdna.com/)** | gBlocks、基因片段等订购与序列编辑 | 订单确认页、邮件附件、网页复制 → FASTA |
| **[GenScript](https://www.genscript.com/)** | GenSmart 等优化与合成 | 网页导出 FASTA 或 CSV（含 `sequence` 列） |
| **[Twist](https://www.twistbioscience.com/)** 等合成平台 | 基因订购流程 | 账户内下载 FASTA / 复制序列 |
| **[Optipyzer](https://optipyzer.com/)** 等第三方优化器 | 多宿主优化 | 按各站说明导出序列 → FASTA |
| **Kazusa 密码子表**（参考） | [Codon Usage Database](https://www.kazusa.or.jp/codon/) 查物种频率，非直接产序列 | 理解指标用；本页已内嵌 A. niger 5061 |

**「接口」两层含义：**（1）**人机接口**：浏览器里复制/下载文件 → 本页导入（**当前支持**）。（2）**程序接口（REST/API）**：供应商企业接口需 Token，宜在 **Python/后端** 拉取后存 FASTA，再导入本页；**勿** 在离线 HTML 里硬编码密钥。

---

## 3. 操作步骤（怎么用）

1. 双击打开 `aniger_codon_review.html`（推荐 Chrome / Edge）。  
2. 在 **原始/目标** 中粘贴或上传参考序列（CDS 或蛋白）。  
3. 在 **候选** 中粘贴或上传多条版本（FASTA 或 CSV）。  
4. 按需调整 CFD 阈值、种子、是否生成本地候选。  
5. 点击 **「分析」**。  
6. 依次查看标签页：**指标与排名** → **逐密码子热图** → **逐密码子长表**。  
7. 打开 **「导出」**，下载 CSV / JSON / 通过校验的 FASTA。

**判断标准（湿实验常用）：**

- **进入排名**：该条 DNA 翻译后与目标蛋白 **完全一致**，且通过基本 CDS 校验。  
- **未通过**：蛋白不一致、长度不是 3 的倍数、内部出现终止子等；看表格里的 **errors** 列。  
- **排名分 `ranking_score`**：在 CAI、CFD、与宿主频率距离、GC 接近 Kazusa 报道值、酶切与长均聚物惩罚等综合后的标量，**仅供排序参考**，不等于表达量保证。

---

## 4. 各页/导出文件实现什么？

| 模块 | 实现内容 |
|------|----------|
| **指标与排名** | 每条候选一行：长度、GC、CAI/CSI、CFD%、稀有位点摘要、酶切位点、均聚物、与原始序列的碱基/密码子一致率（若有原始 DNA）、`ranking_score` 等。若参考为 DNA FASTA，**参与排名的「原始」行 `name` 与 `>` 后第一个词一致**（无名字时 fallback 为 `original_reference`）；`source` 仍为 `original`。 |
| **逐密码子热图** | 每个密码子位置一行：位点、氨基酸、Ref（原始 CDS 该位密码子）、各候选该位密码子；颜色区分与参考一致 / 改变 / 稀有 / 非同义错误。最多展示前 **360** 个密码子位点（全长请用导出 CSV）。 |
| **逐密码子长表** | 与热图同源的长表数据；页面最多预览 **5000** 行。 |
| **导出 · 指标 CSV** | 上表完整字段，UTF-8 BOM，Excel 可直接打开。 |
| **导出 · 逐密码子 CSV** | 每行：位点、氨基酸、候选名、密码子、参考密码子、宿主频率、相对适应性、是否稀有等。 |
| **导出 · JSON** | 宿主信息、目标摘要、各候选指标、对比行数等，便于程序再处理。 |
| **导出 · FASTA** | 仅 **通过校验且进入排名** 的候选序列。 |

---

## 5. 它是怎么实现的？（原理层面）

- **全部在浏览器里运行**：一个 `.html` 文件里包含 **界面（HTML/CSS）** 和 **逻辑（JavaScript）**，**没有** 后端服务器、**不** 自动访问 IDT/GenScript 网站。  
- **宿主频率表**：黑曲霉 Kazusa 5061 的密码子 **Kazusa 原始计数（`observed_count`）** 以内嵌 CSV 文本形式写在页面脚本里；页面在载入时按氨基酸簇归一化为相对频率。**离线** 即可用。旁路文件 [`aspergillus_niger_5061.csv`](aspergillus_niger_5061.csv) 与 [`aspergillus_niger_5061_SOURCE.md`](aspergillus_niger_5061_SOURCE.md) 记录数据来源。  
- **翻译与遗传密码**：标准核基因密码子表（与黑曲霉 CDS 常用表一致）。  
- **CAI/CSI 风格分数**：对每个密码子取 Kazusa 同义簇内 **相对适应性**（频率/同义最大频率），再对数平均（与 `codon_core` 一致思路）。  
- **CFD%**：密码子相对适应性 **低于** 所选阈值的位点比例（与 CodonTransformer 文档中 CFD 构造一致思路）。  
- **排名分**：在 `codon_core.py` 中 `ranking_score` 的同一套加权公式在 JS 中复现。  
- **隐私**：序列 **不会上传** 到任何服务器；仅在本地内存中计算与下载。

---

## 6. 与命令行工具的关系

- **`codon_metrics_cli.py`**：适合批处理、脚本流水线；依赖 Python + `biopython` / `pandas` / `python_codon_tables`（见 `requirements-mini.txt`）。  
- **`aniger_codon_review.html`**：适合无 Python 环境的电脑、会议现场快速评审。  

两者宿主表均指向 **Kazusa A. niger 5061**；细指标命名可能略有差异，以各自导出 CSV 表头为准。

---

## 7. 常见问题

**Q：为什么我的候选全部「未通过」？**  
A：多为 **翻译蛋白与目标不一致**（缺终止子、移码、错了一个 aa）。检查 CDS 是否整段为 3 的倍数、是否与公司返回的蛋白序列一致。

**Q：为什么没有 Excel 一键导出？**  
A：单文件 HTML 为保持 **零依赖**，未内置 xlsx 库；用 **指标 CSV + 逐密码子 CSV** 在 Excel 中打开即可。

**Q：双击打不开或按钮无反应？**  
A：换 Chrome/Edge；若公司策略禁止本地脚本，可把同一 HTML 放到内网简单静态文件服务器上，用 `http://` 打开。

---

## 附录 A：Codon_1_import 逐步示例（与仓库中 `analysis/Codon_1_export.dna.fasta` 对比）

以下路径以本仓库为例：`analysis/Codon_1_import.dna.fasta`、`analysis/Codon_1_export.dna.fasta`。

### A.1 仅用「原始/目标」+ 本地候选

1. 用浏览器打开 `mini app/aniger_codon_review.html`。  
2. 在 **原始/目标** 中粘贴或上传 `Codon_1_import.dna.fasta` 全文（含 `>Codon_1_extracted_dna_len897`）。  
3. **候选** 可留空；保持勾选 **生成本地候选**，随机种子默认即可。  
4. 点击 **分析**。  

**预期：**

- 顶部提示目标蛋白 **298 aa**、原始 DNA **897 nt**（末尾终止子 **TAG**）。  
- **指标与排名** 至少 4 行：`name` 为 `Codon_1_extracted_dna_len897` 的 **原始行**（`source=original`），以及 `local_highest_frequency`、`local_weighted_random`、`local_balanced_gc_gc3`。  
- **逐密码子热图** 中 **Ref** 列 = 导入序列在各位的密码子；与「本地 HFC」等列对照可看同义替换。  
- **导出** 可下载指标 CSV、逐密码子 CSV、JSON、通过候选 FASTA。

### A.2 增加「酵母优化版」作候选（import vs export）

1. 保持 **原始/目标** 仍为 `Codon_1_import`（定义目标蛋白与 Ref）。  
2. 在 **候选** 中再粘贴或上传 `Codon_1_export.dna.fasta`（或与其合并的多条 FASTA）。  
3. **分析**。  

**前提：** 导出序列翻译后必须与 import **同一蛋白**（长度一致、无内部终止）；否则会进入 **未通过** 并在 `errors` 中说明。若一致，可在热图中对比 **Ref（import）** 与各候选列（含 export）的密码子差异，并从 **指标** 看黑曲霉 Kazusa 意义下的 CAI/CFD 等。

### A.3 结果怎么读（摘要）

- **进入排名**：翻译与目标蛋白一致且 CDS 形状合法。  
- **`ranking_score`**：多指标加权分，**仅作候选间排序参考**，不保证表达量。  
- **热图颜色**：与 Ref 一致 / 改变 / 稀有（相对适应性低于 CFD 阈值）/ 非同义错误（应极少见，若出现说明数据有误）。

---

## 附录 B：导出表中 `name` 列含义

| `name`（CSV 全名） | 含义 |
|--------------------|------|
| **与 FASTA `>` 首词相同**（如 `Codon_1_extracted_dna_len897`） | 来自 **原始/目标** 的参考 DNA 行；`source` 为 `original`。若 `>` 后无名字则为 `original_reference`。 |
| `local_highest_frequency` | 本地 **HFC**（每 aa 取 Kazusa 最高频密码子 + 高频终止子）。 |
| `local_weighted_random` | 本地按 Kazusa **频率加权随机**（受随机种子影响）。 |
| `local_balanced_gc_gc3` | 本地 **GC / GC3 平衡** 贪心序列。 |
| **其他** | 来自您在 **候选** 区上传/粘贴的 FASTA `>` 名或 CSV 的 `name`/`id`；重名时程序会加 `_2`、`_3` 等后缀。 |

界面表格列宽可能截断名称，**以导出 CSV 的 `name` 列为准**。

---

*文档版本：与 `aniger_codon_review.html` 配套；修订时请同步检查页面内嵌逻辑是否变更。*

# Aspergillus niger (黑曲霉) Codon Usage Enrichment Ideas

This document describes enrichment ideas for `aspergillus_niger_5061.csv`, focusing on making the codon optimizer more useful for *Aspergillus niger* (黑曲霉) culture and gene expression.

**Current baseline columns（当前基线表）**：`aspergillus_niger_5061.csv` 现为 **`amino_acid`, `codon`, `observed_count`** —— 即 [Kazusa 5061](https://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi?species=5061) 括号内整数计数；相对频率由工具按簇归一化。下文建议的新列应追加在右侧，并保持每簇 `observed_count` 与 Kazusa 或自建统计一致后再派生 RSCU 等。

---

## 1. Purpose / 目的

- Provide practical ways to enrich the codon usage CSV for optimization in *A. niger*.
- Include both English and Chinese descriptions in the same file.
- Focus on metrics, comparisons, and data fields that support codon selection and expression prediction.

- 为黑曲霉的密码子优化提供实用增强方案。
- 在同一个文件中同时包含英文和中文说明。
- 重点是支持密码子选择和表达量预测的指标、比较和数据字段。

---

## 2. Recommended CSV Enrichment Fields / 推荐添加字段

1. `RSCU` (Relative Synonymous Codon Usage)
   - Explain how often a codon is used relative to expected usage for its amino acid.
   - Useful for identifying over-used and under-used codons.

1. `RSCU`（相对同义密码子使用频率）
   - 解释某个密码子相对于氨基酸的预期使用频率。
   - 有助于识别过度使用和低频密码子。

1. `OptimalityScore`
   - A normalized score (0–1) combining frequency, RSCU, and host preference.
   - Can be used directly by optimization tools to rank codons.

1. `OptimalityScore`
   - 一个归一化分数（0–1），结合了频率、RSCU 和宿主偏好。
   - 可作为优化工具直接排序密码子。

1. `tRNA_copy_number` or `tRNA_abundance`
   - Add tRNA gene copy counts or predicted abundance if available for *A. niger*.
   - Helps identify codons that may slow translation because of low tRNA supply.

1. `tRNA_copy_number` 或 `tRNA_abundance`
   - 如果可用，添加黑曲霉的 tRNA 基因拷贝数或预测丰度。
   - 有助于识别因 tRNA 供应不足而可能减慢翻译的密码子。

1. `GC_content` and `GC3_content`
   - Report the GC percentage of each codon or codon group.
   - Useful for balancing overall GC content in synthetic CDS designs.

1. `GC_content` 和 `GC3_content`
   - 报告每个密码子或密码子组的 GC 百分比。
   - 对于在合成 CDS 设计中平衡整体 GC 含量非常有用。

1. `CAI_reference` or `CAI_score`
   - Add a CAI-like metric based on a reference set of highly expressed *A. niger* genes.
   - Supports optimization toward host-preferred expression patterns.

1. `CAI_reference` 或 `CAI_score`
   - 添加基于高表达黑曲霉基因参考集的类 CAI 指标。
   - 支持朝宿主偏好的表达模式进行优化。

1. `UsageRank` or `PreferredFlag`
   - Rank codons within each synonymous amino acid group.
   - Add a boolean column such as `preferred` for codons that are recommended by the host.

1. `UsageRank` 或 `PreferredFlag`
   - 在每个同义氨基酸组内对密码子进行排序。
   - 添加一个布尔列，例如 `preferred`，表示宿主推荐的密码子。

1. `Source` and `Confidence`
   - Document the origin of the data and a confidence level.
   - Example: `Kazusa 5061`, `predicted from genome`, `experimental`.

1. `Source` 和 `Confidence`
   - 记录数据来源和置信等级。
   - 例如：`Kazusa 5061`、`predicted from genome`、`experimental`。

---

## 3. Suggested Data Extensions / 建议扩展数据

1. Add additional rows for related strains or conditions
   - Example: add codon usage from another *A. niger* strain or a closely related Aspergillus species.
   - Add a `condition` or `strain` column for comparisons.

1. 添加相关菌株或条件的行
   - 例如：添加来自另一株黑曲霉或近缘曲霉物种的密码子使用数据。
   - 添加 `condition` 或 `strain` 列以便进行比较。

1. Add comparisons to common hosts
   - Include columns for `E_coli`, `S_cerevisiae`, or `A_oryzae` codon frequencies.
   - Add `delta_frequency` columns to show differences versus *A. niger*.

1. 添加与常见宿主的比较
   - 包括 `E_coli`、`S_cerevisiae` 或 `A_oryzae` 的密码子频率列。
   - 添加 `delta_frequency` 列以显示与黑曲霉的差异。

1. Add experimental or expression-linked annotations
   - `high_expression_codon`, `low_expression_codon`, or `proteomics_support`
   - Useful if you have fermentation expression data or proteomics for *A. niger*.

1. 添加实验或表达相关注释
   - `high_expression_codon`、`low_expression_codon` 或 `proteomics_support`
   - 如果有发酵表达数据或黑曲霉蛋白质组数据，这些信息非常有用。

---

## 4. Practical Use Cases / 实用场景

- Use the enriched CSV to build a codon optimizer that selects preferred codons for *A. niger*.
- Use RSCU and CAI-like scores to avoid rare or low-abundance codons in synthetic designs.
- Compare output rankings across strains or culture conditions.
- Build a candidate scoring system for synthetic gene design, prioritizing both codon bias and GC balance.

- 使用增强过的 CSV 构建一个为黑曲霉选择推荐密码子的优化器。
- 使用 RSCU 和类 CAI 分数来避免合成设计中的稀有或低丰度密码子。
- 比较不同菌株或培养条件下的输出排名。
- 构建一个合成基因设计候选评分系统，优先考虑密码子偏好和 GC 平衡。

---

## 5. Implementation Notes / 实施说明

- Start by calculating derived metrics from the current CSV: `RSCU`, `OptimalityScore`, `GC_content`, `GC3_content`.
- If available, add tRNA copy number or abundance data from *A. niger* genome annotations.
- Use external references such as Kazusa codon tables, CUTG, or NCBI fungal genome data for support.
- Keep the CSV organized with clear column names and a `source` field for traceability.

- 从当前 CSV 开始计算派生指标：`RSCU`、`OptimalityScore`、`GC_content`、`GC3_content`。
- 如果可用，从黑曲霉基因组注释中添加 tRNA 拷贝数或丰度数据。
- 使用 Kazusa 密码子表、CUTG 或 NCBI 真菌基因组数据作为参考。
- 使用清晰的列名和 `source` 字段保持 CSV 的可跟踪性。

---

## 6. Recommended File Name / 推荐文件名

- `mini app/aspergillus_niger_5061_enrichment_ideas.md`

- `mini app/aspergillus_niger_5061_enrichment_ideas.md`

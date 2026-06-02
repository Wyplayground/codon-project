# Aspergillus niger — 密码子频率表数据来源与口径

## 物种与快照

| 项目 | 值 |
|------|-----|
| 物种 | *Aspergillus niger* |
| NCBI taxid | **5061** |
| 数据来源 | [Kazusa Codon Usage Database](https://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi?species=5061) |
| 页面摘要（摘录） | 13905 CDS · **6,130,423** codons；编码区 GC **53.76%**；第三位 GC **59.39%**（与离线页 `ANIGER_CODING_GC` / `ANIGER_GC3` 一致） |
| 表抓取 / 重算日期 | 2026-05-12（与 CSV 内嵌计数一致；若 Kazusa 后台更新，计数可能微变，需重新运行构建脚本） |

## 统计口径

1. **原始计数**：来自 Kazusa 页面「per thousand (number)」中的 **括号内整数计数**；RNA 三联体已换写为 **DNA**（T 代 U）。
2. **同义簇 `relative_frequency`**：对每一组编码同一氨基酸的密码子，  
   `relative_frequency = observed_count / sum(observed_count)`，故**每组和为 1**（与 CSI / 相对适应性计算一致）。
3. **终止密码子**：`TAA`、`TAG`、`TGA` 单独成簇，三者频率和为 1；下游 CSI 通常只对**编码**密码子几何平均（HTML 已排除终止子参与 CSI），与本表不冲突。
4. **RSCU**：由脚本内归一化后的相对频率与簇内密码子数可得：`RSCU = relative_frequency × n_synonymous`（与 `host_rscu` / 文献定义一致）。

## 与旧版 CSV 的差异

旧版为三列 `relative_frequency` 小数。现版 **`aspergillus_niger_5061.csv` 仅保留 Kazusa 原始 `observed_count`**（三列：`amino_acid`, `codon`, `observed_count`），相对频率在浏览器或分析脚本中按簇求和归一化，避免手写小数的舍入漂移。

## 重建命令（可选）

在 `mini app/new version` 目录执行：

`python generate_kazusa5061_table.py`

可从脚本内嵌的 Kazusa 文本块重新生成 `aspergillus_niger_5061.csv`（需与 Kazusa 网页同步更新块内计数时运行）。

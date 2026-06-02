# Aspergillus niger 密码子频率表（多来源）

生成时间（UTC）：2026-05-14T06:07:50Z

## 文件

| 文件 | 来源说明 |
|------|----------|
| `aspergillus_niger_kazusa.tsv` | [Kazusa Codon Usage Database](https://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi?species=5061)，物种合并统计（taxid 5061）。 |
| `aspergillus_niger_refseq_cds_GCF_000002855.4_computed.tsv` | NCBI RefSeq 组装 **GCF_000002855.4**（CBS 513.88 / ASM285v2），由 `cds_from_genomic.fna.gz` 重算。FTP: `https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/002/855/GCF_000002855.4_ASM285v2/GCF_000002855.4_ASM285v2_cds_from_genomic.fna.gz` |
| `aspergillus_niger_ncbi_genbank_cds_GCA_000230395.2_computed.tsv` | NCBI GenBank 组装 **GCA_000230395.2**（ATCC 1015 / ASPNI v3），由 `cds_from_genomic.fna.gz` 重算。FTP: `https://ftp.ncbi.nlm.nih.gov/genomes/genbank/fungi/Aspergillus_niger/latest_assembly_versions/GCA_000230395.2_ASPNI_v3.0/GCA_000230395.2_ASPNI_v3.0_cds_from_genomic.fna.gz` |
| `aspergillus_niger_ncbi_hivecuts.tsv` | **优先**：GWU HIVE CGI 解析的 CoCoPUTs。**若返回 403**，脚本改为写入与 **RefSeq cds（GCF_000002855.4）** 相同的计数（CoCoPUTs「RefSeq 优先」的可复现替代）；需要与网页完全一致时可从 [FDA DNA HIVE](https://dnahive.fda.gov/dna.cgi?cmd=cuts_main) 导出覆盖。 |
| `cross_check_summary.tsv` | 各表 `fraction` 两两 Pearson 相关与 Top10 绝对差异密码子。 |
| `aspergillus_niger_one_for_all.csv` | **宽表**：每个密码子一行，各来源的 `count` / `fraction` / `per_thousand` 并排（逗号分隔，便于 Excel）。列名前缀为 `kazusa_`、`refseq_…`、`genbank_…`、`hivecuts_`。 |
| `fetch_log.txt` | 运行日志。 |

## 列说明

所有 `*.tsv`：`codon`（DNA ACGT）、`count`、`fraction`、`per_thousand`、`source`、`taxid`、`assembly`、`downloaded_on`。

## 注意

- **Kazusa 合并表** vs **单一组装重算表**口径不同，数值接近但不应期待完全一致。
- CDS 计数时跳过 **长度非 3 倍数** 或 **含非 ACGT** 的序列（见各 `.meta.json`）。

# codon-project

Public repository for *Aspergillus niger* codon work: an offline **candidate-review visualization**, reference frequency tables, and (in development) codon optimization models.

**Open the visualization tool:** https://wyplayground.github.io/codon-project/visualization/

This URL is the product link to share with collaborators. The GitHub repo holds source code and data for the full project.

## Project layout

| Path | Description |
|------|-------------|
| [`docs/visualization/`](docs/visualization/) | Bilingual review app (`index.html`), full HTML app, HOWTO/SOP, Kazusa CSV, frequency tables, demo sequences |
| [`docs/visualization/index.html`](docs/visualization/index.html) | Simplified offline review app (English default, EN \| 中文 toggle) |
| [`model/`](model/) | Codon optimization model code (planned / in development) |
| [`scripts/`](scripts/) | Build helper for bilingual `docs/visualization/index.html` |

## Quick start (visualization)

1. Open the [visualization tool](https://wyplayground.github.io/codon-project/visualization/) or `docs/visualization/index.html` locally in a browser (fully offline; Kazusa taxid 5061 data is embedded).
2. Paste an original/target sequence and one or more candidate sequences (FASTA or CSV).
3. Compare CSI, GC%, low-adapted codon %, and per-position codon maps.

See [`docs/visualization/aniger_codon_review_simple_HOWTO.md`](docs/visualization/aniger_codon_review_simple_HOWTO.md) for step-by-step instructions (Chinese).

## Rebuild bilingual homepage

```bash
python scripts/build_bilingual_index.py
```

Source HTML: CodonTransformer `05_mini_apps` deliverable (`aniger_codon_review_simple.html`).

## Roadmap

- [x] Publish visualization and reference tables under `/visualization/`
- [ ] Codon optimization model under `model/`
- [ ] Additional algorithms as the project grows

## License

Apache License 2.0 — see [LICENSE](LICENSE).

---

## 中文简介

本仓库是**黑曲霉（*Aspergillus niger*）**密码子相关工作的公开项目：候选序列评审可视化、频率表数据，以及规划中的密码子优化模型。

- **可视化工具（对外分享链接）：** https://wyplayground.github.io/codon-project/visualization/
- 详细操作见 [`docs/visualization/aniger_codon_review_simple_HOWTO.md`](docs/visualization/aniger_codon_review_simple_HOWTO.md)

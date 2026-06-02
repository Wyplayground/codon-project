# codon-project

Offline tools and reference data for reviewing *Aspergillus niger* codon-optimized CDS candidates.

**Live site (GitHub Pages):** https://wyplayground.github.io/codon-project/

## What this repo contains

| Path | Description |
|------|-------------|
| [`docs/`](docs/) | GitHub Pages site: bilingual candidate-review app, full HTML app, HOWTO/SOP, Kazusa CSV, frequency tables, and demo sequences |
| [`docs/index.html`](docs/index.html) | **Homepage** — simplified offline review app (English default, EN \| 中文 toggle) |
| [`docs/aniger_codon_review.html`](docs/aniger_codon_review.html) | Full-featured offline review app (Chinese UI) |
| [`docs/data/`](docs/data/) | Source notes and computed codon-frequency tables |
| [`docs/examples/`](docs/examples/) | Demo FASTA/CSV inputs |
| [`model/`](model/) | Placeholder for future codon optimization model code |
| [`scripts/`](scripts/) | Build helper for bilingual `docs/index.html` |

## Quick start

1. Open the [live site](https://wyplayground.github.io/codon-project/) or `docs/index.html` locally in a browser (fully offline; Kazusa taxid 5061 data is embedded).
2. Paste an original/target sequence and one or more candidate sequences (FASTA or CSV).
3. Compare CSI, GC%, low-adapted codon %, and per-position codon maps.

See [`docs/aniger_codon_review_simple_HOWTO.md`](docs/aniger_codon_review_simple_HOWTO.md) for step-by-step instructions (Chinese).

## Rebuild bilingual homepage

```bash
python scripts/build_bilingual_index.py
```

Source HTML: CodonTransformer `05_mini_apps` deliverable (`aniger_codon_review_simple.html`).

## Roadmap

- [x] Publish visualization site and reference tables
- [ ] Codon optimization model under `model/`

## License

Apache License 2.0 — see [LICENSE](LICENSE).

---

## 中文简介

本仓库提供**黑曲霉（*Aspergillus niger*）**密码子候选序列的离线评审工具与频率表数据。

- 在线访问：https://wyplayground.github.io/codon-project/
- 主页 `docs/index.html` 默认英文，可切换中文
- 详细操作见 [`docs/aniger_codon_review_simple_HOWTO.md`](docs/aniger_codon_review_simple_HOWTO.md)

"""Build docs/visualization/index.html (English default + Chinese toggle) from the simple deliverable."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r"D:/2026/CodonTransformer-main/05_mini_apps/deliverables/基于黑曲霉的密码子可视化交付物/aniger_codon_review_simple.html")
OUT = ROOT / "docs" / "visualization" / "index.html"

I18N_BLOCK = r'''
  let LANG = "en";
  const I18N = {
    en: {
      page_title: "A. niger codon candidate review (simple)",
      header_title: '<i>Aspergillus niger</i> codon candidate review (simple)',
      header_sub: "Offline single-file HTML. Check that external/manual CDS candidates encode the same protein; compare CSI, GC%, and low-adapted codon %.",
      label_ref: "Original / target sequence",
      label_cand: "Candidate sequences",
      ph_ref: ">linB_original\nATG...TAG",
      ph_cand: "Multi-FASTA or CSV: name,source,sequence",
      chk_local: "Generate local reference candidates (fixed seed; not ranked)",
      help_src_title: "Candidate sources",
      help_src_p1: "This page does not submit to IDT, GenScript, JCat, etc. Paste FASTA / CSV / plain sequence from vendors here to compare.",
      help_src_p2: 'Use FASTA headers or CSV <code>source</code> values such as <code>manual</code>, <code>IDT</code>, <code>GenScript</code>, <code>JCat</code>, <code>company_A</code>.',
      help_src_p3: '<a href="https://www.kazusa.or.jp/codon/" target="_blank" rel="noopener noreferrer">Kazusa Codon Usage</a> table for <i>A. niger</i> taxid 5061 is embedded.',
      btn_run: "Analyze candidates",
      tab_metrics: "Metrics & ranking",
      tab_codons: "Codon map",
      tab_long: "Per-position table",
      tab_export: "Export",
      unit_aa: "aa",
      unit_nt: "nt",
      unit_count: "",
      summary_protein_len: "Target protein length",
      summary_original_cds: "Original CDS",
      summary_ext_pass: "External passed",
      summary_ext_fail: "External failed",
      not_provided: "N/A",
      ranking_notice: "Ranking aids screening only: higher <strong>CSI</strong>, then lower <strong>low-adapted codon %</strong>, then <strong>GC%</strong> closer to host coding GC {gc}%; no expression prediction score.",
      metrics_help_title: "CSI, GC%, low-adapted %, errors, warnings, status",
      metrics_help_csi: "<strong>CSI (codon adaptation index)</strong> measures how closely the CDS matches <i>A. niger</i> preferred codons (geometric mean of relative adaptiveness; M, W, and stop codons skipped).",
      metrics_help_gc: "<strong>GC%</strong> is the fraction of G+C bases in the DNA sequence.",
      metrics_help_low: "<strong>Low-adapted codon %</strong> is the fraction of coding codons whose relative adaptiveness is strictly below the threshold (stop codons excluded). The threshold affects this metric and heatmap coloring only, not CSI or GC%.",
      metrics_help_errors: "<strong>errors</strong> are hard failures (invalid bases, length, internal stops, translation mismatch, etc.). Any error means <strong>failed</strong>.",
      metrics_help_warnings: "<strong>warnings</strong> are reminders (e.g. start not ATG). Warnings alone still allow <strong>pass</strong> if errors are empty.",
      metrics_help_status: "<strong>status</strong> for external candidates: <strong>Pass</strong> only if errors are empty and translated protein matches the target exactly.",
      h2_external_rank: "External / manual candidate ranking",
      hint_external_rank: "Only candidates that passed validation (no errors; protein match).",
      no_external_pass: "No external candidates passed translation consistency checks.",
      h2_reference: "Original sequence baseline",
      hint_no_dna_baseline: "Target entered as protein only; no original DNA baseline.",
      h2_external_fail: "Failed external candidates",
      h2_local: "Program-generated reference candidates (not ranked)",
      hint_local: "Generated from the embedded <i>A. niger</i> frequency table for local reproducible reference; not a guarantee of highest expression.",
      no_local: "No local reference candidates were generated.",
      h2_codon_map: "Per-position codon map",
      codon_map_notice: "Each row is one amino-acid/codon position; each column is one sequence. Cell values are 3 bp codons. Up to 360 positions shown.",
      label_threshold: "Low-adapted codon threshold",
      hint_slider: "Moving the slider updates rare coloring here and low-adapted % on the Metrics tab.",
      threshold_help_title: "What is the low-adapted codon threshold?",
      threshold_help_p1: "<strong>Relative adaptiveness</strong> = codon frequency ÷ highest synonymous frequency for that amino acid (0–1).",
      threshold_help_p2: "Codons with relative adaptiveness <strong>strictly below</strong> the threshold count as low-adapted/rare.",
      legend_same: "Same as original",
      legend_changed: "Synonymous change",
      legend_rare: "Relative adaptiveness below {t}",
      legend_bad: "Non-synonymous / error",
      no_heatmap: "No passing sequences available for per-position comparison.",
      h2_long: "Per-position detail (export)",
      long_notice: 'Long table: one row per candidate × position. <code>relative_adaptiveness</code> = codon freq / max synonymous freq; <code>rare</code> = below threshold; <code>gc3</code> = third base G or C.',
      long_truncated: "Showing first 5000 rows only; export CSV for the full table.",
      h2_export: "Export",
      export_notice: "Candidate metrics CSV is enabled. Other export buttons are reserved for a future release.",
      btn_metrics_csv: "Candidate metrics CSV",
      btn_detail_csv: "Per-position CSV",
      btn_json: "JSON report",
      btn_fasta_ext: "Passed external FASTA",
      btn_fasta_local: "Local reference FASTA",
      btn_future: "Coming in a later version",
      no_data: "(no data)",
      status_ref: "Original baseline",
      status_local_ok: "Local reference",
      status_local_bad: "Local error",
      status_pass: "Pass",
      status_fail: "Fail",
      col_rank: "rank", col_name: "name", col_source: "source", col_status: "status",
      col_len_nt: "len_nt", col_codon_count: "codon_count", col_csi: "CSI", col_gc: "GC%",
      col_low_adapted: "Low-adapted codon %", col_gc3: "GC3%", col_errors: "errors", col_warnings: "warnings",
      col_note: "note", col_included: "included_in_ranking", col_is_local: "is_local_reference",
      col_position: "position", col_amino_acid: "amino_acid", col_candidate: "candidate", col_codon: "codon",
      col_reference_codon: "reference_codon", col_same_as_reference: "same_as_reference",
      col_synonymous: "synonymous_with_target", col_host_frequency: "host_frequency",
      col_relative_adaptiveness: "relative_adaptiveness", col_rare: "rare", col_gc3_flag: "gc3",
      heat_position: "position", heat_aa: "AA", heat_original: "original",
      msg_target_ok: "Target protein {aa} aa; {cds}",
      msg_target_protein_only: "Target entered as protein",
      msg_original_cds: "Original CDS {nt} nt",
      local_note_hfc: "Highest-frequency synonymous codon per amino acid; often high CSI but may skew GC/GC3.",
      local_note_weighted: "Frequency-weighted random codons (fixed seed 42 for reproducibility).",
      local_note_balanced: "Balance relative adaptiveness with coding GC {gc}% and GC3 {gc3}%; reference only, not an expression guarantee.",
      err_no_ref: "No original/target sequence provided.",
      err_empty_ref: "Original/target sequence is empty.",
      err_invalid_ref_cds: "Invalid original CDS: {detail}",
      err_ref_internal_stop: "Original CDS contains an internal stop codon.",
      err_protein_internal_stop: "Target protein contains an internal stop symbol.",
      err_not_dna_or_protein: "Target is neither standard DNA nor standard protein: {chars}",
      err_invalid_bases: "Non A/C/G/T bases: {chars}",
      err_len_not_multiple: "Length {len} nt is not a multiple of 3",
      err_too_short: "Sequence too short to be a CDS",
      warn_start_not_atg: "Start codon is {codon}, not ATG",
      err_or_warn_no_stop: "Last codon {codon} is not a stop codon",
      err_internal_stops: "Internal stop codon(s) at position(s): {pos}",
      err_unknown_codon: "Unknown codon(s); translation incomplete",
      err_protein_mismatch: "Translated protein differs from target ({detail})",
      err_must_be_dna: "Candidate must be a DNA CDS, not a protein sequence",
      mismatch_len: "target {t} aa, candidate {c} aa",
      mismatch_pos: "position {i}: target {t}, candidate {c}",
      mismatch_unknown: "unknown difference",
      json_scoring_note: "External ranking: higher CSI, lower low-adapted %, GC% closer to host coding GC; no combined expression score."
    },
    zh: {
      page_title: "黑曲霉密码子候选评审（简化版）",
      header_title: "黑曲霉（<i>Aspergillus niger</i>）密码子候选评审：简化版",
      header_sub: "离线单文件 HTML。重点审核外部/人工候选 CDS 是否编码同一蛋白，并用 CSI、GC content、低适配密码子比例做简洁比较。",
      label_ref: "原始/目标序列", label_cand: "候选序列",
      ph_ref: ">linB_original\nATG...TAG",
      ph_cand: "支持多条 FASTA，或 CSV：name,source,sequence",
      chk_local: "生成程序参考候选（固定内部种子，不参与排名）",
      help_src_title: "候选来源说明",
      help_src_p1: "本页不自动提交 IDT、GenScript、JCat 等网站。请把网站或基因公司返回的 FASTA / CSV / 纯序列粘贴到上方文本框后统一比较。",
      help_src_p2: "FASTA header 或 CSV 的 <code>source</code> 列可写 <code>manual</code>、<code>IDT</code>、<code>GenScript</code>、<code>JCat</code>、<code>company_A</code> 等来源标签。",
      help_src_p3: '<a href="https://www.kazusa.or.jp/codon/" target="_blank" rel="noopener noreferrer">Kazusa Codon Usage</a> 的黑曲霉 taxid 5061 频率表已内嵌。',
      btn_run: "分析候选",
      tab_metrics: "指标与排序", tab_codons: "逐位点密码子对照图",
      tab_long: "逐位点明细表（导出用）", tab_export: "导出",
      unit_aa: "aa", unit_nt: "nt", unit_count: "条",
      summary_protein_len: "目标蛋白长度", summary_original_cds: "原始 CDS",
      summary_ext_pass: "外部候选通过", summary_ext_fail: "外部候选未通过",
      not_provided: "未提供",
      ranking_notice: "排序只用于辅助筛选：先按 <strong>CSI</strong> 高低，再按 <strong>低适配密码子%</strong> 低高，最后按 <strong>GC%</strong> 接近黑曲霉编码区 GC {gc}% 的程度排序；不输出综合表达量预测分。",
      metrics_help_title: "CSI、GC%、低适配密码子%、errors、warnings 与状态列说明",
      metrics_help_csi: "<strong>CSI（密码子适应指数）</strong>反映整条 CDS 与黑曲霉偏好密码子的接近程度。",
      metrics_help_gc: "<strong>GC%</strong>为整条 DNA 序列中 G 与 C 所占比例。",
      metrics_help_low: "<strong>低适配密码子%</strong>为相对适应度严格小于阈值的编码密码子所占比例；终止密码子不计入。",
      metrics_help_errors: "<strong>errors</strong>为硬错误信息列表。只要存在任一条 error，该候选即<strong>未通过</strong>。",
      metrics_help_warnings: "<strong>warnings</strong>为提醒信息。仅有 warnings 而 errors 为空时，仍可通过验证。",
      metrics_help_status: "<strong>状态</strong>：「通过」当且仅当 errors 为空且翻译蛋白与目标完全一致。",
      h2_external_rank: "外部/人工候选排序",
      hint_external_rank: "仅展示已通过验证的候选（无 errors 且翻译与目标蛋白一致）。",
      no_external_pass: "暂无通过翻译一致性验证的外部候选。",
      h2_reference: "原始序列基线",
      hint_no_dna_baseline: "目标以蛋白形式输入，没有原始 DNA 基线。",
      h2_external_fail: "未通过的外部候选",
      h2_local: "程序生成参考候选（不参与总体排名）",
      hint_local: "以下序列由本页根据黑曲霉频率表生成，主要用于本地可复现参考，不代表一定最高表达。",
      no_local: "未生成本地参考候选。",
      h2_codon_map: "逐位点密码子对照图",
      codon_map_notice: "每一行是一个氨基酸/密码子位置，每一列是一条序列。最多显示前 360 个密码子位点。",
      label_threshold: "低适配密码子阈值",
      hint_slider: "拖动滑块会实时更新稀有着色，并同步刷新指标页中的低适配密码子%。",
      threshold_help_title: "什么是低适配密码子阈值？",
      threshold_help_p1: "相对适应度 = 该密码子频率 ÷ 同氨基酸最高频密码子频率（0～1）。",
      threshold_help_p2: "相对适应度严格小于阈值的编码密码子计为低适配/稀有。",
      legend_same: "与原始序列相同", legend_changed: "同义替换",
      legend_rare: "相对适应度低于 {t}", legend_bad: "非同义/错误位点",
      no_heatmap: "没有可用于逐位点对照的通过序列。",
      h2_long: "逐位点明细表（导出用）",
      long_notice: "每一行对应某条候选序列 × 某个密码子位置。",
      long_truncated: "页面仅显示前 5000 行，请导出 CSV 查看全部。",
      h2_export: "导出",
      export_notice: "当前版本只开放候选指标 CSV 下载。",
      btn_metrics_csv: "候选指标 CSV", btn_detail_csv: "逐位点明细 CSV",
      btn_json: "JSON 报告", btn_fasta_ext: "通过外部候选 FASTA", btn_fasta_local: "本地参考候选 FASTA",
      btn_future: "后续版本启用", no_data: "（无数据）",
      status_ref: "原始基线", status_local_ok: "本地参考", status_local_bad: "本地异常",
      status_pass: "通过", status_fail: "未通过",
      col_rank: "rank", col_name: "name", col_source: "source", col_status: "status",
      col_len_nt: "len_nt", col_codon_count: "codon_count", col_csi: "CSI", col_gc: "GC%",
      col_low_adapted: "低适配密码子%", col_gc3: "GC3%", col_errors: "errors", col_warnings: "warnings",
      col_note: "note", col_included: "included_in_ranking", col_is_local: "is_local_reference",
      col_position: "position", col_amino_acid: "amino_acid", col_candidate: "candidate", col_codon: "codon",
      col_reference_codon: "reference_codon", col_same_as_reference: "same_as_reference",
      col_synonymous: "synonymous_with_target", col_host_frequency: "host_frequency",
      col_relative_adaptiveness: "relative_adaptiveness", col_rare: "rare", col_gc3_flag: "gc3",
      heat_position: "position", heat_aa: "AA", heat_original: "original",
      msg_target_ok: "目标蛋白 {aa} aa；{cds}",
      msg_target_protein_only: "目标以蛋白形式输入",
      msg_original_cds: "原始 CDS {nt} nt",
      local_note_hfc: "每个氨基酸选黑曲霉频率表中最高频的同义密码子，通常 CSI 较高，但可能让 GC/GC3 偏向单一。",
      local_note_weighted: "按黑曲霉同义密码子频率抽样生成，固定内部种子 42 保证每次结果一致。",
      local_note_balanced: "在相对适应度、黑曲霉编码区 GC {gc}% 和 GC3 {gc3}% 之间折中；仅供参考，不是表达量保证。",
      err_no_ref: "没有提供原始/目标序列。", err_empty_ref: "原始/目标序列为空。",
      err_invalid_ref_cds: "原始 CDS 无效：{detail}", err_ref_internal_stop: "原始 CDS 含内部终止密码子。",
      err_protein_internal_stop: "目标蛋白序列含内部终止符号。",
      err_not_dna_or_protein: "目标序列既不是标准 DNA，也不是标准蛋白序列：{chars}",
      err_invalid_bases: "含非 A/C/G/T 碱基：{chars}",
      err_len_not_multiple: "长度 {len} nt 不是 3 的倍数", err_too_short: "序列太短，不能作为 CDS",
      warn_start_not_atg: "起始密码子为 {codon}，不是 ATG",
      err_or_warn_no_stop: "末端密码子 {codon} 不是终止密码子",
      err_internal_stops: "存在内部终止密码子：{pos}",
      err_unknown_codon: "含未知密码子，无法完整翻译",
      err_protein_mismatch: "翻译蛋白与目标不一致（{detail}）",
      err_must_be_dna: "候选必须是 DNA CDS，不能是蛋白序列",
      mismatch_len: "目标 {t} aa，候选 {c} aa",
      mismatch_pos: "第 {i} 位：目标 {t}，候选 {c}",
      mismatch_unknown: "未知差异",
      json_scoring_note: "外部候选排序按 CSI 高、低适配密码子% 低、GC% 接近黑曲霉编码区 GC 参考值排序；没有输出综合表达量预测分。"
    }
  };

  function t(key) {
    const pack = I18N[LANG] || I18N.en;
    return pack[key] != null ? pack[key] : (I18N.en[key] || key);
  }
  function tf(key, params) {
    let s = t(key);
    if (params) for (const [k, v] of Object.entries(params)) s = s.split("{" + k + "}").join(String(v));
    return s;
  }
  function applyStaticI18n() {
    document.documentElement.lang = LANG === "zh" ? "zh-CN" : "en";
    document.title = t("page_title");
    const map = { headerTitle: "header_title", headerSub: "header_sub", labelRef: "label_ref", labelCand: "label_cand",
      chkLocalSpan: "chk_local", helpSrcTitle: "help_src_title", helpSrcP1: "help_src_p1", helpSrcP2: "help_src_p2",
      helpSrcP3: "help_src_p3", btnRun: "btn_run", tabMetrics: "tab_metrics", tabCodons: "tab_codons",
      tabLong: "tab_long", tabExport: "tab_export" };
    for (const [id, key] of Object.entries(map)) {
      const el = document.getElementById(id);
      if (!el) continue;
      if (key === "header_title" || key.startsWith("help_src_p")) el.innerHTML = t(key);
      else el.textContent = t(key);
    }
    document.getElementById("refText").placeholder = t("ph_ref");
    document.getElementById("candText").placeholder = t("ph_cand");
    document.getElementById("btnLangEn").classList.toggle("active", LANG === "en");
    document.getElementById("btnLangZh").classList.toggle("active", LANG === "zh");
  }
  function setLang(lang) {
    LANG = lang === "zh" ? "zh" : "en";
    try { localStorage.setItem("codon_review_lang", LANG); } catch (e) {}
    applyStaticI18n();
    if (lastRunState) renderFromState(currentLowAdaptedThreshold);
  }
  const METRIC_COL_LABEL = { rank: "col_rank", name: "col_name", source: "col_source", status: "col_status",
    len_nt: "col_len_nt", codon_count: "col_codon_count", CSI: "col_csi", "GC%": "col_gc",
    low_adapted_pct: "col_low_adapted", errors: "col_errors", warnings: "col_warnings" };
  const DETAIL_COL_LABEL = { position: "col_position", amino_acid: "col_amino_acid", candidate: "col_candidate",
    source: "col_source", codon: "col_codon", reference_codon: "col_reference_codon",
    same_as_reference: "col_same_as_reference", synonymous_with_target: "col_synonymous",
    host_frequency: "col_host_frequency", relative_adaptiveness: "col_relative_adaptiveness",
    rare: "col_rare", gc3: "col_gc3_flag", included_in_ranking: "col_included", is_local_reference: "col_is_local" };
  function tableHtmlLabeled(rows, allowHtml, colLabelMap) {
    if (!rows.length) return `<p class="hint">${esc(t("no_data"))}</p>`;
    const keys = Object.keys(rows[0]);
    const th = keys.map((key) => `<th>${esc(t(colLabelMap[key] || key))}</th>`).join("");
    const body = rows.map((row) => `<tr>${keys.map((key) => `<td>${allowHtml && key === "status" ? row[key] : esc(row[key])}</td>`).join("")}</tr>`).join("");
    return `<table class="data"><thead><tr>${th}</tr></thead><tbody>${body}</tbody></table>`;
  }
'''

HEADER_HTML = '''  <header>
    <div class="header-row">
      <div><h1 id="headerTitle"></h1><p id="headerSub"></p></div>
      <div class="lang-toggle">
        <button type="button" id="btnLangEn" class="lang-btn active">EN</button><span class="lang-sep">|</span>
        <button type="button" id="btnLangZh" class="lang-btn">中文</button>
      </div>
    </div>
  </header>'''

ASIDE_HTML = '''    <aside>
      <label for="refText" id="labelRef"></label>
      <textarea id="refText"></textarea>
      <label for="candText" id="labelCand"></label>
      <textarea id="candText"></textarea>
      <label class="row"><input type="checkbox" id="chkLocal" checked /><span id="chkLocalSpan"></span></label>
      <details class="help"><summary id="helpSrcTitle"></summary><p id="helpSrcP1"></p><p id="helpSrcP2"></p><p id="helpSrcP3"></p></details>
      <div class="row" style="margin-top:1rem;"><button type="button" class="primary" id="btnRun"></button></div>
    </aside>'''

TABS_HTML = '''      <div class="tabs">
        <button type="button" class="tab active" data-tab="tabMetrics" id="tabMetrics"></button>
        <button type="button" class="tab" data-tab="tabCodons" id="tabCodons"></button>
        <button type="button" class="tab" data-tab="tabLong" id="tabLong"></button>
        <button type="button" class="tab" data-tab="tabExport" id="tabExport"></button>
      </div>'''

HEADER_CSS = '''
    .header-row { display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap; }
    .lang-toggle { display: flex; align-items: center; gap: 0.35rem; font-size: 13px; }
    .lang-btn { padding: 0.3rem 0.55rem; border-radius: 6px; }
    .lang-btn.active { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); font-weight: 650; }
    .lang-sep { color: var(--muted); }
'''

INIT_BLOCK = r'''
  try { const saved = localStorage.getItem("codon_review_lang"); if (saved === "zh" || saved === "en") LANG = saved; } catch (e) {}
  document.getElementById("btnLangEn").addEventListener("click", () => setLang("en"));
  document.getElementById("btnLangZh").addEventListener("click", () => setLang("zh"));
  applyStaticI18n();
'''


def patch_function(src: str, name: str, new_body: str) -> str:
    pattern = rf"function {re.escape(name)}\([^)]*\) \{{"
    m = re.search(pattern, src)
    if not m:
        raise RuntimeError(f"function {name} not found")
    start = m.start()
    depth = 0
    i = m.end() - 1
    while i < len(src):
        if src[i] == "{":
            depth += 1
        elif src[i] == "}":
            depth -= 1
            if depth == 0:
                return src[:start] + new_body + src[i + 1 :]
        i += 1
    raise RuntimeError(f"unclosed function {name}")


FUNCTIONS = {
    "validateCdsShape": r'''function validateCdsShape(dna, requireStop) {
    const errors = []; const warnings = []; const bad = invalidDnaChars(dna);
    if (bad.length) { errors.push(tf("err_invalid_bases", { chars: bad.join(",") })); return { errors, warnings, hasInvalidBases: true }; }
    if (dna.length % 3 !== 0) { errors.push(tf("err_len_not_multiple", { len: dna.length })); return { errors, warnings, hasInvalidBases: false }; }
    if (dna.length < 6) { errors.push(t("err_too_short")); return { errors, warnings, hasInvalidBases: false }; }
    if (dna.slice(0, 3) !== "ATG") warnings.push(tf("warn_start_not_atg", { codon: dna.slice(0, 3) }));
    const last = dna.slice(-3);
    if (!STOP_CODONS.has(last)) { const msg = tf("err_or_warn_no_stop", { codon: last }); if (requireStop) errors.push(msg); else warnings.push(msg); }
    const codons = splitCodons(dna); const internalStops = [];
    for (let i = 0; i < codons.length - 1; i++) if (STOP_CODONS.has(codons[i])) internalStops.push(i + 1);
    if (internalStops.length) errors.push(tf("err_internal_stops", { pos: internalStops.slice(0, 12).join(",") }));
    return { errors, warnings, hasInvalidBases: false };
  }''',
    "buildTarget": r'''function buildTarget(records) {
    if (!records.length) throw new Error(t("err_no_ref"));
    const record = records[0]; const seq = normalizeSeq(record.sequence);
    if (!seq) throw new Error(t("err_empty_ref"));
    const isDna = [...seq].every((ch) => DNA_BASES.has(ch));
    if (isDna) {
      const shape = validateCdsShape(seq, false);
      if (shape.errors.length) throw new Error(tf("err_invalid_ref_cds", { detail: shape.errors.join("; ") }));
      const protein = translateDna(seq).replace(/\*+$/g, "");
      if (protein.includes("*")) throw new Error(t("err_ref_internal_stop"));
      return { name: record.name || "reference", source_type: "dna", original_dna: seq, target_protein: protein, warnings: shape.warnings };
    }
    const protein = normalizeProtein(seq).replace(/[\*_]+$/g, "");
    if (/[\*_]/.test(protein)) throw new Error(t("err_protein_internal_stop"));
    const bad = [...protein].filter((ch) => !PROTEIN_ALPHABET.has(ch));
    if (bad.length) throw new Error(tf("err_not_dna_or_protein", { chars: [...new Set(bad)].join(",") }));
    return { name: record.name || "target_protein", source_type: "protein", original_dna: null, target_protein: protein, warnings: [] };
  }''',
    "firstProteinMismatch": r'''function firstProteinMismatch(target, observed) {
    if (target.length !== observed.length) return tf("mismatch_len", { t: target.length, c: observed.length });
    for (let i = 0; i < target.length; i++) if (target[i] !== observed[i]) return tf("mismatch_pos", { i: i + 1, t: target[i], c: observed[i] });
    return t("mismatch_unknown");
  }''',
    "analyzeRecord": r'''function analyzeRecord(record, targetProtein, lookup, cfdThreshold) {
    const dna = normalizeSeq(record.sequence); const requireStop = record.group !== "reference";
    const shape = validateCdsShape(dna, requireStop); const errors = [...shape.errors]; const warnings = [...shape.warnings];
    let protein = "";
    if (!shape.hasInvalidBases && dna.length >= 3 && dna.length % 3 === 0) {
      protein = translateDna(dna).replace(/\*+$/g, "");
      if (protein.includes("X")) errors.push(t("err_unknown_codon"));
      if (protein !== targetProtein) errors.push(tf("err_protein_mismatch", { detail: firstProteinMismatch(targetProtein, protein) }));
    } else if (!errors.length) errors.push(t("err_must_be_dna"));
    let metrics = {};
    if (!invalidDnaChars(dna).length && dna.length > 0 && dna.length % 3 === 0) metrics = computeCoreMetrics(dna, lookup, cfdThreshold);
    const passed = errors.length === 0 && protein === targetProtein;
    return { name: record.name, source: record.source, group: record.group, dna, protein, passed,
      included: record.group === "external" && passed, is_local_reference: record.group === "local",
      note: record.note || "", errors, warnings, metrics };
  }''',
    "computeCoreMetrics": r'''function computeCoreMetrics(dna, lookup, cfdThreshold) {
    return { len_nt: dna.length, codon_count: splitCodons(dna).length, CSI: round(csi(dna, lookup), 5),
      "GC%": round(gcPercent(dna), 3), low_adapted_pct: round(cfdPercent(dna, lookup, cfdThreshold), 3),
      "GC3%": round(gcByPosition(dna, 3), 3) };
  }''',
    "generateLocalCandidates": r'''function generateLocalCandidates(targetProtein, table, lookup) {
    const specs = [
      { name: "local_highest_frequency", source: "local_hfc", seq: highestFrequencySequence(targetProtein, table), key: "local_note_hfc" },
      { name: "local_weighted_frequency", source: "local_weighted", seq: weightedFrequencySequence(targetProtein, table), key: "local_note_weighted" },
      { name: "local_balanced_gc_gc3", source: "local_balanced", seq: balancedSequence(targetProtein, table, lookup), key: "local_note_balanced" }
    ];
    return specs.map((s) => ({ name: s.name, source: s.source, group: "local", sequence: s.seq,
      note: s.key === "local_note_balanced" ? tf(s.key, { gc: ANIGER_CODING_GC, gc3: ANIGER_GC3 }) : t(s.key) }));
  }''',
    "sortExternalCandidates": r'''function sortExternalCandidates(analyses) {
    return analyses.filter((a) => a.group === "external" && a.included).sort((a, b) => {
      const csiDiff = (b.metrics.CSI ?? 0) - (a.metrics.CSI ?? 0);
      if (Math.abs(csiDiff) > 1e-12) return csiDiff;
      const cfdDiff = (a.metrics.low_adapted_pct ?? 100) - (b.metrics.low_adapted_pct ?? 100);
      if (Math.abs(cfdDiff) > 1e-12) return cfdDiff;
      const gcA = Math.abs((a.metrics["GC%"] ?? ANIGER_CODING_GC) - ANIGER_CODING_GC);
      const gcB = Math.abs((b.metrics["GC%"] ?? ANIGER_CODING_GC) - ANIGER_CODING_GC);
      if (Math.abs(gcA - gcB) > 1e-12) return gcA - gcB;
      return a.name.localeCompare(b.name);
    });
  }''',
    "statusLabel": r'''function statusLabel(a) {
    if (a.group === "reference") return `<span class="status-ref">${esc(t("status_ref"))}</span>`;
    if (a.group === "local") return a.passed ? `<span class="status-ref">${esc(t("status_local_ok"))}</span>` : `<span class="status-fail">${esc(t("status_local_bad"))}</span>`;
    return a.passed ? `<span class="status-pass">${esc(t("status_pass"))}</span>` : `<span class="status-fail">${esc(t("status_fail"))}</span>`;
  }''',
    "metricRow": r'''function metricRow(a, rank) {
    return { rank: rank || "", name: a.name, source: a.source, status: stripHtml(statusLabel(a)),
      included_in_ranking: a.included, is_local_reference: a.is_local_reference,
      len_nt: a.metrics.len_nt || "", codon_count: a.metrics.codon_count || "", CSI: a.metrics.CSI ?? "",
      "GC%": a.metrics["GC%"] ?? "", low_adapted_pct: a.metrics.low_adapted_pct ?? "",
      errors: a.errors.join("; "), warnings: a.warnings.join("; "), note: a.note || "" };
  }''',
    "displayMetricRow": r'''function displayMetricRow(a, rank) {
    return { rank: rank || "", name: a.name, source: a.source, status: statusLabel(a),
      len_nt: a.metrics.len_nt || "", codon_count: a.metrics.codon_count || "", CSI: a.metrics.CSI ?? "",
      "GC%": a.metrics["GC%"] ?? "", low_adapted_pct: a.metrics.low_adapted_pct ?? "",
      errors: a.errors.join("; "), warnings: a.warnings.join("; ") };
  }''',
    "renderHeatmap": r'''function renderHeatmap(analyses, comparisonRows, maxPos) {
    const orderedAnalyses = [...analyses.filter((a) => a.group === "reference"),
      ...analyses.filter((a) => a.group === "external" && a.passed), ...analyses.filter((a) => a.group === "local" && a.passed)];
    const names = orderedAnalyses.map((a) => a.name);
    if (!names.length) return `<p class="notice warn">${esc(t("no_heatmap"))}</p>`;
    const byPos = {}, aaByPos = {}, refByPos = {};
    for (const row of comparisonRows) {
      if (!names.includes(row.candidate)) continue;
      if (!byPos[row.position]) byPos[row.position] = {};
      byPos[row.position][row.candidate] = row; aaByPos[row.position] = row.amino_acid; refByPos[row.position] = row.reference_codon || "";
    }
    const positions = Object.keys(byPos).map(Number).sort((a, b) => a - b).slice(0, maxPos);
    const head = names.map((name) => `<th>${esc(name)}</th>`).join("");
    const body = positions.map((pos) => {
      const cells = [`<td class="pos">${pos}</td>`, `<td>${esc(aaByPos[pos])}</td>`, `<td>${esc(refByPos[pos])}</td>`];
      for (const name of names) {
        const row = byPos[pos] && byPos[pos][name];
        if (!row) { cells.push(`<td class="missing">-</td>`); continue; }
        let cls = row.same_as_reference ? "same" : "changed"; if (row.rare) cls = "rare"; if (!row.synonymous_with_target) cls = "bad";
        cells.push(`<td class="${cls}" title="${esc(`source=${row.source}; relative_adaptiveness=${row.relative_adaptiveness}`)}">${esc(row.codon)}</td>`);
      }
      return `<tr>${cells.join("")}</tr>`;
    }).join("");
    return `<div class="codon-wrap"><table class="codon-map"><thead><tr><th>${esc(t("heat_position"))}</th><th>${esc(t("heat_aa"))}</th><th>${esc(t("heat_original"))}</th>${head}</tr></thead><tbody>${body}</tbody></table></div>`;
  }''',
    "reportJson": r'''function reportJson(target, analyses, comparisonRows, cfdThreshold) {
    const ranked = sortExternalCandidates(analyses);
    return JSON.stringify({ host: { name: "Aspergillus niger", taxid: ANIGER_TAXID, genetic_code: GENETIC_CODE,
      kazusa_coding_gc_percent: ANIGER_CODING_GC, kazusa_gc3_percent: ANIGER_GC3 },
      scoring_note: t("json_scoring_note"), low_adapted_codon_threshold: cfdThreshold,
      target: { name: target.name, source_type: target.source_type, protein_length_aa: target.target_protein.length,
        original_dna_length_nt: target.original_dna ? target.original_dna.length : null, warnings: target.warnings },
      candidates: analyses.map((a) => metricRow(a, ranked.indexOf(a) >= 0 ? ranked.indexOf(a) + 1 : "")),
      comparison_row_count: comparisonRows.length, generated_by: "codon-project/docs/visualization/index.html" }, null, 2);
  }''',
    "renderLocalSection": r'''function renderLocalSection(localAnalyses) {
    if (!localAnalyses.length) return `<h2>${esc(t("h2_local"))}</h2><p class="hint">${esc(t("no_local"))}</p>`;
    const items = localAnalyses.map((a) => `<article class="local-item"><h3>${esc(a.name)}</h3><p class="hint">${esc(a.note)}</p>
      <div class="scroll" style="max-height:190px;">${tableHtmlLabeled([displayMetricRow(a, "")], true, METRIC_COL_LABEL)}</div>
      <pre class="sequence">${esc(wrapFasta(a.name, a.source, a.dna))}</pre></article>`).join("");
    return `<h2>${esc(t("h2_local"))}</h2><p class="hint">${esc(t("hint_local"))}</p><div class="local-list">${items}</div>`;
  }''',
    "renderMetrics": r'''function renderMetrics(target, analyses, comparisonRows, cfdThreshold) {
    const ranked = sortExternalCandidates(analyses);
    const externalFailed = analyses.filter((a) => a.group === "external" && !a.passed);
    const references = analyses.filter((a) => a.group === "reference");
    const locals = analyses.filter((a) => a.group === "local");
    const rankedRows = ranked.map((a, idx) => displayMetricRow(a, idx + 1));
    const failedRows = externalFailed.map((a) => displayMetricRow(a, ""));
    const referenceRows = references.map((a) => displayMetricRow(a, ""));
    document.getElementById("tabMetrics").innerHTML = `
      <div class="summary-grid">
        <div><span class="hint">${esc(t("summary_protein_len"))}</span><strong>${target.target_protein.length}</strong><span class="hint">${esc(t("unit_aa"))}</span></div>
        <div><span class="hint">${esc(t("summary_original_cds"))}</span><strong>${target.original_dna ? target.original_dna.length : esc(t("not_provided"))}</strong><span class="hint">${esc(t("unit_nt"))}</span></div>
        <div><span class="hint">${esc(t("summary_ext_pass"))}</span><strong>${ranked.length}</strong><span class="hint">${esc(t("unit_count"))}</span></div>
        <div><span class="hint">${esc(t("summary_ext_fail"))}</span><strong>${externalFailed.length}</strong><span class="hint">${esc(t("unit_count"))}</span></div>
      </div>
      <p class="notice">${tf("ranking_notice", { gc: ANIGER_CODING_GC })}</p>
      <details class="help"><summary>${esc(t("metrics_help_title"))}</summary>
        <p>${t("metrics_help_csi")}</p><p>${t("metrics_help_gc")}</p><p>${t("metrics_help_low")}</p>
        <p>${t("metrics_help_errors")}</p><p>${t("metrics_help_warnings")}</p><p>${t("metrics_help_status")}</p></details>
      <h2>${esc(t("h2_external_rank"))}</h2><p class="hint">${esc(t("hint_external_rank"))}</p>
      <div class="scroll">${rankedRows.length ? tableHtmlLabeled(rankedRows, true, METRIC_COL_LABEL) : `<p class="notice warn">${esc(t("no_external_pass"))}</p>`}</div>
      <h2>${esc(t("h2_reference"))}</h2>
      <div class="scroll">${referenceRows.length ? tableHtmlLabeled(referenceRows, true, METRIC_COL_LABEL) : `<p class="hint">${esc(t("hint_no_dna_baseline"))}</p>`}</div>
      ${failedRows.length ? `<h2>${esc(t("h2_external_fail"))}</h2><div class="scroll">${tableHtmlLabeled(failedRows, true, METRIC_COL_LABEL)}</div>` : ""}
      ${renderLocalSection(locals)}`;
    document.getElementById("tabCodons").innerHTML = `
      <h2>${esc(t("h2_codon_map"))}</h2><p class="notice">${esc(t("codon_map_notice"))}</p>
      <label for="codonThresholdSlider">${esc(t("label_threshold"))} <span id="codonThresholdVal">${cfdThreshold.toFixed(2)}</span></label>
      <input type="range" id="codonThresholdSlider" min="0.05" max="0.80" step="0.05" value="${cfdThreshold.toFixed(2)}" />
      <p class="hint">${esc(t("hint_slider"))}</p>
      <details class="help"><summary>${esc(t("threshold_help_title"))}</summary><p>${t("threshold_help_p1")}</p><p>${t("threshold_help_p2")}</p></details>
      <div class="legend">
        <span><i class="swatch same"></i>${esc(t("legend_same"))}</span>
        <span><i class="swatch changed"></i>${esc(t("legend_changed"))}</span>
        <span><i class="swatch rare"></i>${esc(tf("legend_rare", { t: cfdThreshold.toFixed(2) }))}</span>
        <span><i class="swatch bad"></i>${esc(t("legend_bad"))}</span></div>
      ${renderHeatmap(analyses, comparisonRows, 360)}`;
    document.getElementById("tabLong").innerHTML = `
      <h2>${esc(t("h2_long"))}</h2><p class="notice">${t("long_notice")}</p>
      <div class="scroll">${tableHtmlLabeled(comparisonRows.slice(0, 5000), false, DETAIL_COL_LABEL)}${comparisonRows.length > 5000 ? `<p class="notice warn">${esc(t("long_truncated"))}</p>` : ""}</div>`;
    installThresholdSlider();
  }''',
    "renderExports": r'''function renderExports(target, analyses, comparisonRows, cfdThreshold) {
    const ranked = sortExternalCandidates(analyses);
    const allMetrics = analyses.map((a) => metricRow(a, ranked.indexOf(a) >= 0 ? ranked.indexOf(a) + 1 : ""));
    document.getElementById("tabExport").innerHTML = `
      <h2>${esc(t("h2_export"))}</h2><p class="notice">${esc(t("export_notice"))}</p>
      <div class="download-row">
        <button type="button" id="dlMetrics">${esc(t("btn_metrics_csv"))}</button>
        <button type="button" disabled title="${esc(t("btn_future"))}">${esc(t("btn_detail_csv"))}</button>
        <button type="button" disabled title="${esc(t("btn_future"))}">${esc(t("btn_json"))}</button>
        <button type="button" disabled title="${esc(t("btn_future"))}">${esc(t("btn_fasta_ext"))}</button>
        <button type="button" disabled title="${esc(t("btn_future"))}">${esc(t("btn_fasta_local"))}</button>
      </div>`;
    document.getElementById("dlMetrics").onclick = () => downloadText("aniger_simple_metrics.csv", rowsToCsv(allMetrics), "text/csv");
  }''',
    "run": r'''function run() {
    document.getElementById("messages").innerHTML = "";
    const table = loadAnigerTable(); const lookup = codonLookup(table);
    const refMerged = document.getElementById("refText").value;
    const candMerged = document.getElementById("candText").value;
    let target;
    try { target = buildTarget(parseTextCandidates(refMerged, "reference")); }
    catch (err) { pushMessage("err", esc(err.message || err)); return; }
    const cdsPart = target.original_dna ? tf("msg_original_cds", { nt: target.original_dna.length }) : t("msg_target_protein_only");
    pushMessage("ok", esc(tf("msg_target_ok", { aa: target.target_protein.length, cds: cdsPart })));
    for (const warning of target.warnings) pushMessage("warn", esc(warning));
    const records = [];
    if (target.original_dna) records.push({ name: target.name || "original_reference", source: "original", group: "reference", sequence: target.original_dna });
    records.push(...parseTextCandidates(candMerged, "manual").map((r) => ({ ...r, group: "external" })));
    if (document.getElementById("chkLocal").checked) records.push(...generateLocalCandidates(target.target_protein, table, lookup));
    lastRunState = { target, uniqueRecords: makeUniqueRecords(records), table, lookup };
    renderFromState(currentLowAdaptedThreshold);
  }''',
}


def main() -> None:
    src = SOURCE.read_text(encoding="utf-8")
    src = src.replace('<html lang="zh-CN">', '<html lang="en">')
    src = src.replace("<title>黑曲霉密码子候选评审（简化版）</title>", "<title>A. niger codon candidate review (simple)</title>")
    src = src.replace("    code { font-family: var(--mono); font-size: 0.92em; }\n  </style>",
                      "    code { font-family: var(--mono); font-size: 0.92em; }" + HEADER_CSS + "\n  </style>")
    src = re.sub(r"<header>.*?</header>", HEADER_HTML, src, count=1, flags=re.DOTALL)
    src = re.sub(r"<aside>.*?</aside>", ASIDE_HTML, src, count=1, flags=re.DOTALL)
    src = re.sub(r'<div class="tabs">\s*<button type="button" class="tab active" data-tab="tabMetrics">.*?</div>',
                 TABS_HTML, src, count=1, flags=re.DOTALL)
    src = src.replace('"use strict";', '"use strict";' + I18N_BLOCK)
    src = re.sub(r"  const LOCAL_NOTES = \{.*?\};\n  const LOW_ADAPTED_LABEL = .*?;\n", "  /* LOCAL_NOTES via i18n */\n", src, count=1, flags=re.DOTALL)
    for name, body in FUNCTIONS.items():
        src = patch_function(src, name, body)
    src = src.replace('return `<p class="hint">（无数据）</p>`;', 'return `<p class="hint">${esc(t("no_data"))}</p>`;')
    src = src.replace('  document.getElementById("btnRun").addEventListener("click", () => {', INIT_BLOCK + '\n  document.getElementById("btnRun").addEventListener("click", () => {')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(src, encoding="utf-8")
    print(f"Wrote {OUT} ({len(src.splitlines())} lines)")


if __name__ == "__main__":
    main()

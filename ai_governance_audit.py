import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="AI Governance Audit Framework",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=Libre+Franklin:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Libre Franklin', sans-serif;
    background-color: #0c0f1a !important;
    color: #e8e4dc;
}
.main, .block-container {
    background-color: #0c0f1a !important;
}
[data-testid="stAppViewContainer"] { background-color: #0c0f1a !important; }
[data-testid="stHeader"] { background-color: #0c0f1a !important; }
h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
    color: #f0ece4 !important;
    letter-spacing: -0.3px;
}

[data-testid="stSidebar"] {
    background: #080b14 !important;
    border-right: 1px solid rgba(255,255,255,0.06);
}
[data-testid="stSidebar"] * { color: #c8c4bc !important; }
[data-testid="stSidebar"] input { background: #111624 !important; border-color: rgba(255,255,255,0.1) !important; color: #e8e4dc !important; }

.slabel {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #5a7fa8;
    margin-bottom: 4px;
    margin-top: 24px;
    display: block;
}

.hero {
    background: linear-gradient(135deg, #111828 0%, #0d1420 100%);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 20px;
    padding: 48px 44px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    width: 320px; height: 320px;
    border-radius: 50%;
    border: 1px solid rgba(90,127,168,0.08);
    top: -100px; right: -80px;
}
.hero-tag {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #5a7fa8;
    border: 1px solid rgba(90,127,168,0.25);
    background: rgba(90,127,168,0.08);
    padding: 4px 12px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 18px;
}
.hero h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: 2.4rem !important;
    font-weight: 800 !important;
    color: #f0ece4 !important;
    margin: 0 0 10px 0 !important;
    letter-spacing: -1.2px;
    line-height: 1.1;
}
.hero p {
    color: rgba(232,228,220,0.5);
    font-size: 0.92rem;
    margin: 0;
    line-height: 1.7;
    max-width: 640px;
}

.progress-bar-outer {
    background: rgba(255,255,255,0.05);
    border-radius: 99px;
    height: 4px;
    margin: 20px 0 8px;
    overflow: hidden;
}
.progress-bar-inner {
    height: 4px;
    border-radius: 99px;
    background: linear-gradient(90deg, #5a7fa8, #7eb8d4);
}
.step-counter {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 1px;
    color: rgba(232,228,220,0.35);
    margin-bottom: 24px;
}

.step-card {
    background: #111828;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 28px 28px 24px;
    margin-bottom: 20px;
}
.step-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #f0ece4;
    margin-bottom: 6px;
}
.step-card-desc {
    font-size: 0.83rem;
    color: rgba(232,228,220,0.45);
    line-height: 1.6;
    margin-bottom: 16px;
}

.q-item {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 6px;
}
.q-severity {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 2px 8px;
    border-radius: 3px;
    display: inline-block;
    margin-bottom: 6px;
}
.sev-critical { background: rgba(192,57,43,0.15); color: #e74c3c; border: 1px solid rgba(192,57,43,0.25); }
.sev-high     { background: rgba(211,84,0,0.15);  color: #e67e22; border: 1px solid rgba(211,84,0,0.25); }
.sev-medium   { background: rgba(183,149,11,0.15); color: #f1c40f; border: 1px solid rgba(183,149,11,0.25); }
.sev-low      { background: rgba(30,132,73,0.15);  color: #2ecc71; border: 1px solid rgba(30,132,73,0.25); }
.q-text { font-size: 0.88rem; color: rgba(232,228,220,0.8); line-height: 1.5; }

.stButton > button {
    background: #111828 !important;
    color: #e8e4dc !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.5px !important;
    padding: 10px 22px !important;
}
.stButton > button:hover {
    background: #1a2438 !important;
    border-color: rgba(90,127,168,0.4) !important;
    color: #f0ece4 !important;
}

.stRadio > div { gap: 6px !important; }
.stRadio label {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 8px !important;
    padding: 8px 14px !important;
    font-size: 0.83rem !important;
    color: rgba(232,228,220,0.7) !important;
    cursor: pointer !important;
}
.stRadio label:hover {
    background: rgba(90,127,168,0.1) !important;
    border-color: rgba(90,127,168,0.3) !important;
    color: #e8e4dc !important;
}

.score-hero {
    background: linear-gradient(135deg, #111828 0%, #0d1c2e 100%);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 36px 32px;
    text-align: center;
}
.score-num {
    font-family: 'Syne', sans-serif;
    font-size: 5rem;
    font-weight: 800;
    line-height: 1;
    margin: 10px 0 6px;
}
.score-lbl {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(232,228,220,0.35);
    margin-bottom: 6px;
}

.finding {
    border-left: 3px solid;
    padding: 14px 18px;
    margin-bottom: 8px;
    background: #111828;
    border-radius: 0 10px 10px 0;
    font-size: 0.87rem;
    line-height: 1.6;
    color: rgba(232,228,220,0.8);
}
.finding-lbl {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.rec {
    background: #111828;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 8px;
    font-size: 0.87rem;
    color: rgba(232,228,220,0.78);
    line-height: 1.65;
}
.rec-n {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    color: rgba(255,255,255,0.08);
    float: left;
    margin-right: 14px;
    line-height: 1;
}

.fw-tag {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 8px;
    border-radius: 4px;
    margin: 2px 3px 2px 0;
    background: rgba(90,127,168,0.1);
    color: #5a9fd4;
    border: 1px solid rgba(90,127,168,0.2);
}

.stTextInput input {
    background: #111828 !important;
    border-color: rgba(255,255,255,0.08) !important;
    color: #e8e4dc !important;
    border-radius: 8px !important;
}
.stDownloadButton button {
    background: #1e3a5f !important;
    color: #7eb8d4 !important;
    border: 1px solid rgba(90,127,168,0.35) !important;
    border-radius: 8px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
}
hr { border-color: rgba(255,255,255,0.06) !important; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# FRAMEWORK DATA
# ============================================================
DOMAINS = {
    "Transparency & Explainability": {
        "icon": "◎", "weight": 0.20,
        "description": "Can the system's decisions be explained to affected users and auditors? Are model inputs, outputs, and logic disclosed appropriately?",
        "frameworks": ["EU AI Act Art. 13", "NIST AI RMF – MAP", "ISO 42001 §8.4"],
        "questions": [
            ("Is documentation available explaining how the AI system makes decisions?", "high"),
            ("Can the system provide explanations for individual decisions to affected users?", "high"),
            ("Are training data sources, types, and collection methods disclosed?", "medium"),
            ("Is there a published model card describing capabilities and limitations?", "medium"),
            ("Are performance benchmarks and accuracy metrics available internally or publicly?", "low"),
        ]
    },
    "Fairness & Non-Discrimination": {
        "icon": "◑", "weight": 0.22,
        "description": "Does the system treat individuals and groups equitably? Has it been tested for bias across protected characteristics?",
        "frameworks": ["EU AI Act Art. 10", "NIST AI RMF – MEASURE", "OECD AI Principles"],
        "questions": [
            ("Has the system been tested for differential performance across demographic groups?", "critical"),
            ("Are there mechanisms to detect and correct discriminatory outputs?", "high"),
            ("Was training data audited for historical bias before use?", "high"),
            ("Does the system comply with anti-discrimination laws in its jurisdiction?", "critical"),
            ("Is there a formal fairness metric used to evaluate model outputs?", "medium"),
        ]
    },
    "Accountability & Oversight": {
        "icon": "◻", "weight": 0.22,
        "description": "Who is responsible when the AI system causes harm? Are there human review processes, escalation paths, and audit trails?",
        "frameworks": ["OSFI E-23 §4", "NIST AI RMF – GOVERN", "ISO 42001 §5.3", "EU AI Act Art. 17"],
        "questions": [
            ("Is there a named responsible party accountable for the system's outcomes?", "critical"),
            ("Are audit logs maintained of system decisions and interactions?", "high"),
            ("Is there a human-in-the-loop process for high-stakes decisions?", "high"),
            ("Is there a formal incident response process for AI-related harms?", "medium"),
            ("Has an external or third-party audit been conducted?", "medium"),
        ]
    },
    "Security & Robustness": {
        "icon": "◈", "weight": 0.18,
        "description": "Is the system resilient to adversarial inputs, data poisoning, and misuse? Are vulnerabilities regularly assessed?",
        "frameworks": ["NIST AI RMF – MANAGE", "ISO 42001 §8.5", "EU AI Act Art. 15"],
        "questions": [
            ("Has the system been tested against adversarial inputs and prompt injection?", "high"),
            ("Is there protection against data poisoning during model training?", "high"),
            ("Are access controls in place to prevent unauthorized model queries?", "medium"),
            ("Is there monitoring for model drift or performance degradation in production?", "medium"),
            ("Has a red-teaming or penetration testing exercise been conducted?", "low"),
        ]
    },
    "Privacy & Data Governance": {
        "icon": "◍", "weight": 0.18,
        "description": "Does the system comply with data protection laws? Is personal data handled, stored, and retained appropriately?",
        "frameworks": ["GDPR / PIPEDA / CCPA", "ISO 42001 §8.3", "OECD AI Principles", "OSFI E-23 §6"],
        "questions": [
            ("Does the system comply with applicable privacy laws (GDPR, PIPEDA, CCPA)?", "critical"),
            ("Is personal data minimized — only collected and retained as needed?", "high"),
            ("Are data subjects informed when AI is used to make decisions about them?", "high"),
            ("Is there a data retention and deletion policy in place?", "medium"),
            ("Are data sharing agreements reviewed before training data is acquired?", "medium"),
        ]
    }
}

RESPONSE_OPTS = ["Yes — fully in place", "Partially — in progress", "No — not addressed", "Not applicable"]
RISK_LEVELS   = {"Yes — fully in place": 1.0, "Partially — in progress": 0.5,
                 "No — not addressed": 0.0, "Not applicable": None}
STEPS = ["Welcome"] + list(DOMAINS.keys()) + ["Results"]


# ============================================================
# SESSION STATE
# ============================================================
for key, val in [("step", 0), ("responses", {}), ("meta", {})]:
    if key not in st.session_state:
        st.session_state[key] = val


# ============================================================
# HELPERS
# ============================================================
def domain_score(domain):
    resp   = st.session_state.responses.get(domain, {})
    scored = [RISK_LEVELS[v] for v in resp.values() if RISK_LEVELS.get(v) is not None]
    return (sum(scored) / len(scored) * 100) if scored else 0

def overall_score():
    scores = {d: domain_score(d) for d in DOMAINS}
    tw = sum(DOMAINS[d]["weight"] for d in scores)
    return sum(scores[d] * DOMAINS[d]["weight"] for d in scores) / tw if tw else 0

def rating(score):
    if score >= 80: return "Strong",     "#2ecc71"
    if score >= 60: return "Adequate",   "#f1c40f"
    if score >= 40: return "Needs Work", "#e67e22"
    return           "High Risk",        "#e74c3c"

def sev_color(sev):
    return {"critical": "#e74c3c", "high": "#e67e22", "medium": "#f1c40f", "low": "#2ecc71"}.get(sev, "#888")

def get_findings():
    downgrade = {"critical": "high", "high": "medium", "medium": "low", "low": "low"}
    sev_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    findings  = []
    for domain, dd in DOMAINS.items():
        resp = st.session_state.responses.get(domain, {})
        for i, (q, sev) in enumerate(dd["questions"]):
            r = resp.get(f"{domain}_{i}", "Not applicable")
            if r == "No — not addressed":
                findings.append({"domain": domain, "q": q, "sev": sev, "status": "Gap — not addressed"})
            elif r == "Partially — in progress":
                findings.append({"domain": domain, "q": q, "sev": downgrade[sev], "status": "Partially addressed"})
    findings.sort(key=lambda x: sev_order[x["sev"]])
    return findings

def radar_chart(d_sc):
    cats   = list(d_sc.keys())
    labels = [d.split("&")[0].strip() for d in cats]
    vals   = [d_sc[d] for d in cats]
    fig = go.Figure(go.Scatterpolar(
        r=vals + [vals[0]], theta=labels + [labels[0]],
        fill='toself', fillcolor='rgba(90,127,168,0.12)',
        line=dict(color='#5a9fd4', width=2),
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0,100],
                tickfont=dict(size=9, family='DM Mono', color='rgba(232,228,220,0.3)'),
                gridcolor='rgba(255,255,255,0.06)', linecolor='rgba(255,255,255,0.06)'),
            angularaxis=dict(
                tickfont=dict(size=10, family='Libre Franklin', color='rgba(232,228,220,0.6)'),
                gridcolor='rgba(255,255,255,0.06)', linecolor='rgba(255,255,255,0.06)')
        ),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False, margin=dict(l=40,r=40,t=40,b=40), height=320
    )
    return fig

def bar_chart(d_sc):
    cats   = list(d_sc.keys())
    labels = [d.split("&")[0].strip() for d in cats]
    vals   = [d_sc[d] for d in cats]
    colors = [rating(v)[1] for v in vals]
    fig = go.Figure(go.Bar(
        x=labels, y=vals, marker_color=colors, marker_line_width=0,
        text=[f"{v:.0f}" for v in vals], textposition='outside',
        textfont=dict(family='DM Mono', size=11, color='rgba(232,228,220,0.5)')
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(range=[0,118], showgrid=True, gridcolor='rgba(255,255,255,0.05)',
                   tickfont=dict(family='DM Mono', size=9, color='rgba(232,228,220,0.3)')),
        xaxis=dict(tickfont=dict(family='Libre Franklin', size=10, color='rgba(232,228,220,0.55)')),
        margin=dict(l=10,r=10,t=24,b=10), height=280, showlegend=False
    )
    return fig

def generate_report():
    sc  = overall_score()
    rat = rating(sc)[0]
    fnd = get_findings()
    d_sc = {d: domain_score(d) for d in DOMAINS}
    meta = st.session_state.meta
    lines = [
        "="*68, "AI GOVERNANCE AUDIT REPORT", "="*68,
        f"System        : {meta.get('system','—')}",
        f"Use Case      : {meta.get('usecase','—')}",
        f"Sector        : {meta.get('sector','—')}",
        f"Deployment    : {meta.get('stage','—')}",
        f"Assessed by   : {meta.get('assessor','—')}",
        f"Date          : {datetime.today().strftime('%B %d, %Y')}",
        f"Framework     : EU AI Act · NIST AI RMF 1.0 · ISO 42001 · OSFI E-23",
        "", "-"*68, "OVERALL SCORE", "-"*68,
        f"  {sc:.1f} / 100   —   {rat}", "",
        "-"*68, "DOMAIN SCORES", "-"*68,
    ]
    for d, s in d_sc.items():
        lines.append(f"  {d:<40} {s:>5.1f}   {rating(s)[0]}")
    lines += ["", "-"*68, f"FINDINGS  ({len(fnd)} total)", "-"*68]
    for i, f in enumerate(fnd, 1):
        lines += [f"  [{f['sev'].upper()}] {f['domain']}",
                  f"  {i}. {f['q']}", f"     Status: {f['status']}", ""]
    lines += ["-"*68, "END OF REPORT", "="*68]
    return "\n".join(lines)


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown('<span class="slabel">System Under Review</span>', unsafe_allow_html=True)
    st.session_state.meta["system"]   = st.text_input("AI System Name", value=st.session_state.meta.get("system",""), placeholder="e.g. LoanDecisionAI v2.1")
    st.session_state.meta["usecase"]  = st.text_input("Use Case", value=st.session_state.meta.get("usecase",""), placeholder="e.g. Credit scoring")
    st.session_state.meta["sector"]   = st.selectbox("Sector", ["Financial Services","Healthcare","Public Sector","HR","Education","Legal","Retail","Insurance","Other"])
    st.session_state.meta["stage"]    = st.selectbox("Deployment Stage", ["Pre-deployment","Pilot / limited rollout","Full production","Under review / suspended"])
    st.session_state.meta["assessor"] = st.text_input("Assessor", value=st.session_state.meta.get("assessor",""), placeholder="Your name")

    st.markdown("---")
    st.markdown('<span class="slabel">Framework Alignment</span>', unsafe_allow_html=True)
    st.markdown('<span class="fw-tag">EU AI Act</span><span class="fw-tag">NIST AI RMF</span><span class="fw-tag">ISO 42001</span><span class="fw-tag">OSFI E-23</span><span class="fw-tag">OECD 2025</span>', unsafe_allow_html=True)

    st.markdown("---")
    cur = st.session_state.step
    pct = int((cur / (len(STEPS) - 1)) * 100) if len(STEPS) > 1 else 0
    st.markdown(f'<span class="slabel">Progress — {pct}%</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="progress-bar-outer"><div class="progress-bar-inner" style="width:{pct}%;"></div></div>', unsafe_allow_html=True)
    for i, s in enumerate(STEPS):
        c = "#5a9fd4" if i == cur else ("#2ecc71" if i < cur else "rgba(232,228,220,0.2)")
        prefix = "▶ " if i == cur else ("✓ " if i < cur else "○ ")
        st.markdown(f'<p style="font-family:\'DM Mono\',monospace;font-size:0.65rem;color:{c};letter-spacing:1px;margin:3px 0;">{prefix}{s}</p>', unsafe_allow_html=True)


# ============================================================
# STEP 0 — WELCOME
# ============================================================
step = st.session_state.step

if step == 0:
    st.markdown("""
    <div class="hero">
        <div class="hero-tag">⚖ AI Governance · Risk Assessment</div>
        <h1>AI Governance<br>Audit Framework</h1>
        <p>Evaluate an AI system against structured governance criteria drawn from the EU AI Act, NIST AI Risk Management Framework, ISO 42001, and OSFI E-23. Identify gaps, assess risk exposure, and generate a findings report.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    for col, icon, title, desc in [
        (c1, "◎", "5 Governance Domains", "Transparency, Fairness, Accountability, Security, Privacy"),
        (c2, "◈", "25 Structured Questions", "Severity-tagged, drawn from real regulatory frameworks"),
        (c3, "◻", "Scored Risk Report", "Weighted score, radar chart, findings, and downloadable report"),
    ]:
        col.markdown(f"""
        <div style="background:#111828;border:1px solid rgba(255,255,255,0.06);border-radius:14px;padding:22px 20px;">
            <div style="font-size:1.3rem;color:#5a7fa8;margin-bottom:10px;">{icon}</div>
            <div style="font-family:'Syne',sans-serif;font-size:0.95rem;font-weight:700;color:#f0ece4;margin-bottom:6px;">{title}</div>
            <div style="font-size:0.78rem;color:rgba(232,228,220,0.4);line-height:1.6;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<span class="slabel">How to Use</span>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#111828;border:1px solid rgba(255,255,255,0.06);border-radius:14px;padding:22px 24px;font-size:0.87rem;color:rgba(232,228,220,0.6);line-height:1.9;">
    Fill in the system details in the left sidebar, then work through 5 governance domains one at a time.<br><br>
    For each question select the response that best reflects the <i>current state</i> of the system:<br>
    &nbsp;&nbsp;<b style="color:#2ecc71;">Yes — fully in place</b> &nbsp;· A formal process or control exists and is operational<br>
    &nbsp;&nbsp;<b style="color:#f1c40f;">Partially — in progress</b> &nbsp;· Work has begun but is incomplete or inconsistent<br>
    &nbsp;&nbsp;<b style="color:#e74c3c;">No — not addressed</b> &nbsp;· No action has been taken<br>
    &nbsp;&nbsp;<b style="color:rgba(232,228,220,0.35);">Not applicable</b> &nbsp;· Genuinely irrelevant to this system (use sparingly)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _, cb, _ = st.columns([2, 1, 2])
    with cb:
        if st.button("Begin Assessment →", use_container_width=True):
            st.session_state.step = 1
            st.rerun()


# ============================================================
# STEPS 1–5 — DOMAIN QUESTIONS
# ============================================================
elif 1 <= step <= 5:
    domain_list = list(DOMAINS.keys())
    domain      = domain_list[step - 1]
    dd          = DOMAINS[domain]
    pct         = int((step / (len(STEPS) - 1)) * 100)

    st.markdown(f"""
    <div class="progress-bar-outer"><div class="progress-bar-inner" style="width:{pct}%;"></div></div>
    <div class="step-counter">Domain {step} of 5 &nbsp;·&nbsp; {domain}</div>
    """, unsafe_allow_html=True)

    fw_tags = "".join(f'<span class="fw-tag">{f}</span>' for f in dd["frameworks"])
    st.markdown(f"""
    <div class="step-card">
        <div style="font-family:'DM Mono',monospace;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;color:#5a7fa8;margin-bottom:8px;">{dd['icon']} &nbsp; Domain {step} of 5</div>
        <div class="step-card-title">{domain}</div>
        <div class="step-card-desc">{dd['description']}</div>
        <div>{fw_tags}</div>
    </div>
    """, unsafe_allow_html=True)

    if domain not in st.session_state.responses:
        st.session_state.responses[domain] = {}

    for i, (q, sev) in enumerate(dd["questions"]):
        key     = f"{domain}_{i}"
        cur_val = st.session_state.responses[domain].get(key, "Not applicable")
        idx     = RESPONSE_OPTS.index(cur_val) if cur_val in RESPONSE_OPTS else 3

        st.markdown(f"""
        <div class="q-item">
            <div class="q-severity sev-{sev}">{sev}</div>
            <div class="q-text">{q}</div>
        </div>
        """, unsafe_allow_html=True)

        resp = st.radio("", RESPONSE_OPTS, index=idx, horizontal=True,
                        key=f"radio_{key}", label_visibility="collapsed")
        st.session_state.responses[domain][key] = resp
        st.markdown("<div style='margin-bottom:6px;'></div>", unsafe_allow_html=True)

    sc  = domain_score(domain)
    rat, col = rating(sc)
    st.markdown(f"""
    <div style="background:#111828;border:1px solid rgba(255,255,255,0.06);border-radius:10px;
                padding:14px 20px;margin-top:16px;display:flex;align-items:center;gap:16px;">
        <div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:{col};">{sc:.0f}</div>
        <div>
            <div style="font-family:'DM Mono',monospace;font-size:0.6rem;letter-spacing:2px;text-transform:uppercase;color:rgba(232,228,220,0.3);">Domain Score</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.72rem;color:{col};">{rat}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    nl, _, nr = st.columns([1, 2, 1])
    with nl:
        if st.button("← Back", use_container_width=True):
            st.session_state.step -= 1
            st.rerun()
    with nr:
        label = "View Results →" if step == 5 else "Next Domain →"
        if st.button(label, use_container_width=True):
            st.session_state.step += 1
            st.rerun()


# ============================================================
# STEP 6 — RESULTS
# ============================================================
elif step == 6:
    sc       = overall_score()
    rat, col = rating(sc)
    d_scores = {d: domain_score(d) for d in DOMAINS}
    findings = get_findings()
    crit     = sum(1 for f in findings if f["sev"] == "critical")
    high     = sum(1 for f in findings if f["sev"] == "high")
    med      = sum(1 for f in findings if f["sev"] == "medium")

    st.markdown('<span class="slabel">Results</span>', unsafe_allow_html=True)
    st.markdown("## Assessment Results")
    st.markdown("<br>", unsafe_allow_html=True)

    cs, cr, cb2 = st.columns([1, 1.3, 1.3])

    with cs:
        st.markdown(f"""
        <div class="score-hero">
            <div class="score-lbl">Overall Score</div>
            <div class="score-num" style="color:{col};">{sc:.0f}</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.7rem;letter-spacing:1.5px;text-transform:uppercase;color:{col};margin-bottom:24px;">{rat}</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.6rem;letter-spacing:2px;color:rgba(232,228,220,0.3);text-transform:uppercase;margin-bottom:12px;">Findings</div>
            <div style="font-size:0.85rem;line-height:2.2;text-align:left;padding-left:12px;">
                <span style="color:#e74c3c;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.75rem;color:rgba(232,228,220,0.6);">{crit} Critical</span><br>
                <span style="color:#e67e22;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.75rem;color:rgba(232,228,220,0.6);">{high} High</span><br>
                <span style="color:#f1c40f;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.75rem;color:rgba(232,228,220,0.6);">{med} Medium</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with cr:
        st.markdown('<span class="slabel">Coverage Radar</span>', unsafe_allow_html=True)
        st.plotly_chart(radar_chart(d_scores), use_container_width=True)

    with cb2:
        st.markdown('<span class="slabel">Domain Scores</span>', unsafe_allow_html=True)
        st.plotly_chart(bar_chart(d_scores), use_container_width=True)

    st.markdown("---")
    st.markdown('<span class="slabel">Findings</span>', unsafe_allow_html=True)
    st.markdown(f"### {len(findings)} Finding{'s' if len(findings)!=1 else ''} Identified")

    if not findings:
        st.success("No gaps identified — all assessed criteria are fully in place.")
    else:
        for f in findings:
            c = sev_color(f["sev"])
            st.markdown(f"""
            <div class="finding" style="border-left-color:{c};">
                <div class="finding-lbl" style="color:{c};">{f['sev'].upper()} · {f['domain']} · {f['status']}</div>
                {f['q']}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<span class="slabel">Recommendations</span>', unsafe_allow_html=True)
    st.markdown("### Recommended Actions")

    rec_map = {
        "Transparency & Explainability": "Develop and publish a model card documenting capabilities, limitations, training data sources, and performance benchmarks. This is a baseline expectation under EU AI Act Art. 13 and NIST AI RMF.",
        "Fairness & Non-Discrimination": "Commission a formal bias audit across protected demographic characteristics. Establish a fairness metric (e.g. equalized odds, demographic parity) and define an acceptable disparity threshold before deployment.",
        "Accountability & Oversight": "Assign a named AI system owner accountable for outcomes. Implement human-in-the-loop review for high-stakes decisions and establish an incident response playbook for AI-related harms (OSFI E-23 §4).",
        "Security & Robustness": "Conduct adversarial testing and red-teaming before deployment. Implement production monitoring for model drift with alerting thresholds defined by the system owner (ISO 42001 §8.5).",
        "Privacy & Data Governance": "Conduct a Privacy Impact Assessment and map all personal data flows. Ensure data subject notification obligations are met and a deletion mechanism exists (GDPR Art. 17 / PIPEDA).",
    }

    shown = set()
    recs  = []
    for f in findings:
        if f["sev"] in ("critical","high") and f["domain"] not in shown:
            shown.add(f["domain"])
            recs.append(rec_map[f["domain"]])
    if len(findings) > 8:
        recs.append("Given the volume of open findings, consider a phased rollout with staged governance reviews. Pausing deployment in high-risk contexts until critical gaps are resolved is recommended.")
    if crit > 0:
        recs.append("Critical findings must be resolved before the system is considered fit for deployment. Escalate to senior leadership and consider engaging an external AI governance advisor.")

    if not recs:
        st.success("No priority recommendations. Schedule a re-assessment in 6 months.")
    else:
        for i, r in enumerate(recs, 1):
            st.markdown(f'<div class="rec"><span class="rec-n">{i:02d}</span>{r}<div style="clear:both;"></div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<span class="slabel">Export</span>', unsafe_allow_html=True)
    st.markdown("### Download Audit Report")

    meta  = st.session_state.meta
    fname = f"ai_audit_{(meta.get('system') or 'system').lower().replace(' ','_')}_{datetime.today().strftime('%Y%m%d')}.txt"

    cd, ci, cr2 = st.columns([1, 2, 1])
    with cd:
        st.download_button("⬇  Download Report (.txt)", data=generate_report().encode("utf-8"),
                           file_name=fname, mime="text/plain", use_container_width=True)
    with ci:
        st.markdown(f"""
        <p style="font-size:0.77rem;color:rgba(232,228,220,0.35);line-height:1.9;margin-top:6px;">
        System: <b style="color:rgba(232,228,220,0.6);">{meta.get('system','—')}</b><br>
        Date: <b style="color:rgba(232,228,220,0.6);">{datetime.today().strftime('%B %d, %Y')}</b><br>
        Framework: EU AI Act · NIST AI RMF · ISO 42001 · OSFI E-23
        </p>
        """, unsafe_allow_html=True)
    with cr2:
        if st.button("↺  Start Over", use_container_width=True):
            st.session_state.step = 0
            st.session_state.responses = {}
            st.rerun()

    st.markdown("""
    <p style="font-size:0.72rem;color:rgba(232,228,220,0.2);text-align:center;font-family:'DM Mono',monospace;letter-spacing:0.5px;padding:20px 0 8px;">
    Built by Khushi Rana &nbsp;·&nbsp; AI Governance Audit Framework &nbsp;·&nbsp; For educational and portfolio purposes
    </p>
    """, unsafe_allow_html=True)

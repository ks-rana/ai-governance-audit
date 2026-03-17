import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import math

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AI Governance Audit Framework",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# STYLING
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700;900&family=DM+Mono:wght@300;400;500&family=Libre+Franklin:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Libre Franklin', sans-serif;
    background-color: #f7f5f0;
    color: #1a1a1a;
}

.main {
    background-color: #f7f5f0;
}

h1, h2, h3 {
    font-family: 'Fraunces', serif !important;
    letter-spacing: -0.5px;
    color: #111;
}

/* Top banner */
.audit-header {
    background: #111;
    color: #f7f5f0;
    padding: 36px 40px 28px;
    border-radius: 16px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}
.audit-header::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    border: 1px solid rgba(247,245,240,0.08);
    border-radius: 50%;
}
.audit-header::after {
    content: '';
    position: absolute;
    top: -20px; right: -20px;
    width: 120px; height: 120px;
    border: 1px solid rgba(247,245,240,0.05);
    border-radius: 50%;
}
.audit-header h1 {
    font-family: 'Fraunces', serif !important;
    font-size: 2.1rem;
    font-weight: 900;
    color: #f7f5f0 !important;
    margin: 0 0 6px 0;
    letter-spacing: -1px;
}
.audit-header p {
    color: rgba(247,245,240,0.55);
    font-size: 0.88rem;
    margin: 0;
    letter-spacing: 0.3px;
    font-family: 'Libre Franklin', sans-serif;
}
.audit-tag {
    display: inline-block;
    background: rgba(247,245,240,0.08);
    border: 1px solid rgba(247,245,240,0.15);
    color: rgba(247,245,240,0.7);
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 14px;
}

/* Section label */
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 6px;
    margin-top: 32px;
}

/* Domain card */
.domain-card {
    background: white;
    border: 1px solid #e8e4dc;
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 12px;
}
.domain-title {
    font-family: 'Fraunces', serif;
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 4px;
    color: #111;
}
.domain-desc {
    font-size: 0.8rem;
    color: #777;
    margin-bottom: 0;
    line-height: 1.5;
}

/* Risk pill */
.pill {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 20px;
    margin-left: 8px;
}
.pill-critical { background: #fde8e8; color: #c0392b; border: 1px solid #f5c6c6; }
.pill-high     { background: #fef3e2; color: #d35400; border: 1px solid #fad7a0; }
.pill-medium   { background: #fefde7; color: #b7950b; border: 1px solid #f7dc6f; }
.pill-low      { background: #e8f8f0; color: #1e8449; border: 1px solid #a9dfbf; }

/* Score card */
.score-card {
    background: #111;
    color: #f7f5f0;
    border-radius: 16px;
    padding: 28px 24px;
    text-align: center;
}
.score-number {
    font-family: 'Fraunces', serif;
    font-size: 4rem;
    font-weight: 900;
    line-height: 1;
    margin: 8px 0;
}
.score-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(247,245,240,0.45);
}

/* Finding card */
.finding {
    border-left: 3px solid #ccc;
    padding: 12px 16px;
    margin-bottom: 8px;
    background: white;
    border-radius: 0 8px 8px 0;
    font-size: 0.88rem;
    line-height: 1.6;
    color: #333;
}
.finding.critical { border-left-color: #c0392b; }
.finding.high     { border-left-color: #d35400; }
.finding.medium   { border-left-color: #b7950b; }
.finding.low      { border-left-color: #1e8449; }
.finding-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.finding-label.critical { color: #c0392b; }
.finding-label.high     { color: #d35400; }
.finding-label.medium   { color: #b7950b; }
.finding-label.low      { color: #1e8449; }

/* Recommendation card */
.rec-card {
    background: white;
    border: 1px solid #e8e4dc;
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 8px;
    font-size: 0.87rem;
    color: #333;
    line-height: 1.6;
}
.rec-number {
    font-family: 'Fraunces', serif;
    font-size: 1.4rem;
    font-weight: 900;
    color: #ddd;
    float: left;
    margin-right: 12px;
    line-height: 1;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #fff !important;
    border-right: 1px solid #e8e4dc;
}

/* Inputs */
.stSelectbox label, .stTextInput label, .stRadio label {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    color: #888 !important;
}

/* Slider */
.stSlider label {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.68rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    color: #666 !important;
}

hr { border-color: #e8e4dc !important; }

/* Expander */
.streamlit-expanderHeader {
    font-family: 'Libre Franklin', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    color: #111 !important;
}

/* Download button */
.stDownloadButton button {
    background: #111 !important;
    color: #f7f5f0 !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.5px !important;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# FRAMEWORK DEFINITION
# Five domains drawn from EU AI Act, NIST AI RMF, and ISO 42001
# ============================================================
DOMAINS = {
    "Transparency & Explainability": {
        "icon": "◎",
        "description": "Can the AI system's decisions be explained to affected users and auditors? Are model inputs, outputs, and logic disclosed appropriately?",
        "weight": 0.20,
        "questions": [
            ("Is documentation available explaining how the AI system makes decisions?", "high"),
            ("Can the system provide explanations for individual decisions to affected users?", "high"),
            ("Are the training data sources, data types, and collection methods disclosed?", "medium"),
            ("Is there a published model card or system card describing capabilities and limitations?", "medium"),
            ("Are performance benchmarks and accuracy metrics publicly available?", "low"),
        ]
    },
    "Fairness & Non-Discrimination": {
        "icon": "◑",
        "description": "Does the AI system treat individuals and groups equitably? Has it been tested for bias across protected characteristics?",
        "weight": 0.22,
        "questions": [
            ("Has the system been tested for differential performance across demographic groups?", "critical"),
            ("Are there mechanisms to detect and correct discriminatory outputs?", "high"),
            ("Was training data audited for historical bias before use?", "high"),
            ("Does the system comply with anti-discrimination laws in its deployment jurisdiction?", "critical"),
            ("Is there a formal fairness metric used to evaluate model outputs?", "medium"),
        ]
    },
    "Accountability & Oversight": {
        "icon": "◻",
        "description": "Who is responsible when the AI system causes harm? Are there human review processes, escalation paths, and audit trails?",
        "weight": 0.22,
        "questions": [
            ("Is there a named responsible party (person or team) accountable for the system's outcomes?", "critical"),
            ("Are audit logs maintained of system decisions and interactions?", "high"),
            ("Is there a human-in-the-loop process for high-stakes decisions?", "high"),
            ("Is there a formal incident response process for AI-related harms?", "medium"),
            ("Has an external or third-party audit been conducted?", "medium"),
        ]
    },
    "Security & Robustness": {
        "icon": "◈",
        "description": "Is the AI system resilient to adversarial inputs, data poisoning, and misuse? Are security vulnerabilities regularly assessed?",
        "weight": 0.18,
        "questions": [
            ("Has the system been tested against adversarial inputs and prompt injection?", "high"),
            ("Is there protection against data poisoning during model training?", "high"),
            ("Are access controls in place to prevent unauthorized model queries?", "medium"),
            ("Is there monitoring for model drift or performance degradation in production?", "medium"),
            ("Has a red-teaming or penetration testing exercise been conducted?", "low"),
        ]
    },
    "Privacy & Data Governance": {
        "icon": "◍",
        "description": "Does the system comply with data protection laws? Is personal data handled, stored, and retained appropriately?",
        "weight": 0.18,
        "questions": [
            ("Does the system comply with applicable privacy laws (e.g. GDPR, PIPEDA, CCPA)?", "critical"),
            ("Is personal data minimized — only collected and retained as needed?", "high"),
            ("Are data subjects informed when AI is used to make decisions about them?", "high"),
            ("Is there a data retention and deletion policy in place?", "medium"),
            ("Are data sharing agreements reviewed before training data is acquired?", "medium"),
        ]
    }
}

RISK_LEVELS = {
    "Yes — fully in place": 1.0,
    "Partially — in progress": 0.5,
    "No — not addressed": 0.0,
    "Not applicable": None
}

RISK_COLOR = {
    "critical": "#c0392b",
    "high": "#d35400",
    "medium": "#b7950b",
    "low": "#1e8449"
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================
def compute_domain_score(responses: dict, questions: list) -> float:
    scored = [RISK_LEVELS[r] for r in responses.values() if RISK_LEVELS[r] is not None]
    return (sum(scored) / len(scored) * 100) if scored else 0


def compute_overall_score(domain_scores: dict) -> float:
    total_weight = sum(DOMAINS[d]["weight"] for d in domain_scores)
    weighted = sum(domain_scores[d] * DOMAINS[d]["weight"] for d in domain_scores)
    return weighted / total_weight if total_weight else 0


def score_to_rating(score: float) -> tuple:
    if score >= 80:
        return "Strong", "low", "#1e8449"
    elif score >= 60:
        return "Adequate", "medium", "#b7950b"
    elif score >= 40:
        return "Needs Improvement", "high", "#d35400"
    else:
        return "High Risk", "critical", "#c0392b"


def generate_findings(all_responses: dict, system_name: str) -> list:
    findings = []
    for domain, domain_data in DOMAINS.items():
        responses = all_responses.get(domain, {})
        for i, (question, severity) in enumerate(domain_data["questions"]):
            key = f"{domain}_{i}"
            response = responses.get(key, "Not applicable")
            if response == "No — not addressed":
                findings.append({
                    "domain": domain,
                    "question": question,
                    "severity": severity,
                    "status": "Gap identified"
                })
            elif response == "Partially — in progress":
                # Downgrade severity for partial
                downgraded = {"critical": "high", "high": "medium", "medium": "low", "low": "low"}
                findings.append({
                    "domain": domain,
                    "question": question,
                    "severity": downgraded[severity],
                    "status": "Partially addressed"
                })
    # Sort by severity
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    findings.sort(key=lambda x: order[x["severity"]])
    return findings


def generate_recommendations(findings: list) -> list:
    recs = []
    seen_domains = set()
    for f in findings:
        if f["severity"] in ("critical", "high") and f["domain"] not in seen_domains:
            seen_domains.add(f["domain"])
            domain_data = DOMAINS[f["domain"]]
            if f["domain"] == "Transparency & Explainability":
                recs.append("Develop and publish a model card documenting system capabilities, limitations, training data sources, and performance benchmarks. This is a baseline expectation under the EU AI Act and NIST AI RMF.")
            elif f["domain"] == "Fairness & Non-Discrimination":
                recs.append("Commission a formal bias audit across protected demographic characteristics before or immediately after deployment. Establish a fairness metric (e.g. equalized odds, demographic parity) and set a threshold for acceptable disparity.")
            elif f["domain"] == "Accountability & Oversight":
                recs.append("Assign a named AI system owner accountable for outcomes and implement human-in-the-loop review for high-stakes decisions. Establish an incident response playbook specific to AI-related harms.")
            elif f["domain"] == "Security & Robustness":
                recs.append("Conduct adversarial testing and red-teaming before deployment. Implement production monitoring for model drift and anomalous outputs, with alerting thresholds defined by the system owner.")
            elif f["domain"] == "Privacy & Data Governance":
                recs.append("Conduct a Privacy Impact Assessment (PIA) and map all personal data flows through the system. Ensure data subject notification obligations are met and a deletion mechanism is in place.")
    # Add general recs
    if len(findings) > 10:
        recs.append("Given the volume of open findings, consider pausing deployment or limiting scope until critical and high severity gaps are resolved. A phased rollout with staged governance reviews is recommended.")
    if any(f["severity"] == "critical" for f in findings):
        recs.append("Critical findings must be resolved before the system is considered fit for deployment in high-risk contexts. Escalate to senior leadership and consider engaging an external AI governance advisor.")
    return recs


def build_radar_chart(domain_scores: dict) -> go.Figure:
    categories = list(domain_scores.keys())
    # Shorten labels for radar
    short_labels = [d.split("&")[0].strip() for d in categories]
    values = [domain_scores[d] for d in categories]
    values_closed = values + [values[0]]
    short_labels_closed = short_labels + [short_labels[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=short_labels_closed,
        fill='toself',
        fillcolor='rgba(17,17,17,0.08)',
        line=dict(color='#111', width=2),
        name='Score'
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(247,245,240,0)',
            radialaxis=dict(
                visible=True, range=[0, 100],
                tickfont=dict(size=9, family='DM Mono', color='#aaa'),
                gridcolor='#e8e4dc',
                linecolor='#e8e4dc'
            ),
            angularaxis=dict(
                tickfont=dict(size=10, family='Libre Franklin', color='#444'),
                gridcolor='#e8e4dc',
                linecolor='#e8e4dc'
            )
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=40),
        height=340
    )
    return fig


def build_bar_chart(domain_scores: dict) -> go.Figure:
    domains = list(domain_scores.keys())
    short = [d.split("&")[0].strip() for d in domains]
    scores = [domain_scores[d] for d in domains]
    colors = [score_to_rating(s)[2] for s in scores]

    fig = go.Figure(go.Bar(
        x=short, y=scores,
        marker_color=colors,
        marker_line_width=0,
        text=[f"{s:.0f}" for s in scores],
        textposition='outside',
        textfont=dict(family='DM Mono', size=11, color='#444')
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(range=[0, 115], showgrid=True, gridcolor='#e8e4dc',
                   tickfont=dict(family='DM Mono', size=9, color='#aaa'),
                   title='Score (0–100)'),
        xaxis=dict(tickfont=dict(family='Libre Franklin', size=10, color='#444')),
        margin=dict(l=10, r=10, t=20, b=10),
        height=300,
        showlegend=False
    )
    return fig


def generate_report_text(system_name, use_case, sector, overall_score, rating,
                         domain_scores, findings, recommendations, assessor) -> str:
    date = datetime.today().strftime("%B %d, %Y")
    lines = []
    lines.append("=" * 70)
    lines.append("AI GOVERNANCE AUDIT REPORT")
    lines.append("=" * 70)
    lines.append(f"System Name   : {system_name}")
    lines.append(f"Use Case      : {use_case}")
    lines.append(f"Sector        : {sector}")
    lines.append(f"Assessed by   : {assessor}")
    lines.append(f"Date          : {date}")
    lines.append(f"Framework     : EU AI Act · NIST AI RMF · ISO 42001")
    lines.append("")
    lines.append("-" * 70)
    lines.append("OVERALL SCORE")
    lines.append("-" * 70)
    lines.append(f"  {overall_score:.1f} / 100   —   {rating}")
    lines.append("")
    lines.append("-" * 70)
    lines.append("DOMAIN SCORES")
    lines.append("-" * 70)
    for domain, score in domain_scores.items():
        r, _, _ = score_to_rating(score)
        lines.append(f"  {domain:<38} {score:>5.1f}   {r}")
    lines.append("")
    lines.append("-" * 70)
    lines.append(f"FINDINGS  ({len(findings)} total)")
    lines.append("-" * 70)
    for i, f in enumerate(findings, 1):
        lines.append(f"  [{f['severity'].upper()}] {f['domain']}")
        lines.append(f"  {i}. {f['question']}")
        lines.append(f"     Status: {f['status']}")
        lines.append("")
    lines.append("-" * 70)
    lines.append("RECOMMENDATIONS")
    lines.append("-" * 70)
    for i, r in enumerate(recommendations, 1):
        lines.append(f"  {i}. {r}")
        lines.append("")
    lines.append("=" * 70)
    lines.append("END OF REPORT")
    lines.append("=" * 70)
    return "\n".join(lines)


# ============================================================
# SIDEBAR — System Information
# ============================================================
with st.sidebar:
    st.markdown('<p class="section-label">System Under Review</p>', unsafe_allow_html=True)

    system_name = st.text_input("AI System Name", placeholder="e.g. LoanDecisionAI v2.1")
    use_case = st.text_input("Use Case", placeholder="e.g. Credit scoring for retail lending")
    sector = st.selectbox("Sector", [
        "Financial Services", "Healthcare", "Public Sector / Government",
        "Human Resources", "Education", "Legal", "Retail / E-Commerce",
        "Insurance", "Other"
    ])
    deployment_stage = st.selectbox("Deployment Stage", [
        "Pre-deployment (design/testing)",
        "Pilot / limited rollout",
        "Full production",
        "Under review / suspended"
    ])
    assessor = st.text_input("Assessor Name", placeholder="e.g. Khushi Rana")

    st.markdown("---")
    st.markdown('<p class="section-label">About This Framework</p>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size:0.78rem;color:#888;line-height:1.6;">
    Draws from:<br>
    · <b>EU AI Act</b> (2024)<br>
    · <b>NIST AI RMF 1.0</b><br>
    · <b>ISO/IEC 42001</b><br>
    · <b>OECD AI Principles</b>
    </p>
    """, unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================
st.markdown(f"""
<div class="audit-header">
    <div class="audit-tag">⚖ AI Governance · Risk Assessment Tool</div>
    <h1>AI Governance Audit Framework</h1>
    <p>Evaluate an AI system against structured governance criteria drawn from the EU AI Act, NIST AI Risk Management Framework, and ISO 42001. Identify gaps, assess risk exposure, and generate a findings report.</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# INSTRUCTIONS
# ============================================================
with st.expander("How to use this tool", expanded=False):
    st.markdown("""
    **This tool walks through five governance domains.** For each question, select the response that most accurately reflects the current state of the AI system under review.

    - **Yes — fully in place**: A formal process, document, or control exists and is operational
    - **Partially — in progress**: Work has begun but is incomplete or inconsistently applied
    - **No — not addressed**: No action has been taken on this item
    - **Not applicable**: This criterion is genuinely irrelevant to this system (use sparingly)

    After completing all five domains, scroll to the **Results** section for scores, findings, and recommendations. You can download a full audit report as a text file.

    *Intended for educational and portfolio purposes. Not a substitute for a formal regulatory compliance review.*
    """)

st.markdown("---")


# ============================================================
# ASSESSMENT FORM — Five Domains
# ============================================================
all_responses = {}
domain_scores = {}

for domain, domain_data in DOMAINS.items():
    st.markdown(f'<p class="section-label">Domain</p>', unsafe_allow_html=True)

    severity_counts = {"critical": 0, "high": 0}
    for _, sev in domain_data["questions"]:
        if sev in severity_counts:
            severity_counts[sev] += 1

    pills = ""
    if severity_counts["critical"]:
        pills += f'<span class="pill pill-critical">{severity_counts["critical"]} critical</span>'
    if severity_counts["high"]:
        pills += f'<span class="pill pill-high">{severity_counts["high"]} high</span>'

    st.markdown(f"""
    <div class="domain-card">
        <div class="domain-title">{domain_data['icon']} &nbsp; {domain} {pills}</div>
        <div class="domain-desc">{domain_data['description']}</div>
    </div>
    """, unsafe_allow_html=True)

    responses = {}
    for i, (question, severity) in enumerate(domain_data["questions"]):
        key = f"{domain}_{i}"
        label = f"[{severity.upper()}] {question}"
        response = st.radio(
            label,
            options=list(RISK_LEVELS.keys()),
            horizontal=True,
            key=key,
            index=3  # Default: Not applicable
        )
        responses[key] = response

    all_responses[domain] = responses
    domain_scores[domain] = compute_domain_score(responses, domain_data["questions"])

st.markdown("---")


# ============================================================
# RESULTS
# ============================================================
overall_score = compute_overall_score(domain_scores)
rating, risk_level, rating_color = score_to_rating(overall_score)
findings = generate_findings(all_responses, system_name or "Unnamed System")
recommendations = generate_recommendations(findings)

st.markdown('<p class="section-label">Results</p>', unsafe_allow_html=True)
st.markdown("## Assessment Results")

# Score + radar side by side
col_score, col_radar, col_bar = st.columns([1, 1.4, 1.4])

with col_score:
    critical_count = sum(1 for f in findings if f["severity"] == "critical")
    high_count     = sum(1 for f in findings if f["severity"] == "high")
    medium_count   = sum(1 for f in findings if f["severity"] == "medium")

    st.markdown(f"""
    <div class="score-card">
        <div class="score-label">Overall Score</div>
        <div class="score-number" style="color:{rating_color};">{overall_score:.0f}</div>
        <div style="font-family:'DM Mono',monospace;font-size:0.7rem;letter-spacing:1px;
                    color:{rating_color};margin-bottom:18px;">{rating.upper()}</div>
        <div style="font-family:'DM Mono',monospace;font-size:0.68rem;color:rgba(247,245,240,0.4);
                    letter-spacing:1px;margin-bottom:10px;">FINDINGS BREAKDOWN</div>
        <div style="font-size:0.85rem;line-height:2;">
            <span style="color:#e74c3c;">■</span>
            <span style="font-family:'DM Mono',monospace;font-size:0.75rem;color:rgba(247,245,240,0.7);">
                &nbsp;{critical_count} Critical</span><br>
            <span style="color:#e67e22;">■</span>
            <span style="font-family:'DM Mono',monospace;font-size:0.75rem;color:rgba(247,245,240,0.7);">
                &nbsp;{high_count} High</span><br>
            <span style="color:#f1c40f;">■</span>
            <span style="font-family:'DM Mono',monospace;font-size:0.75rem;color:rgba(247,245,240,0.7);">
                &nbsp;{medium_count} Medium</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_radar:
    st.markdown('<p style="font-family:\'DM Mono\',monospace;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;color:#888;margin-bottom:0;">Coverage Radar</p>', unsafe_allow_html=True)
    st.plotly_chart(build_radar_chart(domain_scores), use_container_width=True)

with col_bar:
    st.markdown('<p style="font-family:\'DM Mono\',monospace;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;color:#888;margin-bottom:0;">Domain Scores</p>', unsafe_allow_html=True)
    st.plotly_chart(build_bar_chart(domain_scores), use_container_width=True)

st.markdown("---")


# ============================================================
# FINDINGS
# ============================================================
st.markdown('<p class="section-label">Findings</p>', unsafe_allow_html=True)
st.markdown(f"### {len(findings)} Finding{'s' if len(findings) != 1 else ''} Identified")

if not findings:
    st.success("No gaps identified. All assessed criteria are fully in place.")
else:
    for f in findings:
        sev = f["severity"]
        st.markdown(f"""
        <div class="finding {sev}">
            <div class="finding-label {sev}">{sev.upper()} · {f['domain']} · {f['status']}</div>
            {f['question']}
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")


# ============================================================
# RECOMMENDATIONS
# ============================================================
st.markdown('<p class="section-label">Recommendations</p>', unsafe_allow_html=True)
st.markdown("### Recommended Actions")

if not recommendations:
    st.success("No priority recommendations at this time. Continue monitoring and schedule a re-assessment in 6 months.")
else:
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"""
        <div class="rec-card">
            <span class="rec-number">{i:02d}</span>
            {rec}
            <div style="clear:both;"></div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")


# ============================================================
# DOWNLOAD REPORT
# ============================================================
st.markdown('<p class="section-label">Export</p>', unsafe_allow_html=True)
st.markdown("### Download Audit Report")

report_text = generate_report_text(
    system_name or "Unnamed System",
    use_case or "Not specified",
    sector,
    overall_score,
    rating,
    domain_scores,
    findings,
    recommendations,
    assessor or "Not specified"
)

col_dl, col_meta, _ = st.columns([1, 2, 1])
with col_dl:
    filename = f"ai_audit_{(system_name or 'system').lower().replace(' ', '_')}_{datetime.today().strftime('%Y%m%d')}.txt"
    st.download_button(
        label="⬇  Download Full Report (.txt)",
        data=report_text.encode("utf-8"),
        file_name=filename,
        mime="text/plain",
        use_container_width=True
    )
with col_meta:
    st.markdown(f"""
    <p style="font-size:0.78rem;color:#888;line-height:1.8;margin-top:8px;">
    System: <b>{system_name or '—'}</b><br>
    Assessed: <b>{datetime.today().strftime('%B %d, %Y')}</b><br>
    Framework: EU AI Act · NIST AI RMF · ISO 42001
    </p>
    """, unsafe_allow_html=True)

st.markdown("---")

# Footer
st.markdown("""
<p style="font-size:0.75rem;color:#bbb;text-align:center;font-family:'DM Mono',monospace;
          letter-spacing:0.5px;padding:16px 0;">
Built by Khushi Rana &nbsp;·&nbsp; AI Governance Audit Framework &nbsp;·&nbsp;
For educational and portfolio purposes
</p>
""", unsafe_allow_html=True)

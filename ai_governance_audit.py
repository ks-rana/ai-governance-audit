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
.main, .block-container { background-color: #0c0f1a !important; }
[data-testid="stAppViewContainer"] { background-color: #0c0f1a !important; }
[data-testid="stHeader"] { background-color: #0c0f1a !important; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; color: #f0ece4 !important; letter-spacing: -0.3px; }

/* ---- SIDEBAR — UNTOUCHED ---- */
[data-testid="stSidebar"] { background: #080b14 !important; border-right: 1px solid rgba(255,255,255,0.06); }
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span { color: #c8c4bc !important; }
[data-testid="stSidebar"] input[type="text"] {
    background-color: #111828 !important;
    color: #e8e4dc !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 6px !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #111828 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 6px !important;
    color: #e8e4dc !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] span,
[data-testid="stSidebar"] [data-baseweb="select"] div {
    color: #e8e4dc !important;
    background-color: transparent !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] svg { fill: #5a7fa8 !important; }
[data-baseweb="popover"] [data-baseweb="menu"] {
    background-color: #111828 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}
[data-baseweb="popover"] [role="option"] {
    background-color: #111828 !important;
    color: #e8e4dc !important;
}
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="popover"] [aria-selected="true"] {
    background-color: #1a2a42 !important;
    color: #7eb8d4 !important;
}

/* ---- LABELS ---- */
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

/* ---- HERO ---- */
.hero {
    background: #111828;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 20px;
    padding: 48px 44px 40px;
    margin-bottom: 24px;
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
.hero p { color: rgba(232,228,220,0.65) !important; font-size: 0.95rem; margin: 0; line-height: 1.7; max-width: 640px; }

/* ---- DISCLAIMER ---- */
.disclaimer {
    background: rgba(246,173,85,0.06);
    border: 1px solid rgba(246,173,85,0.2);
    border-left: 3px solid #f6ad55;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin-bottom: 20px;
    font-size: 0.86rem;
    color: rgba(232,228,220,0.82);
    line-height: 1.75;
}
.disclaimer-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #f6ad55;
    margin-bottom: 6px;
}

/* ---- PROGRESS ---- */
.progress-bar-outer {
    background: rgba(255,255,255,0.05);
    border-radius: 99px;
    height: 4px;
    margin: 20px 0 8px;
    overflow: hidden;
}
.progress-bar-inner { height: 4px; border-radius: 99px; background: linear-gradient(90deg, #5a7fa8, #7eb8d4); }
.step-counter {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 1px;
    color: rgba(232,228,220,0.5);
    margin-bottom: 24px;
}

/* ---- DOMAIN HEADER CARD ---- */
.step-card {
    background: #111828;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 28px 28px 24px;
    margin-bottom: 24px;
}
.step-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    color: #f0ece4;
    margin-bottom: 6px;
}
.step-card-desc {
    font-size: 0.88rem;
    color: rgba(232,228,220,0.65);
    line-height: 1.65;
    margin-bottom: 16px;
}

/* ---- QUESTION CARD ---- */
.q-card {
    background: #111828;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 18px 20px 14px;
    margin-bottom: 6px;
    transition: border-color 0.2s;
}
.q-card:hover {
    border-color: rgba(90,127,168,0.35);
}

/* ---- SEVERITY BADGES ---- */
.q-severity {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 2px 8px;
    border-radius: 3px;
    display: inline-block;
    margin-bottom: 8px;
}
.sev-critical { background: rgba(192,57,43,0.18); color: #f07060; border: 1px solid rgba(192,57,43,0.3); }
.sev-high     { background: rgba(211,84,0,0.18);  color: #f09050; border: 1px solid rgba(211,84,0,0.3); }
.sev-medium   { background: rgba(183,149,11,0.18); color: #f0d060; border: 1px solid rgba(183,149,11,0.3); }
.sev-low      { background: rgba(30,132,73,0.18);  color: #50d080; border: 1px solid rgba(30,132,73,0.3); }

/* ---- QUESTION TEXT — BRIGHT ---- */
.q-text {
    font-size: 0.93rem;
    color: #e8e4dc;
    line-height: 1.55;
    font-weight: 500;
    margin-bottom: 10px;
}

/* ---- EXPLANATION BOX ---- */
.q-explain {
    background: rgba(90,127,168,0.07);
    border-left: 2px solid rgba(90,127,168,0.3);
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    margin-bottom: 4px;
}
.q-explain-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #5a9fd4;
    margin-bottom: 5px;
}
.q-explain-text {
    font-size: 0.82rem;
    color: rgba(232,228,220,0.62);
    line-height: 1.7;
}

/* ---- BUTTONS ---- */
.stButton > button {
    background: #111828 !important;
    color: #e8e4dc !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 8px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.5px !important;
    padding: 10px 22px !important;
}
.stButton > button:hover {
    background: #1a2438 !important;
    border-color: rgba(90,127,168,0.45) !important;
    color: #f0ece4 !important;
}

/* ---- RADIO — BRIGHT AND READABLE ---- */
.stRadio > div { gap: 6px !important; flex-wrap: wrap !important; }
.stRadio label {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    padding: 9px 16px !important;
    font-size: 0.85rem !important;
    color: #d8d4cc !important;
    cursor: pointer !important;
    font-family: 'Libre Franklin', sans-serif !important;
    font-weight: 500 !important;
}
.stRadio label:hover {
    background: rgba(90,127,168,0.12) !important;
    border-color: rgba(90,127,168,0.4) !important;
    color: #f0ece4 !important;
}

/* ---- SCORE CARD ---- */
.score-hero {
    background: #111828;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 36px 32px;
    text-align: center;
}
.score-num { font-family: 'Syne', sans-serif; font-size: 5rem; font-weight: 800; line-height: 1; margin: 10px 0 6px; }
.score-lbl { font-family: 'DM Mono', monospace; font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: rgba(232,228,220,0.4); margin-bottom: 6px; }

/* ---- FINDINGS ---- */
.finding {
    border-left: 3px solid;
    padding: 16px 18px;
    margin-bottom: 10px;
    background: #111828;
    border-radius: 0 10px 10px 0;
    border-top: 1px solid rgba(255,255,255,0.05);
    border-right: 1px solid rgba(255,255,255,0.05);
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.finding-lbl {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.finding-text {
    font-size: 0.9rem;
    color: #e8e4dc;
    font-weight: 500;
    line-height: 1.55;
    margin-bottom: 8px;
}
.finding-explain {
    font-size: 0.81rem;
    color: rgba(232,228,220,0.55);
    line-height: 1.7;
    padding-top: 8px;
    border-top: 1px solid rgba(255,255,255,0.05);
}

/* ---- RECS ---- */
.rec {
    background: #111828;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 18px 22px;
    margin-bottom: 10px;
    font-size: 0.89rem;
    color: #d8d4cc;
    line-height: 1.7;
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

/* ---- SCORING TABLE ---- */
.score-table { width: 100%; border-collapse: collapse; font-size: 0.83rem; }
.score-table th { font-family: 'DM Mono', monospace; font-size: 0.6rem; letter-spacing: 1.5px; text-transform: uppercase; color: #5a7fa8; padding: 8px 12px; border-bottom: 1px solid rgba(255,255,255,0.08); text-align: left; }
.score-table td { padding: 9px 12px; border-bottom: 1px solid rgba(255,255,255,0.04); color: rgba(232,228,220,0.8); vertical-align: top; }
.score-table tr:last-child td { border-bottom: none; }

/* ---- FW TAGS ---- */
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
    color: #7eb8d4;
    border: 1px solid rgba(90,127,168,0.25);
}

/* ---- MISC ---- */
.stTextInput input { background: #111828 !important; border-color: rgba(255,255,255,0.08) !important; color: #e8e4dc !important; border-radius: 8px !important; }
.stDownloadButton button { background: #1e3a5f !important; color: #7eb8d4 !important; border: 1px solid rgba(90,127,168,0.35) !important; border-radius: 8px !important; font-family: 'DM Mono', monospace !important; font-size: 0.75rem !important; }
.stDownloadButton button:hover { background: #254a78 !important; }
hr { border-color: rgba(255,255,255,0.07) !important; }
.streamlit-expanderHeader { background: #111828 !important; color: #d8d4cc !important; border-radius: 10px !important; font-family: 'Libre Franklin', sans-serif !important; border: 1px solid rgba(255,255,255,0.07) !important; }
.streamlit-expanderContent { background: #0f1623 !important; border: 1px solid rgba(255,255,255,0.06) !important; border-radius: 0 0 10px 10px !important; }
[data-testid="stTabs"] button { color: rgba(232,228,220,0.6) !important; font-family: 'DM Mono', monospace !important; font-size: 0.75rem !important; }
[data-testid="stTabs"] button[aria-selected="true"] { color: #e8e4dc !important; border-bottom-color: #5a7fa8 !important; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# FRAMEWORK DATA — questions now include explanations
# ============================================================
DOMAINS = {
    "Transparency & Explainability": {
        "icon": "◎", "weight": 0.20,
        "description": "Can the system's decisions be explained to affected users and auditors? Are model inputs, outputs, and logic disclosed appropriately?",
        "frameworks": ["EU AI Act Art. 13", "NIST AI RMF – MAP", "ISO 42001 §8.4"],
        "questions": [
            (
                "Is documentation available explaining how the AI system makes decisions?",
                "high",
                "System documentation — sometimes called a model card or technical spec — describes the logic, inputs, and outputs of an AI system. Without it, auditors and affected users have no basis for understanding or challenging a decision. The EU AI Act Art. 13 requires this for high-risk systems."
            ),
            (
                "Can the system provide explanations for individual decisions to affected users?",
                "high",
                "Individual explainability means a person denied a loan, flagged in a hiring process, or affected by any AI decision can receive a plain-language reason. This is a legal right in many jurisdictions (GDPR Art. 22, PIPEDA) and a core ethical principle. Systems that cannot explain individual outputs are fundamentally unaccountable."
            ),
            (
                "Are training data sources, types, and collection methods disclosed?",
                "medium",
                "AI systems learn from data — and undisclosed or poorly understood training data is one of the most common sources of bias and error. Disclosure of data sources, collection methods, and any known limitations allows reviewers to assess whether the system has a sound foundation. Omitting this is a major gap under NIST AI RMF MAP function."
            ),
            (
                "Is there a published model card describing capabilities and limitations?",
                "medium",
                "A model card is a short document (often 1–2 pages) that describes what a model is designed to do, what it should not be used for, its performance characteristics, and known failure modes. Pioneered by Google, now expected by many AI governance frameworks. Its absence makes third-party evaluation almost impossible."
            ),
            (
                "Are performance benchmarks and accuracy metrics available internally or publicly?",
                "low",
                "Accuracy metrics tell you how well the system performs — but also where it fails. Without these, it is impossible to compare the system against alternatives, set performance thresholds, or demonstrate that it meets minimum quality standards. Even internal availability (not public) is a baseline expectation."
            ),
        ]
    },
    "Fairness & Non-Discrimination": {
        "icon": "◑", "weight": 0.22,
        "description": "Does the system treat individuals and groups equitably? Has it been tested for bias across protected characteristics?",
        "frameworks": ["EU AI Act Art. 10", "NIST AI RMF – MEASURE", "OECD AI Principles"],
        "questions": [
            (
                "Has the system been tested for differential performance across demographic groups?",
                "critical",
                "Disparate impact testing checks whether an AI system performs differently — in accuracy, error rate, or outcome — for different demographic groups (race, gender, age, disability, etc.). A system that is 95% accurate overall may be 80% accurate for a minority group. Without this test, you cannot know whether the system is discriminating, intentionally or not."
            ),
            (
                "Are there mechanisms to detect and correct discriminatory outputs?",
                "high",
                "Detection mechanisms — monitoring, feedback loops, human review queues — catch discriminatory outputs after deployment. Correction mechanisms allow the system to be retrained, recalibrated, or overridden when bias is detected. Without both, a system may discriminate indefinitely after launch with no remediation pathway."
            ),
            (
                "Was training data audited for historical bias before use?",
                "high",
                "Historical data often encodes past discrimination — for example, hiring data that reflects decades of biased decisions, or lending data from an era of redlining. Using this data uncritically trains the AI to replicate those biases. A pre-training data audit identifies and documents these risks before they are baked into the system."
            ),
            (
                "Does the system comply with anti-discrimination laws in its jurisdiction?",
                "critical",
                "In most jurisdictions, using AI in hiring, lending, housing, or healthcare that results in disparate impact on protected groups violates existing law — even without discriminatory intent. Compliance requires a legal review of applicable statutes (e.g. Human Rights Act in Canada, Equal Credit Opportunity Act in the US, EU non-discrimination directives). This is non-negotiable."
            ),
            (
                "Is there a formal fairness metric used to evaluate model outputs?",
                "medium",
                "Fairness metrics quantify bias mathematically — common examples include demographic parity, equalized odds, and predictive parity. Without a defined metric, 'fairness' is a vague claim rather than a measurable standard. Different metrics encode different values and trade-offs, so choosing one requires deliberate ethical reasoning, not just technical convenience."
            ),
        ]
    },
    "Accountability & Oversight": {
        "icon": "◻", "weight": 0.22,
        "description": "Who is responsible when the AI system causes harm? Are there human review processes, escalation paths, and audit trails?",
        "frameworks": ["OSFI E-23 §4", "NIST AI RMF – GOVERN", "ISO 42001 §5.3", "EU AI Act Art. 17"],
        "questions": [
            (
                "Is there a named responsible party accountable for the system's outcomes?",
                "critical",
                "Without a named owner, accountability diffuses across teams and no one is responsible when something goes wrong. OSFI E-23 requires model owners for all material models. The EU AI Act requires designated responsible persons for high-risk AI. A named owner also ensures someone has the authority to pull the system offline if needed."
            ),
            (
                "Are audit logs maintained of system decisions and interactions?",
                "high",
                "Audit logs are a record of what the system decided, when, and based on what inputs. They are essential for post-incident investigation, regulatory inquiry, and monitoring for drift or abuse. Without logs, a system operates as a black box — decisions cannot be reconstructed, challenged, or explained after the fact."
            ),
            (
                "Is there a human-in-the-loop process for high-stakes decisions?",
                "high",
                "Human-in-the-loop (HITL) means a human reviews or can override the AI's decision before it takes effect — particularly for decisions that significantly affect individuals (loan denials, medical triage, benefit eligibility). The EU AI Act mandates HITL for high-risk AI systems. HITL does not mean reviewing everything — it means having a defined escalation path for high-stakes cases."
            ),
            (
                "Is there a formal incident response process for AI-related harms?",
                "medium",
                "An AI incident response process defines what happens when something goes wrong — who gets notified, how the system is suspended, how affected individuals are informed, and how root causes are investigated. Without this, organisations react to AI failures reactively and inconsistently, often exacerbating reputational and regulatory harm."
            ),
            (
                "Has an external or third-party audit been conducted?",
                "medium",
                "Internal teams often have blind spots, institutional biases, and insufficient independence to audit their own systems rigorously. Third-party audits bring external credibility, methodological rigour, and legal defensibility. They are increasingly expected by regulators and institutional clients as a condition of deployment in high-risk domains."
            ),
        ]
    },
    "Security & Robustness": {
        "icon": "◈", "weight": 0.18,
        "description": "Is the system resilient to adversarial inputs, data poisoning, and misuse? Are vulnerabilities regularly assessed?",
        "frameworks": ["NIST AI RMF – MANAGE", "ISO 42001 §8.5", "EU AI Act Art. 15"],
        "questions": [
            (
                "Has the system been tested against adversarial inputs and prompt injection?",
                "high",
                "Adversarial inputs are deliberately crafted to confuse or manipulate an AI system — causing it to misclassify, generate harmful output, or bypass safety controls. Prompt injection is a specific attack on language models. Testing for these before deployment is a baseline security requirement, analogous to penetration testing for software systems."
            ),
            (
                "Is there protection against data poisoning during model training?",
                "high",
                "Data poisoning involves introducing corrupted or malicious data into the training pipeline, causing the model to learn incorrect or harmful patterns. This can be an intentional attack or an accidental contamination from poor data governance. Protections include data provenance tracking, validation pipelines, and restricted access to training infrastructure."
            ),
            (
                "Are access controls in place to prevent unauthorized model queries?",
                "medium",
                "Unrestricted access to an AI model allows adversaries to probe it systematically — extracting training data, reverse-engineering decision logic, or generating harmful outputs at scale. Access controls (authentication, rate limiting, scope restrictions) are standard security hygiene and particularly important for models deployed via API."
            ),
            (
                "Is there monitoring for model drift or performance degradation in production?",
                "medium",
                "Models degrade over time as the real-world distribution of data shifts away from the training distribution — a phenomenon called drift. A model that performed well at launch may perform poorly six months later without anyone noticing, if monitoring is absent. Production monitoring with alerting thresholds is required under ISO 42001 §8.5."
            ),
            (
                "Has a red-teaming or penetration testing exercise been conducted?",
                "low",
                "Red-teaming involves a dedicated team attempting to break, mislead, or misuse the AI system — simulating what a motivated adversary would do. It is distinct from standard QA testing in that it is adversarial and open-ended. Leading AI labs (OpenAI, Anthropic, Google DeepMind) conduct red-teaming before major deployments. It surfaces failure modes that normal testing misses."
            ),
        ]
    },
    "Privacy & Data Governance": {
        "icon": "◍", "weight": 0.18,
        "description": "Does the system comply with data protection laws? Is personal data handled, stored, and retained appropriately?",
        "frameworks": ["GDPR / PIPEDA / CCPA", "ISO 42001 §8.3", "OECD AI Principles", "OSFI E-23 §6"],
        "questions": [
            (
                "Does the system comply with applicable privacy laws (GDPR, PIPEDA, CCPA)?",
                "critical",
                "GDPR (EU), PIPEDA (Canada), and CCPA (California) all impose obligations on AI systems that process personal data — consent requirements, rights of access and deletion, restrictions on automated decision-making, and mandatory breach notification. Non-compliance carries significant fines (up to 4% of global revenue under GDPR) and reputational damage. This is the baseline legal floor."
            ),
            (
                "Is personal data minimized — only collected and retained as needed?",
                "high",
                "Data minimization is a foundational privacy principle — collect only what you need, retain it only as long as necessary, and delete it when the purpose is fulfilled. AI systems often over-collect data 'just in case' it might be useful for training. This creates unnecessary privacy risk and legal exposure. Both GDPR Art. 5 and PIPEDA require data minimization."
            ),
            (
                "Are data subjects informed when AI is used to make decisions about them?",
                "high",
                "Transparency to data subjects — the people the AI makes decisions about — is a legal right in most jurisdictions. Under GDPR Art. 22, individuals have the right to know when a decision is made solely by automated means and to request human review. Failing to inform data subjects is both a legal violation and an ethical failure."
            ),
            (
                "Is there a data retention and deletion policy in place?",
                "medium",
                "A retention policy specifies how long different categories of data are kept and when they are deleted. Without one, organisations accumulate data indefinitely — increasing breach risk, storage costs, and regulatory exposure. Deletion mechanisms are particularly important for AI training data, where removing personal data from a trained model is technically complex."
            ),
            (
                "Are data sharing agreements reviewed before training data is acquired?",
                "medium",
                "Training data often comes from third parties — scraped from the web, purchased from data brokers, or shared by partners. Without reviewing the legal basis for that data's collection and the terms under which it can be used for AI training, organisations may be training on data they have no right to use — a growing area of regulatory and litigation risk."
            ),
        ]
    }
}

RESPONSE_OPTS = ["Yes — fully in place", "Partially — in progress", "No — not addressed", "Not applicable"]
RISK_LEVELS   = {"Yes — fully in place": 1.0, "Partially — in progress": 0.5,
                 "No — not addressed": 0.0, "Not applicable": None}
STEPS = ["Welcome"] + list(DOMAINS.keys()) + ["Results"]

REC_MAP = {
    "Transparency & Explainability": "Develop and publish a model card documenting capabilities, limitations, training data sources, and performance benchmarks. This is a baseline expectation under EU AI Act Art. 13 and NIST AI RMF.",
    "Fairness & Non-Discrimination": "Commission a formal bias audit across protected demographic characteristics. Establish a fairness metric (e.g. equalized odds, demographic parity) and define an acceptable disparity threshold before deployment.",
    "Accountability & Oversight": "Assign a named AI system owner accountable for outcomes. Implement human-in-the-loop review for high-stakes decisions and establish an incident response playbook for AI-related harms (OSFI E-23 §4).",
    "Security & Robustness": "Conduct adversarial testing and red-teaming before deployment. Implement production monitoring for model drift with alerting thresholds defined by the system owner (ISO 42001 §8.5).",
    "Privacy & Data Governance": "Conduct a Privacy Impact Assessment and map all personal data flows. Ensure data subject notification obligations are met and a deletion mechanism exists (GDPR Art. 17 / PIPEDA).",
}


# ============================================================
# SESSION STATE
# ============================================================
for k, v in [("step", 0), ("responses", {}), ("meta", {})]:
    if k not in st.session_state:
        st.session_state[k] = v


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
    return {"critical": "#f07060", "high": "#f09050", "medium": "#f0d060", "low": "#50d080"}.get(sev, "#888")

def get_findings():
    downgrade = {"critical": "high", "high": "medium", "medium": "low", "low": "low"}
    sev_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    findings  = []
    for domain, dd in DOMAINS.items():
        resp = st.session_state.responses.get(domain, {})
        for i, (q, sev, explain) in enumerate(dd["questions"]):
            r = resp.get(f"{domain}_{i}", "Not applicable")
            if r == "No — not addressed":
                findings.append({"domain": domain, "q": q, "sev": sev,
                                  "status": "Gap — not addressed", "explain": explain})
            elif r == "Partially — in progress":
                findings.append({"domain": domain, "q": q, "sev": downgrade[sev],
                                  "status": "Partially addressed", "explain": explain})
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
                tickfont=dict(size=9, family='DM Mono', color='rgba(232,228,220,0.35)'),
                gridcolor='rgba(255,255,255,0.07)', linecolor='rgba(255,255,255,0.07)'),
            angularaxis=dict(
                tickfont=dict(size=10, family='Libre Franklin', color='rgba(232,228,220,0.7)'),
                gridcolor='rgba(255,255,255,0.07)', linecolor='rgba(255,255,255,0.07)')
        ),
        paper_bgcolor='rgba(0,0,0,0)', showlegend=False,
        margin=dict(l=40,r=40,t=40,b=40), height=320
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
        textfont=dict(family='DM Mono', size=11, color='rgba(232,228,220,0.65)')
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(range=[0,118], showgrid=True, gridcolor='rgba(255,255,255,0.06)',
                   tickfont=dict(family='DM Mono', size=9, color='rgba(232,228,220,0.4)')),
        xaxis=dict(tickfont=dict(family='Libre Franklin', size=10, color='rgba(232,228,220,0.7)')),
        margin=dict(l=10,r=10,t=24,b=10), height=280, showlegend=False
    )
    return fig

def build_report_text():
    sc   = overall_score()
    rat  = rating(sc)[0]
    fnd  = get_findings()
    d_sc = {d: domain_score(d) for d in DOMAINS}
    meta = st.session_state.meta
    date = datetime.today().strftime("%B %d, %Y")
    resp_display = {
        "Yes — fully in place": "YES", "Partially — in progress": "PARTIAL",
        "No — not addressed": "NO",    "Not applicable": "N/A"
    }
    lines = [
        "=" * 68, "AI GOVERNANCE AUDIT REPORT", "=" * 68,
        f"System        : {meta.get('system','—')}",
        f"Use Case      : {meta.get('usecase','—')}",
        f"Sector        : {meta.get('sector','—')}",
        f"Deployment    : {meta.get('stage','—')}",
        f"Assessed by   : {meta.get('assessor','—')}",
        f"Date          : {date}",
        f"Framework     : EU AI Act · NIST AI RMF 1.0 · ISO 42001 · OSFI E-23",
        "",
        "DISCLAIMER", "-" * 68,
        "This report is generated by an educational tool and is intended as a",
        "reference for responsible AI principles only. It does not constitute",
        "a formal compliance assessment, legal opinion, or regulatory determination.",
        "For real decisions, please engage your organisation's AI Risk Committee,",
        "legal counsel, or a qualified AI governance advisor.",
        "",
        "-" * 68, "SCORING METHODOLOGY", "-" * 68,
        "Each response is scored: Yes = 1.0 | Partial = 0.5 | No = 0.0 | N/A = excluded",
        "Domain score = average of scored responses × 100",
        "Overall score = weighted average across 5 domains:",
        "  Transparency (20%) · Fairness (22%) · Accountability (22%)",
        "  Security (18%) · Privacy (18%)",
        "Rating: 80–100 Strong · 60–79 Adequate · 40–59 Needs Work · <40 High Risk",
        "",
        "-" * 68, "OVERALL SCORE", "-" * 68,
        f"  {sc:.1f} / 100   —   {rat}", "",
        "-" * 68, "DOMAIN SCORES", "-" * 68,
    ]
    for d, s in d_sc.items():
        lines.append(f"  {d:<40} {s:>5.1f}   {rating(s)[0]}")
    lines += ["", "-" * 68, "FULL RESPONSE LOG", "-" * 68]
    for domain, dd in DOMAINS.items():
        lines.append(f"\n  {domain}")
        resp = st.session_state.responses.get(domain, {})
        for i, (q, sev, _) in enumerate(dd["questions"]):
            r = resp.get(f"{domain}_{i}", "Not applicable")
            lines.append(f"    [{resp_display.get(r,'?')}] [{sev.upper()}] {q}")
    lines += ["", "-" * 68, f"FINDINGS  ({len(fnd)} total)", "-" * 68]
    for i, f in enumerate(fnd, 1):
        lines += [f"  [{f['sev'].upper()}] {f['domain']}",
                  f"  {i}. {f['q']}",
                  f"     Status: {f['status']}", ""]
    shown = set()
    recs  = []
    for f in fnd:
        if f["sev"] in ("critical","high") and f["domain"] not in shown:
            shown.add(f["domain"])
            recs.append(REC_MAP[f["domain"]])
    if len(fnd) > 8:
        recs.append("Given the volume of open findings, consider a phased rollout with staged governance reviews.")
    if any(f["sev"] == "critical" for f in fnd):
        recs.append("Critical findings must be resolved before deployment. Escalate to senior leadership.")
    if recs:
        lines += ["-" * 68, "RECOMMENDATIONS", "-" * 68]
        for i, r in enumerate(recs, 1):
            lines += [f"  {i}. {r}", ""]
    lines += ["=" * 68, "END OF REPORT", "=" * 68]
    return "\n".join(lines)


# ============================================================
# SIDEBAR — UNTOUCHED
# ============================================================
with st.sidebar:
    st.markdown('<span class="slabel">System Under Review</span>', unsafe_allow_html=True)
    st.session_state.meta["system"]   = st.text_input("AI System Name",   value=st.session_state.meta.get("system",""),   placeholder="e.g. LoanDecisionAI v2.1")
    st.session_state.meta["usecase"]  = st.text_input("Use Case",         value=st.session_state.meta.get("usecase",""),  placeholder="e.g. Credit scoring")
    st.session_state.meta["sector"]   = st.selectbox("Sector",
        ["Financial Services","Healthcare","Public Sector","HR","Education","Legal","Retail","Insurance","Other"])
    st.session_state.meta["stage"]    = st.selectbox("Deployment Stage",
        ["Pre-deployment","Pilot / limited rollout","Full production","Under review / suspended"])
    st.session_state.meta["assessor"] = st.text_input("Assessor",         value=st.session_state.meta.get("assessor",""), placeholder="Your name")
    st.markdown("---")
    st.markdown('<span class="slabel">Frameworks</span>', unsafe_allow_html=True)
    st.markdown('<span class="fw-tag">EU AI Act</span><span class="fw-tag">NIST AI RMF</span><span class="fw-tag">ISO 42001</span><span class="fw-tag">OSFI E-23</span><span class="fw-tag">OECD 2025</span>', unsafe_allow_html=True)
    st.markdown("---")
    cur = st.session_state.step
    pct = int((cur / (len(STEPS) - 1)) * 100)
    st.markdown(f'<span class="slabel">Progress — {pct}%</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="progress-bar-outer"><div class="progress-bar-inner" style="width:{pct}%;"></div></div>', unsafe_allow_html=True)
    for i, s in enumerate(STEPS):
        c      = "#5a9fd4" if i == cur else ("#2ecc71" if i < cur else "rgba(232,228,220,0.2)")
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

    st.markdown("""
    <div class="disclaimer">
        <div class="disclaimer-title">⚠ Important Disclaimer — Please Read Before Proceeding</div>
        This tool is an <b>educational reference</b> designed to support awareness of responsible AI principles.
        It is <b>not</b> a formal compliance assessment, legal opinion, or regulatory determination.<br><br>
        The questions and scoring reflect broadly accepted governance frameworks (EU AI Act, NIST AI RMF,
        ISO 42001, OSFI E-23) but are simplified for portfolio and educational purposes. No score produced
        by this tool should be treated as a definitive view of an AI system's regulatory status or risk profile.<br><br>
        <b>If you are dealing with a real AI deployment decision</b>, do not rely on this tool as your final
        reference. Please engage your organisation's <b>AI Risk Committee</b>, legal counsel, compliance team,
        or a qualified AI governance advisor before making deployment, procurement, or policy decisions.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    for col, icon, title, desc in [
        (c1, "◎", "5 Governance Domains",    "Transparency, Fairness, Accountability, Security, Privacy"),
        (c2, "◈", "25 Structured Questions",  "Each question includes a plain-language explanation of why it matters"),
        (c3, "◻", "Scored Risk Report",       "Weighted score, radar chart, findings, and copyable report"),
    ]:
        col.markdown(f"""
        <div style="background:#111828;border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:22px 20px;">
            <div style="font-size:1.3rem;color:#5a7fa8;margin-bottom:10px;">{icon}</div>
            <div style="font-family:'Syne',sans-serif;font-size:0.95rem;font-weight:700;color:#f0ece4;margin-bottom:6px;">{title}</div>
            <div style="font-size:0.8rem;color:rgba(232,228,220,0.55);line-height:1.6;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("How scoring works — methodology & weights"):
        st.markdown("""
        <p style="font-size:0.86rem;color:rgba(232,228,220,0.7);line-height:1.8;margin-bottom:16px;">
        Each question is answered on a 4-point scale, then converted to a numeric value:
        </p>
        <table class="score-table">
            <tr><th>Response</th><th>Score Value</th><th>What it means</th></tr>
            <tr><td>Yes — fully in place</td><td style="color:#2ecc71;font-family:'DM Mono',monospace;">1.0</td><td>Full credit — control exists and is operational</td></tr>
            <tr><td>Partially — in progress</td><td style="color:#f1c40f;font-family:'DM Mono',monospace;">0.5</td><td>Half credit — work started but incomplete</td></tr>
            <tr><td>No — not addressed</td><td style="color:#e74c3c;font-family:'DM Mono',monospace;">0.0</td><td>No credit — gap identified</td></tr>
            <tr><td>Not applicable</td><td style="color:#888;font-family:'DM Mono',monospace;">excluded</td><td>Question excluded from denominator</td></tr>
        </table>
        <p style="font-size:0.83rem;color:rgba(232,228,220,0.65);margin-top:16px;line-height:1.8;">
        <b style="color:#e8e4dc;">Domain score</b> = average of all scored responses × 100<br>
        <b style="color:#e8e4dc;">Overall score</b> = weighted average across 5 domains:
        </p>
        <table class="score-table">
            <tr><th>Domain</th><th>Weight</th><th>Rationale</th></tr>
            <tr><td>Transparency & Explainability</td><td style="font-family:'DM Mono',monospace;color:#7eb8d4;">20%</td><td>Foundational — required for all other controls to be meaningful</td></tr>
            <tr><td>Fairness & Non-Discrimination</td><td style="font-family:'DM Mono',monospace;color:#7eb8d4;">22%</td><td>Highest regulatory and ethical exposure in most sectors</td></tr>
            <tr><td>Accountability & Oversight</td><td style="font-family:'DM Mono',monospace;color:#7eb8d4;">22%</td><td>Core to OSFI E-23 and NIST GOVERN function</td></tr>
            <tr><td>Security & Robustness</td><td style="font-family:'DM Mono',monospace;color:#7eb8d4;">18%</td><td>Critical but often more technical than governance-facing</td></tr>
            <tr><td>Privacy & Data Governance</td><td style="font-family:'DM Mono',monospace;color:#7eb8d4;">18%</td><td>Significant but partially covered by existing data protection regimes</td></tr>
        </table>
        <p style="font-size:0.83rem;color:rgba(232,228,220,0.55);margin-top:16px;">
        Rating: 80–100 Strong · 60–79 Adequate · 40–59 Needs Work · Below 40 High Risk
        </p>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#111828;border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:22px 24px;font-size:0.88rem;color:rgba(232,228,220,0.7);line-height:1.9;">
    Fill in the system details in the left sidebar, then work through 5 governance domains one at a time.<br>
    Each question includes a <b style="color:#e8e4dc;">plain-language explanation</b> of why it matters.<br><br>
    For each question select the response that best reflects the <i>current state</i> of the system:<br>
    &nbsp;&nbsp;<b style="color:#2ecc71;">Yes — fully in place</b> &nbsp;· A formal process or control exists and is operational<br>
    &nbsp;&nbsp;<b style="color:#f1c40f;">Partially — in progress</b> &nbsp;· Work has begun but is incomplete or inconsistent<br>
    &nbsp;&nbsp;<b style="color:#e74c3c;">No — not addressed</b> &nbsp;· No action has been taken<br>
    &nbsp;&nbsp;<b style="color:rgba(232,228,220,0.4);">Not applicable</b> &nbsp;· Genuinely irrelevant to this system (use sparingly)
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

    for i, (q, sev, explain) in enumerate(dd["questions"]):
        key     = f"{domain}_{i}"
        cur_val = st.session_state.responses[domain].get(key, "Not applicable")
        idx     = RESPONSE_OPTS.index(cur_val) if cur_val in RESPONSE_OPTS else 3

        st.markdown(f"""
        <div class="q-card">
            <div class="q-severity sev-{sev}">{sev}</div>
            <div class="q-text">{q}</div>
            <div class="q-explain">
                <div class="q-explain-title">Why this matters</div>
                <div class="q-explain-text">{explain}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        resp = st.radio("Response", RESPONSE_OPTS, index=idx, horizontal=True,
                        key=f"radio_{key}", label_visibility="collapsed")
        st.session_state.responses[domain][key] = resp
        st.markdown("<div style='margin-bottom:10px;'></div>", unsafe_allow_html=True)

    sc      = domain_score(domain)
    rat, col = rating(sc)
    st.markdown(f"""
    <div style="background:#111828;border:1px solid rgba(255,255,255,0.08);border-radius:10px;
                padding:16px 22px;margin-top:20px;display:flex;align-items:center;gap:16px;">
        <div style="font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;color:{col};">{sc:.0f}</div>
        <div>
            <div style="font-family:'DM Mono',monospace;font-size:0.6rem;letter-spacing:2px;text-transform:uppercase;color:rgba(232,228,220,0.35);">Domain Score So Far</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.75rem;color:{col};">{rat}</div>
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
    high_cnt = sum(1 for f in findings if f["sev"] == "high")
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
            <div style="font-family:'DM Mono',monospace;font-size:0.6rem;letter-spacing:2px;color:rgba(232,228,220,0.35);text-transform:uppercase;margin-bottom:12px;">Findings</div>
            <div style="font-size:0.85rem;line-height:2.2;text-align:left;padding-left:12px;">
                <span style="color:#f07060;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.75rem;color:rgba(232,228,220,0.7);">{crit} Critical</span><br>
                <span style="color:#f09050;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.75rem;color:rgba(232,228,220,0.7);">{high_cnt} High</span><br>
                <span style="color:#f0d060;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.75rem;color:rgba(232,228,220,0.7);">{med} Medium</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with cr:
        st.markdown('<span class="slabel">Coverage Radar</span>', unsafe_allow_html=True)
        st.plotly_chart(radar_chart(d_scores), use_container_width=True)
    with cb2:
        st.markdown('<span class="slabel">Domain Scores</span>', unsafe_allow_html=True)
        st.plotly_chart(bar_chart(d_scores), use_container_width=True)

    with st.expander("How was this score calculated?"):
        st.markdown("""
        <table class="score-table">
            <tr><th>Response</th><th>Value</th></tr>
            <tr><td>Yes — fully in place</td><td style="color:#2ecc71;font-family:'DM Mono',monospace;">1.0 (full credit)</td></tr>
            <tr><td>Partially — in progress</td><td style="color:#f1c40f;font-family:'DM Mono',monospace;">0.5 (half credit)</td></tr>
            <tr><td>No — not addressed</td><td style="color:#e74c3c;font-family:'DM Mono',monospace;">0.0 (no credit)</td></tr>
            <tr><td>Not applicable</td><td style="color:#888;font-family:'DM Mono',monospace;">excluded from average</td></tr>
        </table>
        <p style="font-size:0.83rem;color:rgba(232,228,220,0.65);margin-top:14px;line-height:1.8;">
        Domain weights: Transparency 20% · Fairness 22% · Accountability 22% · Security 18% · Privacy 18%<br>
        Rating: 80–100 Strong · 60–79 Adequate · 40–59 Needs Work · Below 40 High Risk
        </p>
        """, unsafe_allow_html=True)

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
                <div class="finding-text">{f['q']}</div>
                <div class="finding-explain"><b style="color:rgba(232,228,220,0.6);">Why this matters:</b> {f['explain']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<span class="slabel">Recommendations</span>', unsafe_allow_html=True)
    st.markdown("### Recommended Actions")

    shown = set()
    recs  = []
    for f in findings:
        if f["sev"] in ("critical","high") and f["domain"] not in shown:
            shown.add(f["domain"])
            recs.append(REC_MAP[f["domain"]])
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
    st.markdown("### Report")

    report_text = build_report_text()
    meta        = st.session_state.meta
    fname       = f"ai_audit_{(meta.get('system') or 'system').lower().replace(' ','_')}_{datetime.today().strftime('%Y%m%d')}.txt"

    tab1, tab2 = st.tabs(["Copy Report", "Download .txt"])
    with tab1:
        st.markdown('<p style="font-size:0.82rem;color:rgba(232,228,220,0.5);margin-bottom:10px;">Click inside the box → Ctrl+A / Cmd+A to select all → Ctrl+C / Cmd+C to copy.</p>', unsafe_allow_html=True)
        st.text_area("", value=report_text, height=380, label_visibility="collapsed")
    with tab2:
        st.markdown('<p style="font-size:0.82rem;color:rgba(232,228,220,0.5);margin-bottom:14px;">Downloads as .txt — open in Word (File → Open) or any text editor.</p>', unsafe_allow_html=True)
        st.download_button("⬇  Download Report (.txt)", data=report_text.encode("utf-8"),
                           file_name=fname, mime="text/plain", use_container_width=True)
        st.markdown(f"""
        <p style="font-size:0.77rem;color:rgba(232,228,220,0.3);line-height:1.9;margin-top:10px;">
        System: <b style="color:rgba(232,228,220,0.55);">{meta.get('system','—')}</b> &nbsp;·&nbsp;
        Date: <b style="color:rgba(232,228,220,0.55);">{datetime.today().strftime('%B %d, %Y')}</b>
        </p>
        """, unsafe_allow_html=True)

    col_r, _ = st.columns([1, 4])
    with col_r:
        if st.button("↺  Start Over", use_container_width=True):
            st.session_state.step = 0
            st.session_state.responses = {}
            st.rerun()

    st.markdown("""
    <p style="font-size:0.72rem;color:rgba(232,228,220,0.15);text-align:center;font-family:'DM Mono',monospace;letter-spacing:0.5px;padding:20px 0 8px;">
    Built by Khushi Rana &nbsp;·&nbsp; AI Governance Audit Framework &nbsp;·&nbsp; Educational purposes only
    </p>
    """, unsafe_allow_html=True)

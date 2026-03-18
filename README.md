# AI Governance Audit Framework

An interactive tool for evaluating AI systems against structured governance criteria — covering transparency, fairness, accountability, security, and privacy. Generates a scored risk assessment and downloadable audit report.

**[→ View Live Tool](https://ai-governance-audit-9abmdtb9a4zsyrffdqzkbc.streamlit.app/)** <!-- replace with your Streamlit URL -->

---

## The Problem This Addresses

AI systems are being deployed faster than governance frameworks can keep up. Organizations face real liability under emerging regulation — the EU AI Act, NIST AI RMF, and ISO 42001 — but most teams lack a structured way to assess their own systems against these standards.

This tool operationalizes those frameworks into a practical audit workflow: input an AI system, answer 25 governance questions across five domains, and receive a scored risk assessment with prioritized findings and recommendations.

---

## What It Does

A user (an auditor, risk officer, or governance lead) enters details about the AI system under review, then works through five governance domains derived from real regulatory frameworks:

| Domain | Weight | Key Risk Areas |
|---|---|---|
| Transparency & Explainability | 20% | Model cards, decision explanations, disclosure |
| Fairness & Non-Discrimination | 22% | Bias testing, demographic parity, legal compliance |
| Accountability & Oversight | 22% | Named ownership, audit logs, human-in-the-loop |
| Security & Robustness | 18% | Adversarial testing, drift monitoring, access controls |
| Privacy & Data Governance | 18% | GDPR/PIPEDA compliance, data minimization, PIA |

Each question is tagged by severity (Critical / High / Medium / Low). Responses feed into a weighted scoring model that produces:

- An **overall governance score** (0–100) with a risk rating
- A **radar chart** showing coverage across all five domains
- A **prioritized findings list** — gaps and partial controls, sorted by severity
- **Concrete recommendations** grounded in regulatory language
- A **downloadable audit report** (.txt) with full details

---

## Framework Basis

The question set and domain structure are drawn from:

- **EU AI Act (2024)** — transparency, human oversight, and high-risk AI requirements
- **NIST AI Risk Management Framework 1.0** — Govern, Map, Measure, Manage functions
- **ISO/IEC 42001** — AI management system standard
- **OECD AI Principles** — accountability and explainability norms

---

## Why I Built This

Most AI governance work happens in policy documents and academic papers. This project was an attempt to translate that into something *usable* — a tool that forces structured thinking about what responsible AI deployment actually requires in practice.

It also reflects my core interest: the gap between how AI systems are built and how they *should* be governed, especially in high-stakes sectors like financial services, healthcare, and public administration.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web app framework |
| Plotly | Radar and bar charts |

No external data required — the framework logic is entirely self-contained.

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/ks-rana/ai-governance-audit.git
cd ai-governance-audit

# 2. Install dependencies
pip install streamlit plotly pandas

# 3. Run the app
streamlit run ai_governance_audit.py
```

---

## Limitations & Scope

This tool is designed for educational and portfolio purposes. It is not a substitute for a formal regulatory compliance review or legal advice. The scoring model reflects reasonable governance weights but has not been validated against any specific regulatory body's methodology.

A real-world audit would involve document review, stakeholder interviews, technical testing, and legal analysis — this tool models the *structure* of that process, not its full depth.

---

## About

Built by **Khushi Rana** — studying the intersection of Psychology, AI Governance, and data-driven strategy.

[LinkedIn](https://www.linkedin.com/in/khushi-rana-00764223a) · [Personal Website](https://khushi-rana-website.vercel.app/) · [Retail Dashboard Project](https://github.com/ks-rana/retail-sales-dashboard)

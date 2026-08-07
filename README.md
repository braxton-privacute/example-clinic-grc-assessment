# Example Family Clinic — GRC Findings (SCF-mapped)

> **This scenario is fictional.** "Example Family Clinic" is not a real
> organization, and the findings below describe no real practice, patient, or
> incident. The scenario was constructed to exercise the assessment pipeline.
> The methodology, control mapping, scoring, and tooling are my own work.

Structured findings from a post-breach risk assessment of a small outpatient
clinic, mapped to the Secure Controls Framework (SCF 2026.2).

## What this solves

Risk findings are usually written as prose and mapped to frameworks by hand,
which makes them slow to review and easy to get wrong — a mistyped control ID
looks the same as a correct one. This treats findings as structured data and
validates every control ID against the live SCF catalog before any report is
generated, so a bad ID stops the run instead of shipping in a report.

## What's inside

- `data/findings.json` — the findings as structured data
- `run_pipeline.py` — validates control IDs, enriches HIPAA refs, scores, reports
- `read_findings.py` — loads and prints the findings
- `generate_report.py` — renders the Markdown risk matrix
- `narrative.py` — optional AI narrative layer (see below)

Each finding carries: threat, vulnerability, verified SCF control IDs,
likelihood/impact/risk score, HIPAA references, and remediation.

## How to run

```bash
python run_pipeline.py
```

Point it at a different findings file by passing a path:

```bash
python run_pipeline.py data/other-findings.json
```

The pipeline fetches the SCF catalog, validates every control ID, and **stops
before writing anything** if any ID is invalid.

## The AI narrative layer is optional

`narrative.py` generates a written summary grounded in an explicit
verified-facts block. It is **off by default** — the rest of the pipeline runs
without it and without an API key. To enable it, set `USE_REAL_AI = True` and
provide an `ANTHROPIC_API_KEY` environment variable.

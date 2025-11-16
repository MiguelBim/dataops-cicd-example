# DataOps CI/CD Example (GitHub Actions)

A minimal, production-style example of a **DataOps CI/CD pipeline** you can fork and reference in your proposal.

## What this repo shows
- **Multi-env CI** (dev, stage) on pull requests and main pushes
- **Gates** for promotion to **prod** via a protected environment (manual approval)
- **Quality checks**: formatting/lint (ruff), unit tests (pytest), and data quality checks (Great Expectations)
- **Simple ETL job** reading CSV → transform → write CSV
- **Artifacts** saved in CI for inspection
- **Environment variables** for configuration (no hardcoded secrets)

## Quick start (local)
```bash
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r pipeline/requirements.txt
python pipeline/etl_job.py --input data/input.csv --output data/output.csv
pytest -q
great_expectations checkpoint run simple_checkpoint
```

## CI Environments
- **dev** / **stage**: run on PRs and pushes
- **prod**: runs on release tags; requires manual approval (use GitHub Environments protection)

## Repo layout
```
.github/workflows/dataops-ci.yml   # CI/CD pipeline
pipeline/etl_job.py                # Simple ETL job
pipeline/requirements.txt          # Python deps
tests/test_etl_job.py              # Unit tests
great_expectations/                # DQ suite + checkpoint
data/input.csv                     # Sample input
```

## Secrets / Config
Set these as **GitHub Actions Secrets** or **Environment variables** in the relevant environment:
- `DATA_BUCKET` (optional): where to persist outputs in real pipelines
- `ALERT_SLACK_WEBHOOK` (optional): for alerts on failure

> This repo is intentionally simple; replace the ETL and DQ steps with dbt, Spark, or your orchestration of choice (Airflow/Dagster/Prefect). The pipeline pattern remains the same.

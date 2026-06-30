# dockerfile-risk-scan

**Runbook.** Scan Dockerfile snippets for root users, latest tags, and unpinned installs.

## Prerequisites

Container risks often start in simple Dockerfile shortcuts. This CLI catches common issues before image builds ship.

## Procedure

`dockerfile-risk-scan` accepts Dockerfile or container build notes in text, JSON, JSONL, or CSV form.

## Expected Result

```bash
python -m pip install -e ".[dev]"
dockerfile-risk-scan examples/sample.txt
dockerfile-risk-scan examples/sample.txt --json --fail-on medium
```

## Troubleshooting

| Rule | Severity | Meaning |
|---|---:|---|
| `latest-tag` | high | base image uses latest tag |
| `root-user` | medium | container runs as root |
| `unpinned-pip` | low | pip dependency may be unpinned |

## Ownership

```bash
ruff check .
pytest
python -m dockerfile_risk_scan --help
```

License: MIT

### Example Input

```text
FROM python:latest RUN pip install flask USER root
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the dockerfile-risk-scan policy surface explicit.

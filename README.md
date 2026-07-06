<img src="assets/readme-cover.svg" alt="Dockerfile Risk Scan cover" width="100%" />

# Dockerfile Risk Scan

Scan Dockerfile snippets for root users, latest tags, and unpinned installs.

![stack](https://img.shields.io/badge/stack-Python-dc2626?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-7c3aed?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-0891b2?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-b45309?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `dockerfile-risk-scan` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `latest-tag` | high | base image uses latest tag |
| `root-user` | medium | container runs as root |
| `unpinned-pip` | low | pip dependency may be unpinned |

## Command line

```bash
python -m pip install -e ".[dev]"
dockerfile-risk-scan examples/sample.txt
dockerfile-risk-scan examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
FROM python:latest RUN pip install flask USER root
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```

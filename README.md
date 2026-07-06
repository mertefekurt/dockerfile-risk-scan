# Dockerfile Risk Scan

Scan Dockerfile snippets for root users, latest tags, and unpinned installs. In practice it is a narrow guardrail for deployment, cloud, CI, config, and operational safety checks: one command, a concrete report, and very little ceremony.

<img src="assets/readme-cover.svg" alt="Dockerfile Risk Scan cover" width="100%" />

## Review checklist

- [ ] base image uses latest tag (`latest-tag`, high)
- [ ] container runs as root (`root-user`, medium)
- [ ] pip dependency may be unpinned (`unpinned-pip`, low)

## Command path

```bash
git clone https://github.com/mertefekurt/dockerfile-risk-scan.git
cd dockerfile-risk-scan
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
dockerfile-risk-scan examples/sample.txt
dockerfile-risk-scan examples/sample.txt --json
```

## Fixture worth keeping

```text
FROM python:latest RUN pip install flask USER root
```

## Files I look at first

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```

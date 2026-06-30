from __future__ import annotations

from dockerfile_risk_scan.models import Rule

PROJECT_NAME = 'dockerfile-risk-scan'
SUMMARY = 'Scan Dockerfile snippets for root users, latest tags, and unpinned installs.'
SAMPLE_RISK = 'FROM python:latest RUN pip install flask USER root'
SAMPLE_CLEAN = 'FROM python:3.11-slim RUN pip install flask==3.0.0 USER app'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='latest-tag',
        severity='high',
        pattern='\\bFROM\\b.+:latest\\b',
        message='base image uses latest tag',
        recommendation='Pin base image version or digest.',
    ),
    Rule(
        code='root-user',
        severity='medium',
        pattern='\\bUSER\\s+root\\b',
        message='container runs as root',
        recommendation='Use a non-root runtime user.',
    ),
    Rule(
        code='unpinned-pip',
        severity='low',
        pattern='\\bpip install\\s+[a-zA-Z0-9_-]+(\\s|$)',
        message='pip dependency may be unpinned',
        recommendation='Pin runtime dependencies or use a lockfile.',
    ),
)

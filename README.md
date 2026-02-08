# FastAPI + Docker + CI/CD + Trivy

Production FastAPI app con GitHub Actions: tests, Docker build, security scan.

## Quickstart
docker-compose up

## Pipeline Status
[![CI/CD](https://github.com/zafdrive/fastapi-docker-cicd/actions/workflows/cicd.yml/badge.svg)](https://github.com/zafdrive/fastapi-docker-cicd/actions)

## Local Demo
\`\`\`bash
docker compose up
curl http://localhost:8000/
\`\`\`

## Features
- ✅ FastAPI production-ready
- ✅ Pytest automated tests
- ✅ Docker multi-stage build
- ✅ Trivy security scanning
- ✅ GitHub Actions CI/CD
- ✅ Auto-deploy GHCR

## Status Badges
[![Tests](https://github.com/zafdrive/fastapi-docker-cicd/actions/workflows/cicd.yml/badge.svg)](https://github.com/zafdrive/fastapi-docker-cicd/actions)
[![Security](https://github.com/zafdrive/fastapi-docker-cicd/security/badge.svg)](https://github.com/zafdrive/fastapi-docker-cicd/security)

## Pull Image
docker pull ghcr.io/zafdrive/fastapi-docker-cicd:latest

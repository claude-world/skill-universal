---
name: github-analyzer
description: Analyze GitHub repositories for tech stack, dependencies, and metrics
version: 1.0.0
author: Claude World
triggers:
  - "analyze repo"
  - "github analysis"
  - "repo stats"
tools:
  - WebSearch
  - WebFetch
  - Read
  - Grep
---

## GitHub Analyzer Skill

Analyze GitHub repositories to extract tech stack, dependencies, metrics, and more.

## Execution Steps

### 1. Repository Metadata
Stars, forks, issues, license, topics

### 2. Language Analysis
Primary language and percentages

### 3. Dependency Analysis
Package dependencies from package.json, requirements.txt, go.mod, etc.

### 4. Commit Activity
Recent commits, contributors, activity trends

### 5. Documentation Quality
README, CONTRIBUTING, LICENSE, docs folder

### 6. CI/CD Analysis
GitHub Actions, Travis CI, Docker, etc.

## Output Format

```markdown
# GitHub Analysis: {owner}/{repo}

## Overview
- **Stars**: {count}
- **Forks**: {count}
- **License**: {license}

## Tech Stack
- **Languages**: {list}
- **Dependencies**: {key deps}

## Activity
- **Commits**: {count}
- **Contributors**: {count}

## Recommendations
{based on analysis}
```

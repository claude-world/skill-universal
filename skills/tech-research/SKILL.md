---
name: tech-research
description: Research any technology topic and generate comprehensive reports
version: 1.0.0
author: Claude World
triggers:
  - "research"
  - "study"
  - "analyze"
tools:
  - WebSearch
  - WebFetch
  - Read
  - Write
  - Grep
---

## Tech Research Skill

This Skill researches any technology topic by aggregating data from multiple sources.

## Execution Steps

### 1. Web Research
Search "[topic] tutorial 2026", "[topic] documentation", "[topic] best practices"

### 2. GitHub Analysis
Query [topic]/[topic] repository, extract stars/forks/languages/activity

### 3. Community Monitoring
Check recent discussions, trending issues, community feedback

### 4. Documentation Review
Read official docs, extract key features and version info

### 5. Report Generation
Create comprehensive report with overview, findings, stats, insights, resources

## Output Format

```markdown
# [Topic] Research Report

## Overview
[Brief description]

## Key Findings
- Finding 1
- Finding 2

## GitHub Stats
- Repository: [url]
- Stars: [count]
- Languages: [list]

## Community Insights
- Popular discussions
- Common issues

## Resources
- Official Docs: [link]
- Tutorials: [links]

## Recommendations
[Based on findings]
```

## Tool Mapping

### Claude Code
WebSearch, WebFetch, Read, Write, Grep

### Agent SDK (Python)
```python
tools = {
    'web_search': WebSearchTool(),
    'web_fetch': WebFetchTool(),
    'read': ReadTool(),
    'write': WriteTool(),
    'grep': GrepTool()
}
```

### OpenClaw (TypeScript)
```typescript
const tools = {
    'web-search': webSearchTool,
    'web-fetch': webFetchTool,
    'read': readTool,
    'write': writeTool,
    'grep': grepTool
};
```

---
name: customer-support
description: Intelligent customer support with multi-source knowledge aggregation
version: 1.0.0
author: Claude World
triggers:
  - "support"
  - "help"
  - "customer service"
tools:
  - WebSearch
  - WebFetch
  - Read
---

## Customer Support Skill

Aggregate knowledge from multiple sources to provide intelligent customer support.

## Execution Steps

### 1. Query Classification
Technical, Billing/Account, Feature Request, General

### 2. Source Selection
- Technical → Knowledge Base + GitHub Issues
- Billing → FAQ + CRM
- Feature → GitHub Discussions
- General → FAQ + Website

### 3. Knowledge Retrieval
Query selected sources in parallel

### 4. Answer Synthesis
Combine, rank, deduplicate, format

### 5. Follow-up Actions
Log query, identify gaps, suggest improvements

## Output Format

```markdown
## Answer
[comprehensive answer based on all sources]

## Information Sources
- **Knowledge Base**: [link]
- **GitHub Issues**: #[number]
- **FAQ**: [link]

## Related Topics
- {related topic 1}
- {related topic 2}

## Need More Help?
{contact information or next steps}
```

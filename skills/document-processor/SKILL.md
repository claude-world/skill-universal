---
name: document-processor
description: Process PDF, Word, Markdown, and other document formats
version: 1.0.0
author: Claude World
triggers:
  - "process document"
  - "extract text"
  - "parse document"
tools:
  - Read
  - Write
  - Bash
---

## Document Processor Skill

Process various document formats and extract structured information.

## Execution Steps

### 1. Format Detection
Check file extension and MIME type

### 2. Content Extraction
- PDF: Use pdftotext or PyPDF2
- Word: Use pandoc or python-docx
- Markdown: Direct read
- HTML: Use pandoc or lynx

### 3. Structure Analysis
Identify headings, lists, tables, metadata

### 4. Output Generation
Plain text, Markdown, or JSON

## Output Format

```markdown
# Document Summary

**Title**: [extracted title]
**Author**: [if available]
**Date**: [if available]

## Content
[Extracted text content]

## Metadata
- Pages: [count]
- Format: [type]
- Encoding: [encoding]
```

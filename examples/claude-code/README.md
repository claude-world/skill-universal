# Using Skills with Claude Code

Claude Code is the simplest way to use Skills - just create SKILL.md files!

## Quick Start

### 1. Create Your Skill

```bash
# In your project root
mkdir -p .claude/skills/my-skill
```

### 2. Create SKILL.md

```markdown
---
name: my-skill
description: My custom skill
triggers:
  - "my skill"
tools:
  - WebSearch
  - Read
  - Write
---

## What This Skill Does

Describe what your skill does here.

## Execution Steps

1. Step 1
2. Step 2
3. Step 3
```

### 3. Use Your Skill

```bash
# In your project directory
claude -p "Use my skill to do something"
```

## Example: Research Skill

### Step 1: Copy Example Skill

```bash
# Copy tech-research skill to your project
cp -r skill-universal/skills/tech-research .claude/skills/
```

### Step 2: Use It

```bash
claude -p "Use tech-research to study OpenClaw"
```

## Example: Document Processor

### Step 1: Copy Skill

```bash
cp -r skill-universal/skills/document-processor .claude/skills/
```

### Step 2: Process Documents

```bash
claude -p "Use document-processor to extract text from report.pdf"
```

## Best Practices

### 1. Keep Skills Focused

Each Skill should do one thing well.

**Good**:
```markdown
---
name: pdf-extractor
description: Extract text from PDF files
tools: [Bash, Read]
---
```

**Bad**:
```markdown
---
name: everything
description: Does everything
tools: [all tools]
---
```

### 2. Use Clear Names

```markdown
---
name: github-analyzer        # Clear
description: Analyze GitHub repos
---

---
name: ga                    # Not clear
description: Does stuff
---
```

### 3. Document Your Skills

Include:
- What it does
- How to use it
- Examples
- Tool requirements

## Advanced Usage

### Chain Skills

```bash
# Use multiple skills in sequence
claude -p "Use tech-research to study Docker, then use document-processor to create a summary"
```

### Custom Tools

Skills can use MCP (Model Context Protocol) tools:

```markdown
---
tools:
  - WebSearch
  - my-custom-mcp-tool  # Your MCP tool
---
```

## Tips

1. **Start Simple**: Begin with basic Skills
2. **Iterate**: Improve based on usage
3. **Test**: Verify Skills work as expected
4. **Share**: Contribute useful Skills to community

## See Also

- [Skill Format Documentation](https://claude-world.com/docs/universal-skill-loader)
- [Claude Code Skills Guide](https://docs.anthropic.com/claude-code/skills)

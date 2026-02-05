# Contributing to Skill Universal

Thank you for your interest in contributing to Skill Universal!

## How to Contribute

### 1. Add a New Skill

Create a new Skill in the `skills/` directory:

```bash
skills/your-skill/
├── SKILL.md          # Required: Skill definition
├── examples/        # Optional: Example inputs/outputs
└── tests/           # Optional: Test cases
```

### 2. Improve Existing Skills

- Fix bugs
- Add features
- Improve documentation
- Add translations

### 3. Extend Loaders

- Support new platforms
- Improve performance
- Add features
- Fix bugs

## Skill Format

All Skills must follow the SKILL.md format:

```markdown
---
name: your-skill
description: What this skill does
version: 1.0.0
author: Your Name
triggers:
  - "trigger1"
  - "trigger2"
tools:
  - Tool1
  - Tool2
---

## Skill Description

Detailed explanation of what this skill does and how to use it.

## Execution Steps

1. Step 1 description
2. Step 2 description
3. ...

## Examples

### Example 1
Input: ...
Output: ...

## Tool Mapping

### Claude Code
- Tool1 → Tool1

### Agent SDK
```python
tools = {'tool1': Tool1()}
```

### OpenClaw
```typescript
const tools = { 'tool1': tool1 }
```
```

## Development Setup

### Python Development

```bash
cd loaders/python
pip install -r requirements.txt
pytest
```

### TypeScript Development

```bash
cd loaders/typescript
npm install
npm run build
npm test
```

## Testing

Add tests for your Skill in `tests/`:

```python
# tests/test_your_skill.py
from skill_universal import SkillLoader

def test_load_your_skill():
    loader = SkillLoader()
    config = loader.load('skills/your-skill/SKILL.md')
    assert config.name == 'your-skill'
```

## Documentation

Update documentation in `docs/`:
- English: `docs/en/`
- 繁體中文: `docs/zh-tw/`
- 日本語: `docs/ja/`

## Pull Request Process

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Add tests
5. Update documentation
6. Submit a pull request

## Code Style

- **Python**: Follow PEP 8
- **TypeScript**: Follow ESLint rules
- **Markdown**: Use 80-character line length where possible

## Questions?

Feel free to open an issue for discussion!

---

**Happy Coding! 🚀**

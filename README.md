# Skill Universal 🌍

> Write your Skill once, run everywhere - from Claude Code to Agent SDK, OpenClaw, and beyond.

**Skill Universal** demonstrates how declarative Skills (Claude Code Skills format) can be loaded and executed across different Agent platforms.

## 🌟 Why This Matters

### The N*N Problem
Traditional agent development: `N tools = N! possible workflow combinations`

### The Solution
Skills provide intelligent aggregation: `N tools + 1 router = all possible combinations`

## 🚀 Quick Start

### For Claude Code Users
Just create a `.claude/skills/my-skill/SKILL.md` file!

### For Agent SDK Users (Python)
```python
from skill_universal import SkillLoader

loader = SkillLoader()
skill = loader.load("skills/my-skill/SKILL.md")
agent = skill.to_agent_sdk()
```

### For OpenClaw Users (TypeScript)
```typescript
import { SkillLoader } from 'skill-universal';

const loader = new SkillLoader();
const skill = await loader.load('skills/my-skill/SKILL.md');
const openclawSkill = skill.to_openclaw();
```

## 📚 What's Included

### Example Skills
1. **Tech Research** - Research any technology topic
2. **Document Processor** - Process PDF/Word/Markdown
3. **GitHub Analyzer** - Analyze repositories
4. **Customer Support** - Intelligent support aggregation

### Loaders
- **Python** - Load Skills in Python/Agent SDK
- **TypeScript** - Load Skills in TypeScript/Node.js/OpenClaw

## 📖 Documentation

See [docs/](docs/) for detailed documentation in English, 繁體中文, and 日本語.

## 🏗️ Project Structure

```
skill-universal/
├── skills/           # Example Skills (SKILL.md format)
├── loaders/          # Platform-specific loaders
│   ├── python/       # Python/Agent SDK loader
│   └── typescript/   # TypeScript loader
├── examples/         # Usage examples
│   ├── claude-code/
│   ├── agent-sdk/
│   └── openclaw/
└── docs/            # Documentation (EN/ZH-TW/JA)
```

## 💡 Use Cases

- Research automation across web, GitHub, and community
- Document processing for PDF/Word/Markdown
- Repository analysis for tech stack and dependencies
- Customer support with multi-source knowledge aggregation

## 🔧 Installation

```bash
# Python
pip install skill-universal

# TypeScript
npm install skill-universal
```

## 📝 License

MIT License - see [LICENSE](LICENSE)

## 🙏 Acknowledgments

- [Claude Code](https://docs.anthropic.com/claude-code) - Skills format inspiration
- [Anthropic Agent SDK](https://docs.anthropic.com/claude-code/agents) - Python/TypeScript SDKs
- [OpenClaw](https://docs.openclaw.dev) - Open-source agent platform
- [Claude World](https://claude-world.com) - Community and documentation

---

**Made with ❤️ by the Claude World Community**

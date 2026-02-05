# Skill Universal 🌍

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)](https://www.typescriptlang.org/)
[![CI/CD](https://github.com/claude-world/skill-universal/actions/workflows/ci.yml/badge.svg)](https://github.com/claude-world/skill-universal/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/claude-world/skill-universal/branch/main/graph/badge.svg)](https://codecov.io/gh/claude-world/skill-universal)

> **Write your Skill once, run everywhere** - from Claude Code to Agent SDK, OpenClaw, and beyond.

**Skill Universal** demonstrates how declarative Skills (Claude Code Skills format) can be loaded and executed across different Agent platforms.

## 🌟 Why This Matters

### The N×N Problem

Traditional agent development: `N tools = N! possible workflow combinations`

When you have N tools, creating agents for every possible workflow becomes unmanageable.

### The Solution

Skills provide intelligent aggregation: `N tools + 1 router = all possible combinations`

Skills act as:
- **Tool Aggregators** - Combine existing capabilities
- **Decision Engines** - Replace human judgment with AI decisions
- **Execution Coordinators** - Optimize workflows dynamically

## 🚀 Quick Start

### For Claude Code Users

Just create a `.claude/skills/my-skill/SKILL.md` file!

```markdown
---
name: research
description: Research expert
triggers:
  - "research"
  - "study"
tools:
  - WebSearch
  - WebFetch
---

## Research any topic efficiently...

### 1. Search
Search for "[topic] tutorial 2026"

### 2. Fetch Documentation
Read official documentation

### 3. Summarize
Create comprehensive summary
```

### For Agent SDK Users (Python)

```python
from skill_universal import SkillLoader

loader = SkillLoader()
skill = loader.load("skills/my-skill/SKILL.md")
agent = skill.to_agent_sdk()

# Use with Anthropic Agent SDK
# agent.create() returns properly configured agent
```

### For OpenClaw Users (TypeScript)

```typescript
import { SkillLoader } from 'skill-universal';

const loader = new SkillLoader();
const skill = await loader.load('skills/my-skill/SKILL.md');
const openclawSkill = skill.to_openclaw();

// Deploy to OpenClaw platform
// openclawSkill contains proper tool mappings
```

## 📚 What's Included

### Example Skills

| Skill | Description | Tools Used |
|-------|-------------|------------|
| **Tech Research** | Research any technology topic | WebSearch, WebFetch, Read, Write, Grep |
| **Document Processor** | Process PDF/Word/Markdown | Read, Write, Bash |
| **GitHub Analyzer** | Analyze repositories | WebSearch, WebFetch, Read, Grep |
| **Customer Support** | Multi-source support aggregation | WebSearch, WebFetch, Read |

### Loaders

- **Python** (`loaders/python/skill_loader.py`) - Load Skills in Python/Agent SDK
- **TypeScript** (`loaders/typescript/SkillLoader.ts`) - Load Skills in TypeScript/Node.js/OpenClaw

## 📦 Installation

### From PyPI (Python)

```bash
pip install skill-universal
```

### From npm (TypeScript)

```bash
npm install skill-universal
```

### From Source

```bash
git clone https://github.com/claude-world/skill-universal.git
cd skill-universal

# Python
pip install -e .

# TypeScript
npm install
npm run build
```

## 💡 Use Cases

### 1. Research Automation
Automate research across web, GitHub, and community discussions.

### 2. Document Processing
Process PDF, Word, and Markdown documents with consistent interface.

### 3. Repository Analysis
Analyze GitHub repositories for tech stack, dependencies, and metrics.

### 4. Customer Support
Aggregate knowledge from multiple sources for intelligent support.

## 🏗️ Project Structure

```
skill-universal/
├── skills/           # Example Skills (SKILL.md format)
│   ├── tech-research/
│   ├── document-processor/
│   ├── github-analyzer/
│   └── customer-support/
├── loaders/          # Platform-specific loaders
│   ├── python/       # Python/Agent SDK loader
│   │   ├── skill_loader.py
│   │   └── tests/
│   └── typescript/   # TypeScript loader
│       ├── SkillLoader.ts
│       └── tests/
├── examples/         # Usage examples
│   ├── claude-code/
│   ├── agent-sdk/
│   └── openclaw/
├── tests/            # Integration tests
├── docs/             # Documentation (EN/ZH-TW/JA)
├── .github/          # GitHub Actions, issue templates
├── pyproject.toml    # Python packaging
├── package.json      # TypeScript packaging
└── README.md
```

## 🧪 Testing

```bash
# Python tests
pytest tests/

# TypeScript tests
npm test

# All tests
npm run test:all
```

## 📖 Documentation

- [English](docs/README.md)
- [繁體中文](docs/README-zh-tw.md)
- [日本語](docs/README-ja.md)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📊 Status

[![GitHub Stars](https://img.shields.io/github/stars/claude-world/skill-universal?style=social)](https://github.com/claude-world/skill-universal/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/claude-world/skill-universal?style=social)](https://github.com/claude-world/skill-universal/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/claude-world/skill-universal)](https://github.com/claude-world/skill-universal/issues)

## 🗺️ Roadmap

- [x] Core skill loading (Python, TypeScript)
- [x] Example skills
- [x] Claude Code format support
- [x] Agent SDK format support
- [x] OpenClaw format support
- [ ] PyPI package publishing
- [ ] npm package publishing
- [ ] More platform support (LangChain, LlamaIndex, etc.)
- [ ] Skill marketplace
- [ ] Web UI for skill creation

## 📝 License

MIT License - see [LICENSE](LICENSE)

## 🙏 Acknowledgments

- [Claude Code](https://docs.anthropic.com/claude-code) - Skills format inspiration
- [Anthropic Agent SDK](https://docs.anthropic.com/claude-code/agents) - Python/TypeScript SDKs
- [OpenClaw](https://docs.openclaw.dev) - Open-source agent platform
- [Claude World](https://claude-world.com) - Community and documentation

## 🔗 Links

- [Documentation](https://github.com/claude-world/skill-universal/tree/main/docs)
- [Examples](https://github.com/claude-world/skill-universal/tree/main/examples)
- [Issues](https://github.com/claude-world/skill-universal/issues)
- [Discussions](https://github.com/claude-world/skill-universal/discussions)

---

**Made with ❤️ by the [Claude World Community](https://claude-world.com)**

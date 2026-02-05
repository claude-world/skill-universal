# Contributing to Skill Universal

Thank you for your interest in contributing to Skill Universal! This document provides guidelines and instructions for contributing.

## 🚀 Quick Start for Contributors

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`npm run test:all` or `pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📋 Development Setup

### Prerequisites

- Python 3.9+
- Node.js 18+
- Git

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/skill-universal.git
cd skill-universal

# Set up Python environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e ".[dev]"

# Set up TypeScript environment
npm install

# Run tests to verify setup
npm run test:all
```

## 🧪 Testing

### Python Tests

```bash
# Run all Python tests
pytest loaders/python/tests/

# Run with coverage
pytest --cov=skill_universal --cov-report=html

# Run specific test
pytest loaders/python/tests/test_skill_loader.py::test_load_skill
```

### TypeScript Tests

```bash
# Run all TypeScript tests
npm test

# Run with coverage
npm run test:coverage

# Watch mode
npm test -- --watch
```

### Run All Tests

```bash
npm run test:all
```

## 📝 Code Style

### Python

We use:
- **Black** for formatting
- **Ruff** for linting
- **mypy** for type checking

```bash
# Format code
ruff format loaders/python/

# Lint code
ruff check loaders/python/

# Type check
mypy loaders/python/skill_loader.py
```

### TypeScript

We use:
- **Prettier** for formatting
- **ESLint** for linting
- **TypeScript** for type checking

```bash
# Format code
npm run format

# Lint code
npm run lint

# Type check
npm run typecheck
```

## 🎯 Types of Contributions

### Bug Fixes

1. Check existing [Issues](https://github.com/claude-world/skill-universal/issues)
2. Create an issue or comment on existing one
3. Fix the bug
4. Add tests to prevent regression

### New Features

1. Open an issue to discuss the feature first
2. Get feedback from maintainers
3. Implement the feature
4. Add tests and documentation

### Documentation

We welcome documentation improvements:
- Fixing typos
- Adding examples
- Improving explanations
- Translating documentation

### Example Skills

Contributing new example skills is a great way to help others learn:

1. Create a new directory in `skills/your-skill/`
2. Add a `SKILL.md` file
3. Follow the skill format
4. Add usage examples in `examples/`

## 📧 Pull Request Guidelines

### PR Title

Use conventional commits format:

- `feat: add support for LangChain`
- `fix: correct tool mapping for Bash`
- `docs: improve API documentation`
- `test: add tests for skill validation`

### PR Description

Include:
- **What** changes were made
- **Why** the changes are needed
- **How** to test the changes
- **Related issues** (e.g., `Fixes #123`)

### PR Checklist

Before submitting, ensure:
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] PR description is complete

## 🏗️ Project Structure

```
skill-universal/
├── skills/           # Example skills (SKILL.md format)
├── loaders/
│   ├── python/       # Python implementation
│   └── typescript/   # TypeScript implementation
├── examples/         # Usage examples
├── tests/            # Integration tests
├── docs/             # Documentation
└── .github/          # GitHub workflows
```

## 🤝 Code of Conduct

Be respectful, inclusive, and constructive. We're all here to build something amazing together.

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

## 📚 Adding Support for New Platforms

To add support for a new agent platform:

1. Create a new converter method
2. Add tool mappings
3. Add tests
4. Add documentation
5. Add examples

## 🐛 Reporting Bugs

When reporting bugs, include:
- Python/Node.js version
- Skill Universal version
- Steps to reproduce
- Expected vs actual behavior
- Error messages and stack traces

## 💡 Feature Requests

For feature requests:
- Explain the use case
- Describe desired behavior
- Provide examples if possible
- Consider if it fits the project scope

## 📖 Documentation Style

- Use clear, concise language
- Provide code examples
- Include expected output
- Link to related docs
- Use consistent terminology

## 🎓 Getting Help

- Check existing [Issues](https://github.com/claude-world/skill-universal/issues)
- Start a [Discussion](https://github.com/claude-world/skill-universal/discussions)
- Read the [Documentation](https://github.com/claude-world/skill-universal/tree/main/docs)

## 🌟 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Celebrated in our community

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Skill Universal! 🎉

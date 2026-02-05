# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of Skill Universal
- Python loader with support for Claude Code Skills format
- TypeScript loader with support for Claude Code Skills format
- 4 example skills: Tech Research, Document Processor, GitHub Analyzer, Customer Support
- Conversion to Agent SDK format (Python)
- Conversion to OpenClaw format (TypeScript)
- GitHub Actions CI/CD pipeline
- Comprehensive documentation in English, Traditional Chinese, and Japanese
- pyproject.toml for Python packaging
- package.json for TypeScript packaging

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

## [0.1.0] - 2026-02-05

### Added
- Initial public release
- Core skill loading functionality
- Cross-platform format conversion
- Example skills and documentation
- CI/CD pipeline

---

## Release Process

1. Update version in `pyproject.toml` and `package.json`
2. Update this `CHANGELOG.md`
3. Create git tag: `git tag v0.1.0`
4. Push tag: `git push origin v0.1.0`
5. GitHub Actions will automatically publish to PyPI and npm

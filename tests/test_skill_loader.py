"""
Tests for Skill Universal - Python Loader
"""

import os
import json
import tempfile
from pathlib import Path

import pytest
from skill_universal import SkillLoader, SkillConfig


class TestSkillConfig:
    """Test SkillConfig class"""

    def test_skill_config_creation(self):
        """Test creating a SkillConfig object"""
        metadata = {
            'name': 'test-skill',
            'description': 'A test skill',
            'version': '1.0.0',
            'tools': ['WebSearch', 'WebFetch']
        }
        content = "## Test Content"

        config = SkillConfig(metadata, content)

        assert config.name == 'test-skill'
        assert config.description == 'A test skill'
        assert config.version == '1.0.0'
        assert config.tools == ['WebSearch', 'WebFetch']
        assert config.content == "## Test Content"

    def test_skill_config_defaults(self):
        """Test SkillConfig with missing optional fields"""
        metadata = {'name': 'test', 'description': 'Test'}
        config = SkillConfig(metadata, "content")

        assert config.version == '1.0.0'
        assert config.author == ''
        assert config.triggers == []
        assert config.tools == []

    def test_skill_config_repr(self):
        """Test SkillConfig string representation"""
        config = SkillConfig({'name': 'test', 'version': '2.0.0'}, "")
        assert repr(config) == "SkillConfig(name=test, version=2.0.0)"


class TestSkillLoader:
    """Test SkillLoader class"""

    @pytest.fixture
    def loader(self):
        """Create a SkillLoader instance"""
        return SkillLoader()

    @pytest.fixture
    def sample_skill(self):
        """Create a sample skill file"""
        skill_content = """---
name: research-skill
description: Research expert
version: 1.0.0
author: Test Author
triggers:
  - "research"
  - "study"
tools:
  - WebSearch
  - WebFetch
  - Read
---

## Research Steps

### 1. Search
Search for information

### 2. Analyze
Analyze results
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(skill_content)
            temp_path = f.name

        yield temp_path

        os.unlink(temp_path)

    def test_load_skill_file(self, loader, sample_skill):
        """Test loading a skill from file"""
        config = loader.load(sample_skill)

        assert config.name == 'research-skill'
        assert config.description == 'Research expert'
        assert config.version == '1.0.0'
        assert config.author == 'Test Author'
        assert config.triggers == ['research', 'study']
        assert config.tools == ['WebSearch', 'WebFetch', 'Read']
        assert '## Research Steps' in config.content

    def test_load_nonexistent_file(self, loader):
        """Test loading a file that doesn't exist"""
        with pytest.raises(FileNotFoundError):
            loader.load('/nonexistent/file.md')

    def test_load_invalid_frontmatter(self, loader):
        """Test loading a file with invalid frontmatter"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("---\ninvalid yaml\n---\ncontent")
            temp_path = f.name

        with pytest.raises(ValueError):
            loader.load(temp_path)

        os.unlink(temp_path)

    def test_load_missing_required_fields(self, loader):
        """Test loading a skill missing required fields"""
        # Missing name
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("---\ndescription: Test\n---\ncontent")
            temp_path = f.name

        with pytest.raises(ValueError, match="name"):
            loader.load(temp_path)

        os.unlink(temp_path)

        # Missing description
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("---\nname: test\n---\ncontent")
            temp_path = f.name

        with pytest.raises(ValueError, match="description"):
            loader.load(temp_path)

        os.unlink(temp_path)

    def test_load_string(self, loader):
        """Test loading a skill from a string"""
        skill_content = """---
name: string-test
description: Test from string
version: 1.0.0
---

Content here
"""
        config = loader.load_string(skill_content)

        assert config.name == 'string-test'
        assert config.description == 'Test from string'

    def test_to_agent_sdk(self, loader, sample_skill):
        """Test conversion to Agent SDK format"""
        config = loader.load(sample_skill)
        result = loader.to_agent_sdk(config)

        assert result['name'] == 'research-skill'
        assert result['description'] == 'Research expert'
        assert 'You are research-skill' in result['instructions']
        assert 'web_search' in result['tools']
        assert 'web_fetch' in result['tools']
        assert 'read_file' in result['tools']

    def test_to_openclaw(self, loader, sample_skill):
        """Test conversion to OpenClaw format"""
        config = loader.load(sample_skill)
        result = loader.to_openclaw(config)

        assert result['name'] == 'research-skill'
        assert result['description'] == 'Research expert'
        assert result['version'] == '1.0.0'
        assert 'metadata' in result
        assert result['metadata']['author'] == 'Test Author'
        assert len(result['skills']) == 1
        assert result['skills'][0]['name'] == 'execute'

    def test_to_langchain(self, loader, sample_skill):
        """Test conversion to LangChain format"""
        config = loader.load(sample_skill)
        result = loader.to_langchain(config)

        assert result['name'] == 'research-skill'
        assert result['description'] == 'Research expert'
        assert '{context}' in result['prompt_template']
        assert 'web_search' in result['tools']

    def test_to_claude_code(self, loader, sample_skill):
        """Test conversion back to Claude Code format"""
        config = loader.load(sample_skill)
        result = loader.to_claude_code(config)

        assert 'name: research-skill' in result
        assert 'description: Research expert' in result
        assert 'version: 1.0.0' in result
        assert 'author: Test Author' in result
        assert '## Research Steps' in result

    def test_custom_tool_map(self):
        """Test SkillLoader with custom tool map"""
        custom_map = {
            'WebSearch': 'my_search',
            'WebFetch': 'my_fetch',
        }
        loader = SkillLoader(tool_map=custom_map)

        skill_content = """---
name: test
description: Test
tools:
  - WebSearch
  - WebFetch
---
Content
"""
        config = loader.load_string(skill_content)
        result = loader.to_agent_sdk(config)

        assert result['tools'] == ['my_search', 'my_fetch']

    def test_unknown_tool(self, loader):
        """Test handling of unknown tools"""
        skill_content = """---
name: test
description: Test
tools:
  - UnknownTool
---
Content
"""
        config = loader.load_string(skill_content)
        result = loader.to_agent_sdk(config)

        # Unknown tools are passed through
        assert 'UnknownTool' in result['tools']

    def test_validate_valid_skill(self, loader, sample_skill):
        """Test validating a valid skill"""
        config = loader.load(sample_skill)
        errors = loader.validate(config)

        assert errors == []

    def test_validate_missing_name(self, loader):
        """Test validation with missing name"""
        config = SkillConfig({'description': 'test'}, "")
        errors = loader.validate(config)

        assert "Name is required" in errors

    def test_validate_missing_description(self, loader):
        """Test validation with missing description"""
        config = SkillConfig({'name': 'test'}, "")
        errors = loader.validate(config)

        assert "Description is required" in errors

    def test_validate_unknown_tool(self, loader):
        """Test validation with unknown tool"""
        config = SkillConfig({
            'name': 'test',
            'description': 'test',
            'version': '1.0.0',
            'tools': ['UnknownTool']
        }, "")
        errors = loader.validate(config)

        assert "Unknown tool: UnknownTool" in errors


class TestIntegration:
    """Integration tests"""

    def test_load_real_skill(self):
        """Test loading a real skill from the skills directory"""
        loader = SkillLoader()

        # Test tech-research skill
        skill_path = Path(__file__).parent.parent / 'skills' / 'tech-research' / 'SKILL.md'

        if skill_path.exists():
            config = loader.load(str(skill_path))

            assert config.name == 'tech-research'
            assert len(config.tools) > 0

            # Test conversions
            agent_sdk = loader.to_agent_sdk(config)
            assert 'instructions' in agent_sdk

            openclaw = loader.to_openclaw(config)
            assert 'skills' in openclaw

"""
Universal Skill Loader - Python Implementation
Load SKILL.md files and convert them to Agent SDK agents.
"""

import os
import json
import frontmatter
from typing import Dict, List, Any, Optional


class SkillConfig:
    """Parsed SKILL.md configuration"""

    def __init__(self, metadata: Dict[str, Any], content: str):
        self.name = metadata.get('name', 'unknown')
        self.description = metadata.get('description', '')
        self.version = metadata.get('version', '1.0.0')
        self.author = metadata.get('author', '')
        self.triggers = metadata.get('triggers', [])
        self.tools = metadata.get('tools', [])
        self.content = content

    def __repr__(self) -> str:
        return f"SkillConfig(name={self.name}, version={self.version})"


class SkillLoader:
    """Load SKILL.md files and convert to various formats"""

    def __init__(self, tool_map: Optional[Dict[str, str]] = None):
        """
        Initialize the SkillLoader.

        Args:
            tool_map: Optional custom tool mapping. Defaults to standard Claude Code tools.
        """
        self.tool_map = tool_map or {
            'WebSearch': 'web_search',
            'WebFetch': 'web_fetch',
            'Read': 'read_file',
            'Write': 'write_file',
            'Edit': 'edit_file',
            'Grep': 'grep',
            'Bash': 'bash_command',
            'Glob': 'glob',
            'AskUserQuestion': 'ask_user_question',
        }

    def load(self, skill_path: str) -> SkillConfig:
        """
        Load a SKILL.md file.

        Args:
            skill_path: Path to the SKILL.md file

        Returns:
            SkillConfig object with parsed data

        Raises:
            FileNotFoundError: If the skill file doesn't exist
            ValueError: If the skill file is invalid
        """
        if not os.path.exists(skill_path):
            raise FileNotFoundError(f"Skill file not found: {skill_path}")

        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()

        try:
            post = frontmatter.loads(content)
        except Exception as e:
            raise ValueError(f"Invalid frontmatter in {skill_path}: {e}")

        metadata = post.metadata

        # Validate required fields
        if 'name' not in metadata:
            raise ValueError(f"Missing required field 'name' in {skill_path}")

        if 'description' not in metadata:
            raise ValueError(f"Missing required field 'description' in {skill_path}")

        return SkillConfig(metadata, post.content)

    def load_string(self, content: str) -> SkillConfig:
        """
        Load a SKILL.md from a string.

        Args:
            content: String containing SKILL.md content

        Returns:
            SkillConfig object with parsed data
        """
        try:
            post = frontmatter.loads(content)
        except Exception as e:
            raise ValueError(f"Invalid frontmatter: {e}")

        metadata = post.metadata

        # Validate required fields
        if 'name' not in metadata:
            raise ValueError("Missing required field 'name'")

        if 'description' not in metadata:
            raise ValueError("Missing required field 'description'")

        return SkillConfig(metadata, post.content)

    def to_agent_sdk(self, config: SkillConfig) -> Dict[str, Any]:
        """
        Convert to Agent SDK format.

        Args:
            config: SkillConfig object

        Returns:
            Dictionary in Agent SDK format
        """
        return {
            'name': config.name,
            'description': config.description,
            'instructions': f"You are {config.name}\n\n{config.description}\n\n{config.content}",
            'tools': [self.tool_map.get(t, t) for t in config.tools]
        }

    def to_openclaw(self, config: SkillConfig) -> Dict[str, Any]:
        """
        Convert to OpenClaw format.

        Args:
            config: SkillConfig object

        Returns:
            Dictionary in OpenClaw format
        """
        return {
            'name': config.name,
            'description': config.description,
            'version': config.version,
            'metadata': {
                'author': config.author,
                'triggers': config.triggers,
            },
            'skills': [{
                'name': 'execute',
                'description': config.description,
                'tools': [{'name': self.tool_map.get(t, t)} for t in config.tools]
            }]
        }

    def to_langchain(self, config: SkillConfig) -> Dict[str, Any]:
        """
        Convert to LangChain format.

        Args:
            config: SkillConfig object

        Returns:
            Dictionary in LangChain format
        """
        return {
            'name': config.name,
            'description': config.description,
            'prompt_template': f"{config.description}\n\n{{context}}\n\n{config.content}",
            'tools': [self.tool_map.get(t, t) for t in config.tools]
        }

    def to_claude_code(self, config: SkillConfig) -> str:
        """
        Convert back to Claude Code SKILL.md format.

        Args:
            config: SkillConfig object

        Returns:
            SKILL.md formatted string
        """
        frontmatter_data = {
            'name': config.name,
            'description': config.description,
            'version': config.version,
        }

        if config.author:
            frontmatter_data['author'] = config.author

        if config.triggers:
            frontmatter_data['triggers'] = config.triggers

        if config.tools:
            frontmatter_data['tools'] = config.tools

        # Build frontmatter string
        fm_lines = ["---"]
        for key, value in frontmatter_data.items():
            if isinstance(value, list):
                fm_lines.append(f"{key}:")
                for item in value:
                    fm_lines.append(f"  - {item}")
            else:
                fm_lines.append(f"{key}: {value}")
        fm_lines.append("---")
        fm_lines.append("")

        return "\n".join(fm_lines) + config.content

    def validate(self, config: SkillConfig) -> List[str]:
        """
        Validate a SkillConfig object.

        Args:
            config: SkillConfig object

        Returns:
            List of validation errors (empty if valid)
        """
        errors = []

        if not config.name or config.name == 'unknown':
            errors.append("Name is required")

        if not config.description:
            errors.append("Description is required")

        if not config.version:
            errors.append("Version is required")

        # Check if tools are in the tool map
        for tool in config.tools:
            if tool not in self.tool_map:
                errors.append(f"Unknown tool: {tool}")

        return errors


def main():
    """CLI entry point"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: skill-universal <skill-path> [format]")
        print("\nFormats:")
        print("  agent-sdk  (default)")
        print("  openclaw")
        print("  langchain")
        print("  claude-code")
        sys.exit(1)

    loader = SkillLoader()

    try:
        config = loader.load(sys.argv[1])
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    format_name = sys.argv[2] if len(sys.argv) > 2 else 'agent-sdk'

    if format_name == 'agent-sdk':
        result = loader.to_agent_sdk(config)
    elif format_name == 'openclaw':
        result = loader.to_openclaw(config)
    elif format_name == 'langchain':
        result = loader.to_langchain(config)
    elif format_name == 'claude-code':
        result = loader.to_claude_code(config)
        print(result)
        return
    else:
        print(f"Unknown format: {format_name}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

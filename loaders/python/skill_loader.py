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


class SkillLoader:
    """Load SKILL.md files and convert to various formats"""
    def __init__(self):
        self.tool_map = {
            'WebSearch': 'web_search',
            'WebFetch': 'web_fetch',
            'Read': 'read_file',
            'Write': 'write_file',
            'Grep': 'grep',
            'Bash': 'bash_command',
        }

    def load(self, skill_path: str) -> SkillConfig:
        """Load a SKILL.md file"""
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()
        post = frontmatter.loads(content)
        return SkillConfig(post.metadata, post.content)

    def to_agent_sdk(self, config: SkillConfig) -> Dict[str, Any]:
        """Convert to Agent SDK format"""
        return {
            'name': config.name,
            'description': config.description,
            'instructions': f"You are {config.name}\n\n{config.description}",
            'tools': [self.tool_map.get(t, t) for t in config.tools]
        }

    def to_openclaw(self, config: SkillConfig) -> Dict[str, Any]:
        """Convert to OpenClaw format"""
        return {
            'name': config.name,
            'description': config.description,
            'version': config.version,
            'skills': [{
                'name': 'execute',
                'tools': [{'name': self.tool_map.get(t, t)} for t in config.tools]
            }]
        }


def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python skill_loader.py <skill-path> [format]")
        sys.exit(1)

    loader = SkillLoader()
    config = loader.load(sys.argv[1])
    format = sys.argv[2] if len(sys.argv) > 2 else 'agent-sdk'

    if format == 'agent-sdk':
        result = loader.to_agent_sdk(config)
    elif format == 'openclaw':
        result = loader.to_openclaw(config)
    else:
        print(f"Unknown format: {format}")
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

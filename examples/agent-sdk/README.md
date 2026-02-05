# Using Skills with Agent SDK (Python)

Run Claude Code Skills in Python using Agent SDK.

## Installation

```bash
pip install anthropic
pip install skill-universal
```

## Basic Usage

### Load and Run a Skill

```python
from anthropic import Anthropic
from skill_universal import SkillLoader

# 1. Load the Skill
loader = SkillLoader()
config = loader.load('skills/tech-research/SKILL.md')

# 2. Convert to Agent SDK format
agent_config = loader.to_agent_sdk(config)

# 3. Create Agent
agent = Anthropic()

# 4. Run the Skill
message = agent.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    system=agent_config['instructions'],
    tools=[],  # Add your tools here
    messages=[{
        "role": "user",
        "content": "Research OpenClaw framework"
    }]
)

print(message.content)
```

## Advanced Usage

### With Tools

```python
from anthropic import Anthropic
from skill_universal import SkillLoader

loader = SkillLoader()
config = loader.load('skills/github-analyzer/SKILL.md')
agent_config = loader.to_agent_sdk(config)

# Define your tools
tools = [
    {
        "name": "web_search",
        "description": "Search the web",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            },
            "required": ["query"]
        }
    }
]

agent = Anthropic()

message = agent.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    system=agent_config['instructions'],
    tools=tools,
    messages=[{
        "role": "user",
        "content": "Analyze facebook/react"
    }]
)
```

### Batch Processing

```python
from skill_universal import SkillLoader

loader = SkillLoader()

# Load multiple Skills
skills = ['tech-research', 'github-analyzer', 'document-processor']

for skill_name in skills:
    config = loader.load(f'skills/{skill_name}/SKILL.md')
    agent_config = loader.to_agent_sdk(config)
    # Process with agent_config...
```

## Examples

### Example 1: Tech Research

```python
from skill_universal import SkillLoader
from anthropic import Anthropic

loader = SkillLoader()
config = loader.load('../skills/tech-research/SKILL.md')
agent_config = loader.to_agent_sdk(config)

agent = Anthropic()

result = agent.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4000,
    system=agent_config['instructions'],
    messages=[{
        "role": "user",
        "content": "Research Vue.js 3.0"
    }]
)

print(result.content[0].text)
```

### Example 2: Document Processing

```python
from skill_universal import SkillLoader
from anthropic import Anthropic

loader = SkillLoader()
config = loader.load('../skills/document-processor/SKILL.md')
agent_config = loader.to_agent_sdk(config)

agent = Anthropic()

# Read document
with open('document.pdf', 'rb') as f:
    document_content = f.read()

result = agent.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    system=agent_config['instructions'],
    messages=[{
        "role": "user",
        "content": f"Process this document:\n{document_content[:1000]}"  # First 1000 chars
    }]
)

print(result.content[0].text)
```

## Tool Integration

### Custom Tools

Define your own tools for Skills to use:

```python
def github_search_tool(query: str) -> dict:
    """Custom GitHub search tool"""
    # Your implementation
    return {"results": [...]}

tools = [
    {
        "name": "github_search",
        "description": "Search GitHub repositories",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            }
        }
    }
]
```

### MCP Integration

```python
from mcp import Client

# Connect to MCP server
client = Client('stdio')

# List available tools
available_tools = client.list_tools()

# Convert to Agent SDK format
tools = [
    {
        "name": tool.name,
        "description": tool.description,
        "input_schema": tool.inputSchema
    }
    for tool in available_tools
]
```

## Error Handling

```python
from skill_universal import SkillLoader
import sys

try:
    loader = SkillLoader()
    config = loader.load('skills/my-skill/SKILL.md')
    agent_config = loader.to_agent_sdk(config)
    # Use agent_config...
except FileNotFoundError:
    print("Skill file not found")
    sys.exit(1)
except Exception as e:
    print(f"Error loading skill: {e}")
    sys.exit(1)
```

## Best Practices

1. **Validate Skills**: Check Skill format before loading
2. **Cache Results**: Cache parsed configs for performance
3. **Handle Errors**: Gracefully handle missing tools
4. **Log Usage**: Track which Skills are used most

## See Also

- [Anthropic Agent SDK Docs](https://docs.anthropic.com/claude-code/agents)
- [Python Loader Reference](../../loaders/python/)

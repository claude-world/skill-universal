# Using Skills with OpenClaw

Integrate Claude Code Skills into OpenClaw (open-source agent platform).

## Prerequisites

```bash
# Clone OpenClaw
git clone https://github.com/openclaw/openclaw.git
cd openclaw

# Install dependencies
pnpm install

# Setup environment
cp .env.example .env
```

## Installation

```bash
cd openclaw
npm install skill-universal
```

## Basic Usage

### 1. Copy Skills to OpenClaw

```bash
# Copy skills from skill-universal to OpenClaw
cp -r skill-universal/skills/* openclaw/skills/
```

### 2. Load Skill in OpenClaw

Create a new skill in `openclaw/skills/`:

```typescript
// openclaw/skills/tech-research/index.ts
import { SkillLoader } from 'skill-universal';
import { Skill } from '@openclaw/sdk';

const loader = new SkillLoader();
const config = await loader.load('skills/tech-research/SKILL.md');
const openclawConfig = loader.toOpenClaw(config);

export const techResearchSkill: Skill = {
  name: openclawConfig.name,
  description: openclawConfig.description,
  version: openclawConfig.version,

  async execute(context, params) {
    // Implementation
    const { topic } = params;

    // Use tools from config
    const webSearch = context.tools.get('web-search');
    const results = await webSearch.execute({ query: topic });

    return {
      success: true,
      data: results
    };
  }
};
```

### 3. Register Skill

```typescript
// openclaw/index.ts
import { techResearchSkill } from './skills/tech-research';

openclaw.registerSkill(techResearchSkill);
```

## Advanced Usage

### Dynamic Skill Loading

```typescript
import { SkillLoader } from 'skill-universal';
import { readdir } from 'fs/promises';

async function loadAllSkills(skillDir: string) {
  const loader = new SkillLoader();
  const skills = [];

  const entries = await readdir(skillDir, { withFileTypes: true });

  for (const entry of entries) {
    if (entry.isDirectory()) {
      const skillPath = `${skillDir}/${entry.name}/SKILL.md`;

      try {
        const config = await loader.load(skillPath);
        const openclawConfig = loader.toOpenClaw(config);

        // Convert to OpenClaw Skill
        const skill = createSkillFromConfig(openclawConfig);
        skills.push(skill);
      } catch (error) {
        console.error(`Failed to load ${entry.name}:`, error);
      }
    }
  }

  return skills;
}

function createSkillFromConfig(config) {
  return {
    name: config.name,
    description: config.description,
    version: config.version,

    async execute(context, params) {
      // Generic execution logic
      const tools = config.skills[0].tools;
      const results = [];

      for (const tool of tools) {
        const toolInstance = context.tools.get(tool.name);
        if (toolInstance) {
          const result = await toolInstance.execute(params);
          results.push(result);
        }
      }

      return {
        success: true,
        data: results
      };
    }
  };
}
```

## Examples

### Example 1: Tech Research Skill

```typescript
import { SkillLoader } from 'skill-universal';

const loader = new SkillLoader();
const config = await loader.load('skills/tech-research/SKILL.md');

// Use in OpenClaw
openclaw.onMessage(async (message) => {
  if (message.content.includes('research')) {
    const result = await openclaw.executeSkill('tech-research', {
      topic: extractTopic(message)
    });

    message.reply(result.data.summary);
  }
});
```

### Example 2: Document Processing

```typescript
import { SkillLoader } from 'skill-universal';

const loader = new SkillLoader();
const config = await loader.load('skills/document-processor/SKILL.md');

// Process documents in Discord
openclaw.onMessage(async (message) => {
  if (message.hasAttachment && message.attachment.type === 'pdf') {
    const result = await openclaw.executeSkill('document-processor', {
      file: message.attachment.url,
      format: 'markdown'
    });

    message.channel.send(result.data.content);
  }
});
```

### Example 3: GitHub Analyzer

```typescript
import { SkillLoader } from 'skill-universal';

const loader = new SkillLoader();
const config = await loader.load('skills/github-analyzer/SKILL.md');

// Analyze repos mentioned in chat
openclaw.onMessage(async (message) => {
  const githubRepoMatch = message.content.match(/github\.com\/([^\/]+\/[^\/]+)/);

  if (githubRepoMatch) {
    const [, owner, repo] = githubRepoMatch;

    const result = await openclaw.executeSkill('github-analyzer', {
      owner,
      repo
    });

    message.reply(formatAnalysis(result.data));
  }
});
```

## Tool Integration

### Define Tools in OpenClaw

```typescript
// openclaw/tools/web-search.ts
import { Tool } from '@openclaw/sdk';

export const webSearchTool: Tool = {
  name: 'web-search',
  description: 'Search the web',

  async execute(params) {
    const { query } = params;
    // Your implementation
    return {
      results: [...]
    };
  }
};
```

### Register Tools

```typescript
// openclaw/index.ts
import { webSearchTool } from './tools/web-search';

openclaw.registerTool(webSearchTool);
```

## Configuration

### Environment Variables

```bash
# .env
GITHUB_TOKEN=your_token_here
SLACK_TOKEN=your_slack_token
DISCORD_TOKEN=your_discord_token
```

### Skill Settings

```typescript
// openclaw/config/skills.ts
export const skillSettings = {
  'tech-research': {
    enabled: true,
    channels: ['general', 'research'],
    cooldown: 60000  // 1 minute cooldown
  },
  'document-processor': {
    enabled: true,
    channels: ['general'],
    maxFileSize: 10485760  // 10MB
  }
};
```

## Best Practices

1. **Error Handling**: Always handle errors gracefully
2. **Rate Limiting**: Respect API rate limits
3. **Caching**: Cache results to improve performance
4. **Logging**: Log skill executions for debugging

## Troubleshooting

### Skill Not Loading

```bash
# Check skill format
node -e "const fm = require('front-matter'); const fs = require('fs'); console.log(fm.load(fs.readFileSync('skills/tech-research/SKILL.md', 'utf8')));"
```

### Tool Not Found

```bash
# List available tools
openclaw tools list

# Check tool registration
openclaw tools get web-search
```

### Permission Errors

```bash
# Check permissions
openclaw permissions check

# Grant permissions
openclaw permissions grant tech-research --channel=general
```

## See Also

- [OpenClaw Documentation](https://docs.openclaw.dev)
- [TypeScript Loader Reference](../../loaders/typescript/)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)

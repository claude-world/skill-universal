/**
 * Universal Skill Loader - TypeScript Implementation
 *
 * Load SKILL.md files and convert them to various platform formats.
 */

import { readFile } from 'fs/promises';
import frontmatter from 'front-matter';
import { glob } from 'glob';

export interface SkillConfig {
  name: string;
  description: string;
  version: string;
  author: string;
  triggers: string[];
  tools: string[];
  content: string;
  executionSteps: string[];
}

export interface AgentSDKConfig {
  name: string;
  description: string;
  instructions: string;
  tools: string[];
}

export interface OpenClawConfig {
  name: string;
  description: string;
  version: string;
  skills: OpenClawSkill[];
}

export interface OpenClawSkill {
  name: string;
  description: string;
  tools: { name: string }[];
}

export class SkillLoader {
  private toolMap: Map<string, string>;

  constructor() {
    this.toolMap = this.buildToolMap();
  }

  /**
   * Load a SKILL.md file
   */
  async load(skillPath: string): Promise<SkillConfig> {
    const content = await readFile(skillPath, 'utf-8');
    const { attributes, body } = frontmatter(content);

    const metadata = attributes as Record<string, any>;

    return {
      name: metadata.name || 'unknown',
      description: metadata.description || '',
      version: metadata.version || '1.0.0',
      author: metadata.author || '',
      triggers: metadata.triggers || [],
      tools: metadata.tools || [],
      content: body,
      executionSteps: this.parseExecutionSteps(body)
    };
  }

  /**
   * Convert to Agent SDK format
   */
  toAgentSDK(config: SkillConfig): AgentSDKConfig {
    return {
      name: config.name,
      description: config.description,
      instructions: this.generateInstructions(config),
      tools: this.mapTools(config.tools)
    };
  }

  /**
   * Convert to OpenClaw format
   */
  toOpenClaw(config: SkillConfig): OpenClawConfig {
    return {
      name: config.name,
      description: config.description,
      version: config.version,
      skills: [{
        name: 'execute',
        description: config.description,
        tools: config.tools.map(tool => ({
          name: this.toolMap.get(tool, tool)
        }))
      }]
    };
  }

  /**
   * Parse execution steps from markdown content
   */
  private parseExecutionSteps(content: string): string[] {
    const steps: string[] = [];
    const lines = content.split('\n');
    let inExecutionSection = false;

    for (const line of lines) {
      const trimmed = line.trim();

      if (trimmed.startsWith('## Execution Steps') || trimmed.startsWith('## 執行步驟')) {
        inExecutionSection = true;
        continue;
      }

      if (inExecutionSection && trimmed.startsWith('#')) {
        break;
      }

      if (inExecutionSection && trimmed) {
        steps.push(trimmed);
      }
    }

    return steps;
  }

  /**
   * Generate system prompt from SkillConfig
   */
  private generateInstructions(config: SkillConfig): string {
    const steps = config.executionSteps
      .map((step, i) => `${i + 1}. ${step}`)
      .join('\n');

    return `You are ${config.name}

${config.description}

## Available Tools
${config.tools.join(', ')}

## Execution Steps
${steps}

## Additional Context
${config.content}`;
  }

  /**
   * Map tool names to target platform format
   */
  private mapTools(tools: string[]): string[] {
    return tools.map(tool => this.toolMap.get(tool, tool));
  }

  /**
   * Build tool name mapping
   */
  private buildToolMap(): Map<string, string> {
    return new Map([
      // Claude Code → Agent SDK
      ['WebSearch', 'web_search'],
      ['WebFetch', 'web_fetch'],
      ['Read', 'read_file'],
      ['Write', 'write_file'],
      ['Grep', 'grep'],
      ['Bash', 'bash_command'],

      // Generic mappings
      ['web-search', 'web_search'],
      ['web-fetch', 'web_fetch'],
    ]);
  }

  /**
   * Load all Skills from a directory
   */
  async loadFromDirectory(dir: string): Promise<SkillConfig[]> {
    const files = await glob(`${dir}/**/SKILL.md`);
    const configs: SkillConfig[] = [];

    for (const file of files) {
      const config = await this.load(file);
      configs.push(config);
    }

    return configs;
  }
}

/**
 * CLI interface
 */
async function main() {
  const args = process.argv.slice(2);

  if (args.length < 1) {
    console.log('Usage: npx ts-node skill_loader.ts <skill-path> [format]');
    console.log('Formats: agent-sdk, openclaw');
    process.exit(1);
  }

  const [skillPath, format = 'agent-sdk'] = args;

  const loader = new SkillLoader();
  const config = await loader.load(skillPath);

  let result;

  if (format === 'agent-sdk') {
    result = loader.toAgentSDK(config);
  } else if (format === 'openclaw') {
    result = loader.toOpenClaw(config);
  } else {
    console.error(`Unknown format: ${format}`);
    process.exit(1);
  }

  console.log(JSON.stringify(result, null, 2));
}

if (require.main === module) {
  main().catch(console.error);
}

export { SkillLoader };

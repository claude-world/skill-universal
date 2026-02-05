/**
 * Tests for Skill Universal - TypeScript Loader
 */

import { describe, it, expect, beforeEach } from 'vitest';
import { SkillLoader, SkillConfig } from '../SkillLoader';
import { writeFile, unlink } from 'fs/promises';
import { join } from 'path';

describe('SkillLoader', () => {
  let loader: SkillLoader;
  let testSkillPath: string;

  beforeEach(() => {
    loader = new SkillLoader();
    testSkillPath = join(__dirname, 'test-skill.md');
  });

  describe('load', () => {
    it('should load a valid skill file', async () => {
      const skillContent = `---
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
`;

      await writeFile(testSkillPath, skillContent, 'utf-8');
      const config = await loader.load(testSkillPath);

      expect(config.name).toBe('research-skill');
      expect(config.description).toBe('Research expert');
      expect(config.version).toBe('1.0.0');
      expect(config.author).toBe('Test Author');
      expect(config.triggers).toEqual(['research', 'study']);
      expect(config.tools).toEqual(['WebSearch', 'WebFetch', 'Read']);
      expect(config.content).toContain('## Research Steps');

      await unlink(testSkillPath);
    });

    it('should handle missing optional fields', async () => {
      const skillContent = `---
name: test-skill
description: Test
---

Content
`;

      await writeFile(testSkillPath, skillContent, 'utf-8');
      const config = await loader.load(testSkillPath);

      expect(config.version).toBe('1.0.0');
      expect(config.author).toBe('');
      expect(config.triggers).toEqual([]);
      expect(config.tools).toEqual([]);

      await unlink(testSkillPath);
    });

    it('should parse execution steps', async () => {
      const skillContent = `---
name: test
description: Test
---

## Execution Steps

### 1. First Step
Do something first

### 2. Second Step
Do something second
`;

      await writeFile(testSkillPath, skillContent, 'utf-8');
      const config = await loader.load(testSkillPath);

      expect(config.executionSteps).toBeDefined();
      expect(config.executionSteps.length).toBeGreaterThan(0);

      await unlink(testSkillPath);
    });
  });

  describe('toAgentSDK', () => {
    it('should convert to Agent SDK format', async () => {
      const skillContent = `---
name: test-skill
description: Test skill
tools:
  - WebSearch
  - WebFetch
---

Content
`;

      await writeFile(testSkillPath, skillContent, 'utf-8');
      const config = await loader.load(testSkillPath);
      const agentSDK = loader.toAgentSDK(config);

      expect(agentSDK.name).toBe('test-skill');
      expect(agentSDK.description).toBe('Test skill');
      expect(agentSDK.instructions).toContain('You are test-skill');
      expect(agentSDK.tools).toContain('web_search');
      expect(agentSDK.tools).toContain('web_fetch');

      await unlink(testSkillPath);
    });
  });

  describe('toOpenClaw', () => {
    it('should convert to OpenClaw format', async () => {
      const skillContent = `---
name: test-skill
description: Test skill
version: 2.0.0
author: Test Author
tools:
  - WebSearch
---

Content
`;

      await writeFile(testSkillPath, skillContent, 'utf-8');
      const config = await loader.load(testSkillPath);
      const openClaw = loader.toOpenClaw(config);

      expect(openClaw.name).toBe('test-skill');
      expect(openClaw.description).toBe('Test skill');
      expect(openClaw.version).toBe('2.0.0');
      expect(openClaw.skills).toBeDefined();
      expect(openClaw.skills.length).toBe(1);
      expect(openClaw.skills[0].name).toBe('execute');

      await unlink(testSkillPath);
    });
  });

  describe('tool mapping', () => {
    it('should map Claude Code tools to Agent SDK format', async () => {
      const skillContent = `---
name: test
description: Test
tools:
  - WebSearch
  - WebFetch
  - Read
  - Write
  - Grep
  - Bash
---

Content
`;

      await writeFile(testSkillPath, skillContent, 'utf-8');
      const config = await loader.load(testSkillPath);
      const agentSDK = loader.toAgentSDK(config);

      expect(agentSDK.tools).toEqual([
        'web_search',
        'web_fetch',
        'read_file',
        'write_file',
        'grep',
        'bash_command'
      ]);

      await unlink(testSkillPath);
    });

    it('should pass through unknown tools', async () => {
      const skillContent = `---
name: test
description: Test
tools:
  - UnknownTool
---

Content
`;

      await writeFile(testSkillPath, skillContent, 'utf-8');
      const config = await loader.load(testSkillPath);
      const agentSDK = loader.toAgentSDK(config);

      expect(agentSDK.tools).toContain('UnknownTool');

      await unlink(testSkillPath);
    });
  });

  describe('loadFromDirectory', () => {
    it('should load multiple skills from directory', async () => {
      // This test assumes the skills directory exists
      const skills = await loader.loadFromDirectory(join(__dirname, '../../../skills'));

      expect(skills.length).toBeGreaterThan(0);
      expect(skills[0].name).toBeDefined();
    });
  });
});

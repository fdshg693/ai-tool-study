# Agent Skillsの使い方

## AIに渡される内容
```SKILLS.md```に記載された内容が、自動的にAIに渡されます（フロントマターも含めて）。
その他の、ファイルに関しては、必要に応じてAIが参照します。

## 配置場所

### 基本
```.claude/skills/```フォルダ配下に、スキルごとにフォルダを作成します。  
各フォルダは、`SKILL.md`を持つ必要があります。

### フォルダ構造
- 同階層に、他のファイルをAIが参照するために配置可能。
- `scripts/`フォルダ配下に、CLAUDE CODEが実行できるスクリプトを配置可能。

### デフォルトスキル
CLAUDE CODEは、デフォルトで以下のスキルを持ちます。(CLAUDE API・claude.ai(WEBのclaude）で利用可能）))
PowerPoint (pptx): Create presentations, edit slides, analyze presentation content
Excel (xlsx): Create spreadsheets, analyze data, generate reports with charts
Word (docx): Create documents, edit content, format text
PDF (pdf): Generate formatted PDF documents and reports

## 基本構造
```yml
---
name: your-skill-name
description: Brief description of Skill
allowed-tools: {"ToolName1", "ToolName2"}
---
{your prompt instructions here}
```



### スラッシュコマンドとの比較
スラッシュコマンドは基本的に、ユーザが呼び出すが、エージェントスキルはCLAUDE CODEが呼び出します。
スラッシュコマンドと同様に、Pluginから呼び出すことも可能です。


#### 参考文献
https://code.claude.com/docs/en/skills
https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
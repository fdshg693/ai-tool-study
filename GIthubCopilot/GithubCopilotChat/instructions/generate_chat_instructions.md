# チャット右上の歯車ボタンから「Generate Chat Instructions」を選択した場合、以下の内容が自動的にAIモデルに渡されることになります。

## 英語
Analyze this codebase to generate or update `.github/copilot-instructions.md` for guiding AI coding agents.

Focus on discovering the essential knowledge that would help an AI agents be immediately productive in this codebase. Consider aspects like:
- The "big picture" architecture that requires reading multiple files to understand - major components, service boundaries, data flows, and the "why" behind structural decisions
- Critical developer workflows (builds, tests, debugging) especially commands that aren't obvious from file inspection alone
- Project-specific conventions and patterns that differ from common practices
- Integration points, external dependencies, and cross-component communication patterns

Source existing AI conventions from `**/{.github/copilot-instructions.md,AGENT.md,AGENTS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/**,.windsurf/rules/**,.clinerules/**,README.md}` (do one glob search).

Guidelines (read more at https://aka.ms/vscode-instructions-docs):
- If `.github/copilot-instructions.md` exists, merge intelligently - preserve valuable content while updating outdated sections
- Write concise, actionable instructions (~20-50 lines) using markdown structure
- Include specific examples from the codebase when describing patterns
- Avoid generic advice ("write tests", "handle errors") - focus on THIS project's specific approaches
- Document only discoverable patterns, not aspirational practices
- Reference key files/directories that exemplify important patterns

Update `.github/copilot-instructions.md` for the user, then ask for feedback on any unclear or incomplete sections to iterate.
---

## 日本語訳
このコードベースを分析し、AIコーディングエージェントのためのガイドとなる `.github/copilot-instructions.md` を生成または更新してください。

AIエージェントがこのコードベースですぐに生産的に作業できるようにするために必要な知識の発見に注力してください。以下の観点を考慮します：
- 複数ファイルを読まないと理解できない「全体像」のアーキテクチャ：主要なコンポーネント、サービスの境界、データフロー、構造的な意思決定の「理由」
- 重要な開発者ワークフロー（ビルド、テスト、デバッグ）、特にファイルを見ただけでは分からないコマンド
- 一般的な慣習と異なるプロジェクト固有の規約やパターン
- 統合ポイント、外部依存関係、コンポーネント間の通信パターン

既存のAI向け規約は `**/{.github/copilot-instructions.md,AGENT.md,AGENTS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/**,.windsurf/rules/**,.clinerules/**,README.md}` から取得してください（1回のグロブ検索で）。

ガイドライン（詳細は https://aka.ms/vscode-instructions-docs を参照）：
- `.github/copilot-instructions.md` が存在する場合は、価値ある内容を保持しつつ、古いセクションを更新するように賢くマージする
- Markdown構造で簡潔かつ実用的な指示（20～50行程度）を書く
- パターンを説明する際は、コードベースから具体例を含める
- 一般的な助言（「テストを書く」「エラーを処理する」など）は避け、このプロジェクト固有のアプローチに集中する
- 理想的な慣習ではなく、実際に発見できるパターンのみを記載する
- 重要なパターンを示す主要なファイルやディレクトリを参照する

`.github/copilot-instructions.md` を更新したら、不明点や不十分なセクションについてフィードバックを求め、必要に応じて繰り返し改善してください。
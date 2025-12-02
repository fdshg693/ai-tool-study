# 使えるツール
Github Copilot CLIを起動して、使えるツールを直接聞いてみた結果が以下。

## AIの回答
```markdown
Core Development Tools:

     - bash - Execute commands, build, test, run scripts
     - view - Read files and directories
     - create - Create new files
     - edit - Modify existing files
     - glob - Find files by name patterns
     - grep - Search file contents with regex

   Git & GitHub Tools:

     - github-mcp-server-* - GitHub API access for repos, PRs, issues, workflows, commits, etc.
     - Search code, issues, PRs, repositories, and users across GitHub

   Custom Specialist Agents:

     - {agent-name1} - {agent-description1}
    - {agent-name2} - {agent-description2}
    ...

   Web Search:

     - github-mcp-server-web_search - AI-powered web search with citations

   I'm designed to help with software engineering tasks efficiently, preferring ecosystem tools and delegating to specialized agents when available.
```

## 上記の結果のまとめ
使えるツールは大きく分けて以下の4種類。
1. 開発に使う基本的なツール群
   - bash, view, create, edit, glob, grep など
    - bashが使えるため、CLI上でシェルコマンドを実行できる
2. デフォルトで有効にされているGithub MCPサーバーが提供するツール群
   - github-mcp-server-* 系のツールで、GitHubのAPIを利用してリポジトリ、プルリクエスト、イシュー、ワークフロー、コミットなどにアクセスできる
   - 特に`- github-mcp-server-web_search`ツールで、AIによるウェブ検索が可能
3. カスタムスペシャリストエージェント
   - 利用可能な`.github/agents`配下のエージェントがあれば表示される
   
# 細かい動作

## ~/.copilot/config.jsonの内容
```json
{
  "banner": "never",
  "last_logged_in_user": {
    "host": "https://github.com",
    "login": "username"
  },
  "logged_in_users": [
    {
      "host": "https://github.com",
      "login": "username"
    }
  ],
  "model": "{current_ai_model}",
  "render_markdown": true,
  "screen_reader": false,
  "theme": "auto",
  "trusted_folders": [
    "path_1",
    "path_2",
    "..."
  ],
  "asked_setup_terminals": [
    "vscode"
  ]
}%
```

## トークン
- Github MCPサーバーがデフォルトで登録されており、入力トークンで6Kデフォルトで増大する（2025/12/2現在）
  - --disable-builtin-mcps オプションで、組み込みMCPサーバーを無効化可能
ー以下のような最もトークン数を節約したパターンでも現状8Kの入力トークンが送信される（2025/12/2現在）
```bash
copilot --agent test.calculator --prompt "3+4" --disable-builtin-mcps --model claude-haiku-4.5 
```
- デフォルトで、カスタムインストラクション(AGENTS.mdや.copilot-instructions.md)が存在する場合、それらもコンテキストとして送信されるため、トークン数が増加する
  -  --no-custom-instructions オプションで、カスタムインストラクションの読み込みを無効化可能

## メモ
- CLIは、copilot-instructions.mdを自動で読み込みます
- 原則、CWDより上の階層のファイルはアクセスできません
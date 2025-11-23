# 細かい動作

- CLIは、copilot-instructions.mdなどを自動で読み込みません
- 原則、CWDより上の階層のファイルはアクセスできません
- ~/.copilot/config.jsonの内容
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
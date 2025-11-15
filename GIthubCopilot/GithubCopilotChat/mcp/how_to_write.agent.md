


## リモートMCOサーバー追加
```json
{
  // 複数のMCPサーバーを定義可能
  "servers": {
    "github-mcp": {
      // === 必須 ===
      // 	"http", "sse"
      "type": "http",
      // リモートMCPサーバーのURLを指定
      // "http://localhost:3000", "https://api.example.com/mcp"
      "url": "https://api.githubcopilot.com/mcp",

      //=== 必須でない ===
      "headers": {
        	"Authorization": "Bearer ${input:api-token}"
    }
  }
}
```

## STDIO/STDOUTローカルMCPサーバー追加
```json
{
  "servers": {
    "memory": {
      // === 必須 ===
      // 通信形式をstdioに設定
      "type": "stdio",
      // 実行されるコマンド（環境パスに存在する必要があります）
      "command": "npx",

      //=== 必須でない ===
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        // 必要に応じて環境変数を設定
        "MCP_LOG_LEVEL": "debug",
      },
      // ワークスペースの.envファイルを読み込む設定
      "envFile": "${workspaceFolder}/.env"
    }
  }
}
```

### inputsフィールドの使い方
```json
{
  "inputs": [
    {
      // promptStringはテキストボックスから入力を受け取る。pickStringにした場合は、選択肢から選ぶUIになる
      "type": "promptString",
      // 別の場所から、${input:api-token}で参照可能
      "id": "perplexity-key",
      "description": "Perplexity API Key",
      // 入力内容をパスワードとして扱い、非表示にする場合
      "password": true
    }
  ],
  "servers": {
    "perplexity": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "server-perplexity-ask"],
      "env": {
        "PERPLEXITY_API_KEY": "${input:perplexity-key}"
      }
    }
  }
}
```
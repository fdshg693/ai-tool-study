
- gitの状態を質問する（GITコマンドの実行を許可）
```bash
copilot -p "今週のコミットを表示して要約して" --allow-tool 'shell(git)'
```

- 簡単な計算をカスタムエージェントで実行する
    -組み込みMCPサーバーを無効化(Gihutb MCPサーバーを使用しない)ことで、入力トークンを6K節約（2025/12/2現在）
    - CLIで選択可能な最もリクエストが安価なClaude Haiku 4.5モデルを使用(2025/12/2現在)
```bash
copilot --agent test.calculator --prompt "3+4" --disable-builtin-mcps --model claude-haiku-4.5 
```
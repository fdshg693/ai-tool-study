# CLIでの使い方

## 基本
- copilotと入力して、Enterキーを押すと、CLIでGitHub Copilotを使用できます。
```bash
copilot
```
- カレントディレクトリの変更
    - ```/cwd```
- @path/to/file と入力して、特定のファイルをコンテキストとして渡すことができます。

- 信頼済みフォルダ・ファイルに対してCopilotは作業を行える
    - ```/add-dir /path/to/directory``` でディレクトリを信頼済みフォルダに追加（編集しない限り永続的）
    - ```/add-file /path/to/file``` でファイルを会話のコンテキストに追加（一時的）
    - ```~/.copilot```フォルダ配下の```config.json```に保存される。このフォルダは、XDG_CONFIG_HOME環境変数で変更可能
- copilotのセッション中でも、以下のようにして、「!」を先頭に追加することで、直接シェルコマンドを実行できる
    - ```!ls -la```
- クラウドのCodin Agentにチャットを委譲することも可能
    - ```/delegate add関数の実装を完了して```
- 過去セッションを再開することも可能
    - ```copilot --resume```の後で、目的のセッションを選択する
- カスタムインストラクションとして以下のファイルをサポート
    - .github/copilot-instructions.md 
    - .github/copilot-instructions/**/*.instructions.md
    - ```AGENTS.md.```ファイル
- カスタムエージェントも選択可能
    - インタラクティブモードにて、```/agent```から選択可能
    - 直接、プロンプトから「〜〜エージェントを使用して」と指定することも可能
    - 直接指定も可能
        - ```copilot --agent=refactor-agent --prompt "コードをリファクタリングして"```
        - この場合は、 --promptオプションが必須（2025/12/2）
- MCPサーバーの追加
    - ```/mcp add```より、詳細情報を入力
    - MCPは```~/.copilot/mcp-config.json```に保存される
    - 現状、デフォルトでGithub MCPサーバーが登録されている
        -（--disable-builtin-mcps オプションで無効化可能・--disable-mcp-server <server-name>オプションで特定のMCPサーバーを無効化可能）
- ツール許可
    - ```--allow-all-tools```オプションで、すべてのツールを許可
    - ```--deny-tool <tool-name>```オプションで、特定のツールを拒否(allowオプションより優先)
    - ```--allow-tool <tool-name>```オプションで、特定のツールを許可
    - <tool-name>の書き方
        - 'shell(COMMAND)': 特定のシェルコマンドの実行（例: 'shell(ls)', 'shell(git status)'）
        - 'write': ファイルの編集許可（シェルコマンド以外の）
        - 'My-MCP-Server(tool_name)'
- 使えるモデル
    - ```/model```で利用可能なモデル一覧を表示
- エージェント設定ファイルで有効な項目・無効な項目
    - 有効な項目
        - prompt
    - 無効な項目
        - model
        - tools
- 参考文献
    - https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli#trusted-directories
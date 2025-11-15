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
    - ```/add-dir /path/to/directory``` でディレクトリを追加
    - ```/add-file /path/to/file``` でファイルを追加
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
    ```copilot --agent=refactor-agent --prompt "コードをリファクタリングして"```
- MCPサーバーの追加
    - ```/mcp add```より、詳細情報を入力
    - MCPは```~/.copilot/mcp-config.json```に保存される

- 参考文献
    - https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli#trusted-directories
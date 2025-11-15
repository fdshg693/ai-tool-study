## VSCODEに追加する方法
```.vscode/mcp.json```にMCP設定内容を記載

## VSCODEでサポートされているMCP機能
- 通信形式
    - STDIO/STDOUT：ローカル環境のCLIツールと同様に、標準入出力を使用して通信します。
    - Streamable HTTP：HTTPストリーミングを使用して、リアルタイムでデータを送受信します。
    - SSE(サーバー送信イベント)：レガシー
- MCP機能
    - Tools
    - Prompts
    - Resources
    - Elicitation
    - Sampling
    - Authentication
    - Server instructions
    - Roots
    - 参考文献
        - https://modelcontextprotocol.io/specification/2025-06-18#features

### VSCODEとの統合
- resourceは、コンテキストとして、チャットに追加可能
- promptは/コマンドより選択して、チャット入力欄に追加可能

- 参考文献
    - https://code.visualstudio.com/docs/copilot/customization/mcp-servers
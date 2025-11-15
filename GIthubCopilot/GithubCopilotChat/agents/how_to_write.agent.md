---
name: SampleAgent
description: カスタムエージェントのサンプルファイルです。
argument-hint: このプロンプトはサンプルです。
tools: []
model: GPT-4.1
target: github-copilot
mcp-servers: {}
handoffs:
  - label: do calculus
    agent: agent
    prompt: 1+1を計算してください。
    send: true
  - label: echo word
    agent: agent
    prompt: say "Hello, World!"
---
### name
エージェントの名前を指定できます。
この名前が、他のエージェントからこのエージェントを呼び出す際に使用されます。
指定されない場合、ファイル名が使用されます。
空白などを含むことはできません。

### description
チャット入力上で、プレイスホルダーテキストとして表示される説明文を指定できます。

### argument-hint
argument-hintには、プロンプトに引数を渡す際のヒントテキストを指定できます。
このヒントは、チャットでプロンプトを選択したときに表示されます。

### model
利用するAIモデルを指定します。
指定されない場合、現在チャット上で利用されているモデルが使用されます。

### target
```github copilot```または```vscode```のいずれかを指定します。
AIエージェントに与える環境の種類を指定します。

### mcp-servers
Agentが利用するMCPサーバーの設定ファイルを配列形式で指定できます。

### handoffs
handoffsには、このエージェントが他のエージェントに処理を引き継ぐ際の設定を配列形式で指定できます。

- label: 引き継ぎのラベルを指定します。(ボタンに表示されるテキスト)
- agent: 引き継ぎ先のエージェント名を指定します。  
- prompt: 引き継ぎ時に渡すプロンプトを指定します。  
- send: trueに設定すると、選択時に、設定したプロンプトが自動的に送信されます。falseの場合、ユーザーが手動で送信する必要があります。
  - デフォルトはFALSEです。
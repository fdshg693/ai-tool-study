# GitHub Copilot のログを VS Code で確認する方法

## パネルで確認する場合
GitHub Copilot のログは、VS Code の「出力」パネルから確認できます。

## 手順

1. **出力パネルを開く**
   - キーボードショートカット: `⇧⌘U` (Shift + Cmd + U)
   - または、メニューから **表示** → **出力** を選択

2. **出力パネルのドロップダウンから「GitHub Copilot」を選択**
   - 出力パネル右上のドロップダウンリストをクリック
   - 以下のいずれかを選択:
     - **GitHub Copilot** - 一般的なログ
     - **GitHub Copilot Chat** - チャット関連のログ
     - **GitHub Copilot Language Server** - 言語サーバーのログ（利用可能な場合）

## 詳細なログを有効にする方法

より詳細なログを取得したい場合は、設定でログレベルを変更できます。

1. **コマンドパレットを開く** (`⇧⌘P`)
2. **Developer: Set Log Level...** を実行
3. **GitHub Copilot** を選択し、**Debug** または **Trace** を選択

## 利用可能なログチャンネル

| チャンネル名 | 内容 |
|-------------|------|
| GitHub Copilot | 補完機能の一般ログ |
| GitHub Copilot Chat | チャット機能のログ |
| GitHub Copilot Language Server | LSP 通信のログ |

---

## Chat Debug View

Chat Debug viewは、VS Code内でAIリクエストとレスポンスの詳細を確認できる専用ビューです。言語モデルに何の情報が送られ、どのように応答するかを理解するのに役立ちます。

> 参考: https://code.visualstudio.com/docs/copilot/chat/chat-debug-view

### 表示される情報

Chat Debug viewでは各インタラクションについて以下の情報が確認できます：

- AIの振る舞いを設定する**システムプロンプト**
- ユーザーが送信した**プロンプト**
- 言語モデルに送信される**コンテキスト**
- 言語モデルからの**詳細なレスポンス**
- チャットリクエストの一部として呼び出された**ツールからのレスポンス**

### 開き方

Chat Debug viewを開く方法は2つあります：

1. **Chatのオーバーフローメニューから開く**
   - Chatパネルの「...」メニューから「Show Chat Debug View」を選択

2. **コマンドパレットから開く**
   - `⇧⌘P` でコマンドパレットを開く
   - 「Developer: Show Chat Debug View」コマンドを実行

### 活用ポイント

- 各セクションを展開して詳細を確認できる
- 特に**Agentモード**で複数のツールが呼び出される場合に有用
- Copilotが内部でどのようなプロンプトやコンテキストを使っているか確認できる
- プロンプトエンジニアリングの理解やデバッグに非常に有用

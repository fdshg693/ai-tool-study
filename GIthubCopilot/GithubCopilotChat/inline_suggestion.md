# Github Copilotのインラインサジェストの内部動作について
Github Copilotのインラインサジェスト機能は、内部的には以下のようなリクエストを送ることで、補完候補文章を生成しています。  
これは、実際にTerminalエリアのGithub Copilot Chatのログに表示されているリンクをクリックすることで、実際に確認することができます。  
また、チャット右上の歯車ボタンから「Chat Debug view」をクリックすることでも開くことができます。  
以下は、単純・省略化したリクエスト例です。
## メタデータ（ログに表示される情報）
- ここから、gpt-4.1-mini-2025-04-14モデルが使用されていることがわかります。
- また、temperatureが0に設定されていることから、より決定論的な応答が生成されることが示唆されます。
---
## Metadata
~~~
requestType      : ProxyChatCompletions
model            : copilot-nes-oct
maxPromptTokens  : 12285
otherOptions     : {"temperature":0,"stream":true}
timeToFirstToken : 319ms
resolved model   : gpt-4.1-mini-2025-04-14
usage            : {"completion_tokens":142,"completion_tokens_details":{"accepted_prediction_tokens":112,"audio_tokens":0,"reasoning_tokens":0,"rejected_prediction_tokens":1},"prompt_tokens":2434,"prompt_tokens_details":{"audio_tokens":0,"cached_tokens":0},"total_tokens":2576}
~~~

## AIに渡すリクエストメッセージを生成します
### システムメッセージ
日本語訳すると、以下のようなシステムメッセージになります。
```
「ユーザーのコンテキストに基づいて次のコード編集を予測し、Microsoftのコンテンツポリシーに従い、著作権侵害を避けてください。リクエストがガイドラインに違反する可能性がある場合は、「申し訳ありませんが、それについてはお手伝いできません」と返答してください。」
```
---
### System
~~~md
Predict the next code edit based on user context, following Microsoft content policies and avoiding copyright violations. If a request may breach guidelines, reply: "Sorry, I can't assist with that."
~~~

### ユーザーメッセージ
#### 関連コードスニペット情報
- 最近ユーザが閲覧したコードスニペット
- 現在編集中のファイルの内容
- 直近の編集差分履歴
- 編集対象コードの周辺コード（編集対象コードは`code_to_edit`タグで囲まれ、カーソル位置は`<|cursor|>`で示される）
---
### User
- 最近ユーザが閲覧したコードスニペット
~~~md
<|recently_viewed_code_snippet|>
code_snippet_file_path: /absolute/path/to/recently/viewed/file.md

{recently viewed code snippet contents}
<|/recently_viewed_code_snippet|>
~~~
- 現在編集中のファイルの内容
~~~md
<|current_file_content|>
current_file_path: /absolute/path/to/current/file.md

{current file snippet contents}
<|/current_file_content|>
~~~
- 直近の編集差分履歴
~~~md
<|edit_diff_history|>
--- /absolute/path/to/edited/file1.md
+++ /absolute/path/to/edited/file1.md
@@ -1,0 +1,1 @@
+    - {added line of code}

--- /absolute/path/to/edited/file2.md
+++ /absolute/path/to/edited/file2.md
@@ -6,1 +6,1 @@
-{original line of code}
+{modified line of code}
<|/edit_diff_history|>
~~~
- 編集対象コードの周辺コード（編集対象コードは`code_to_edit`タグで囲まれ、カーソル位置は`<|cursor|>`で示される）
~~~md
<|area_around_code_to_edit|>
<|code_to_edit|>
{code to edit before cursor} <|cursor|>{code to edit after cursor}

<|/code_to_edit|>
<|/area_around_code_to_edit|>
~~~
#### 期待動作を教えるプロンプト
- AIのに上のスニペットの見方を教える
- AIにコード編集を予測させる
```
日本語訳すると、以下のようなユーザーメッセージになります。
「開発者は、`github-copilot/docs/memo.md`にあるファイル内の`code_to_edit`タグ内のコードセクションで作業していました。与えられた`recently_viewed_code_snippets`、`current_file_content`、`edit_diff_history`、`area_around_code_to_edit`、および`<|cursor|>`でマークされたカーソル位置を使用して、開発者の作業を続けてください。開発者が次に行ったであろう変更を予測して完了させることで、`code_to_edit`セクションを更新してください。`<|code_to_edit|>`と`<|/code_to_edit|>`タグの間にあった修正後のコードを提供しますが、タグ自体は含めないでください。明らかなタイプミスやエラーがない限り、開発者の最後の変更を取り消したり元に戻したりしないでください。レスポンスに行番号や#|の形式を含めないでください。行をスキップしないでください。手抜きをしないでください。」
```
---
```
The developer was working on a section of code within the tags `code_to_edit` in the file located at `github-copilot/docs/memo.md`. Using the given `recently_viewed_code_snippets`, `current_file_content`, `edit_diff_history`, `area_around_code_to_edit`, and the cursor position marked as `<|cursor|>`, please continue the developer's work. Update the `code_to_edit` section by predicting and completing the changes they would have made next. Provide the revised code that was between the `<|code_to_edit|>` and `<|/code_to_edit|>` tags, but do not include the tags themselves. Avoid undoing or reverting the developer's last change unless there are obvious typos or errors. Don't include the line numbers or the form #| in your response. Do not skip any lines. Do not be lazy.
```
### 実際の補完結果
#### 補完対象のコード
---
## Prediction
```markdown
This is a
```
#### 補完結果
---
## Response
### Assistant
~~~md
This is a pen.
~~~
# .instructions.mdファイルの説明

.instructions.mdファイルは、特定の種類のファイルを読み込む際に、Github Copilotに特定の指示を与えるために使用されます。
```.github/copilot-instructions.md```も同様ですが、こちらは１ファイルしか書けない、必ず読み込まれる、
クラウドで動作するCoding Agentも参照するなど、より汎用的な指示を与えるために使用されます。

## 詳細な読み込まれ方の説明
複数のインストラクションが読み込まれ場合、VSCODEは全てをまとめてAIに渡します。
読み込み順なども不定であるため、指示が競合する場合は意図しない動作をする可能性があります。

## 主要条件
```.github/instructions```フォルダ直下に配置される必要があります。
直下でない場合、配下にあってもAIは認識しません。
ただし、認識するフォルダを```chat.instructionsFilesLocations```設定で追加することが可能です。

## 参考
```.github/instructions/samples/sample.instructions.md```を参考にしてください。

### 参考文献
- [VSCODE公式ドキュメント]https://code.visualstudio.com/docs/copilot/customization/custom-instructions

## AGENTS.md    
chat.useAgentsMdFile設定により、AGENTS.mdファイルをサポートします。

### EXPERIMENTAL: ネストされたAGENTS.mdファイル
chat.useNestedAgentsMdFiles設定により、ネストされたAGENTS.mdファイルをサポートします。
有効にされた場合は、VSCODEが再起的に全てのAGENTS.mdファイルを探索し、全てのファイルパスをAIに渡します。
AIは、渡されたパスから適切なファイルを選択して使用します。


### ```settings.json```に以下のように記載することで、シナリオごとに特定のファイルを読み込ませることが可能です
```json
{
  // PR説明生成時に特定の指示ファイルを使用する
  "github.copilot.chat.pullRequestDescriptionGeneration.instructions": [
    { "text": "Always include a list of key changes." }
  ],
  // コードレビュー時に特定の指示ファイルを使用する
  "github.copilot.chat.reviewSelection.instructions": [
    { "file": "guidance/backend-review-guidelines.md" },
    { "file": "guidance/frontend-review-guidelines.md" }
  ],
  // コミットメッセージ生成時に特定の指示ファイルを使用する
  "github.copilot.chat.commitMessageGeneration.instructions": [
        {"file": ".copilot-commit-message-instructions.md"}
    ]
}
```
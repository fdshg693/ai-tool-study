# .prompt.mdファイルの説明

.instructions.mdファイルと違い、自動でVSCODEがAIに渡しません。
ユーザが必要に応じて、プロンプトを選択し、AIに渡す形となります。

### 設定の仕方
```.github/prompts```フォルダ直下に配置される必要があります。
直下でない場合、配下にあってもAIは認識しません。
ただし、```chat.promptFilesLocations```設定で、別のフォルダを追加指定することも可能です。

### BODYセクションの書き方
#tool:<tool-name> を使用して、特定のツールを参照させることができます。
以下のような変数を利用することが可能です
- Workspace変数： ${workspaceFolder}, ${workspaceFolderBasename}
- 選択箇所変数： ${selection}, ${selectedText}
- ファイル変数： ${file}, ${fileBasename}, ${fileDirname}, ${fileBasenameNoExtension}
- 入力変数： ${input:variableName}, ${input:variableName:placeholder} プロンプトから変数を渡せます


## 参考
```.github/prompts/samples/sample.prompt.md```を、オプションの書き方の参考にしてください。
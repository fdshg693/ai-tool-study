# hooksスクリプトの書き方

### 実行の中止を制御できる
- echo '{"cancel": false}': フックの実行を継続します。
- echo '{"cancel": true}': フックの実行を中止します。

### 動的にAIの会話に、テキストを以下のフィールドから挿入できる
- contextModificationフィールドを利用



## プロンプトを渡す
- ```claude "プロンプト内容"```
    - REPLが起動して、最初のプロンプトとして渡される。
- ```claude -p "プロンプト内容"```
    - SDK経由で、プロンプトが渡され、回答後に終了する。

## オプション
- パイプでコンテンツを渡すこともできる。
    - 例: ```cat file.txt | claude```
- `-c`オプションを渡すことで、最新の会話コンテキストから継続できる。
- `-r "<session-id>"`オプションを渡すことで、特定のセッションから継続できる。
- `claude mcp`でmcp設定を行うことができる。

## 動作変更オプション
- `--add-dir`: 指定したディレクトリ（複数可）を作業ディレクトリとして追加する。
- `--allowedTools`: 使用を許可するツールを指定する。
    - e.g. : `"Bash(git log:*)" "Bash(git diff:*)" "Read"`
- `--disallowedTools`: 使用を禁止するツールを指定する。
    - e.g. : `"Bash(git log:*)" "Bash(git diff:*)" "Read"`

#### 参考文献
https://code.claude.com/docs/en/cli-reference
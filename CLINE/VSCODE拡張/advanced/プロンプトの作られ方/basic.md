# CLINEがAIを呼び出す際の、プロンプトの構築方法について
CLINERULESなどは以下のリクエストには含まれていない

### ユーザのプロンプトを渡す
```markdown
<task>
{ユーザのプロンプトをここに挿入}
</task>
```

### TODOリスト作成の勧め
```markdown
# task_progress RECOMMENDED

When starting a new task, it is recommended to include a todo list using the task_progress parameter.


1. Include a todo list using the task_progress parameter in your next tool call
2. Create a comprehensive checklist of all steps needed
3. Use markdown format: - [ ] for incomplete, - [x] for complete

**Benefits of creating a todo/task_progress list now:**
	- Clear roadmap for implementation
	- Progress tracking throughout the task
	- Nothing gets forgotten or missed
	- Users can see, monitor, and edit the plan

**Example structure:**```
- [ ] Analyze requirements
- [ ] Set up necessary files
- [ ] Implement main functionality
- [ ] Handle edge cases
- [ ] Test the implementation
- [ ] Verify results```

Keeping the task_progress list updated helps track progress and ensures nothing is missed.
```

### 環境情報を渡す

#### エディタ・時刻設定
```markdown
<environment_details>
# Visual Studio Code Visible Files
{.clinerules/配下のマークダウンファイルを列挙}

# Visual Studio Code Open Tabs
{現在開いているタブのファイル名を列挙}

# Current Time
{現在の日時を記載}

# Current Working Directory (/Users/seiwan/CodeStudy/ai-tool-study) Files
{カレントディレクトリ直下のファイル・フォルダを列挙}

# Workspace Configuration
{
  "workspaces": {
    {カレントディレクトリへの絶対パス}: {
      "hint": "カレントフォルダ名",
      "associatedRemoteUrls": [
        "origin: {GitHubリポジトリのURL}"
      ],
      "latestGitCommitHash": "{最新のGitコミットハッシュ}"
    }
  }
}
```

### その他設定
- 使用可能なCLIツール
- コンテキストウィンドウの使用状況
- 現在のモード（ACT MODE / PLAN MODE）
```markdown
# Detected CLI Tools
These are some of the tools on the user's machine, and may be useful if needed to accomplish the task: 
{パス上に見つかったcliツールを列挙}
This list is not exhaustive, and other tools may be available.

# Context Window Usage
0 / 256K tokens used (0%)

# Current Mode
ACT MODE
</environment_details>
```
# AIに渡されるユーザープロンプト

## 最初にシステムプロンプトと一緒に渡されるコンテキスト
```markdown
<environment_info>
The user's current OS is: {user platform, e.g., "macOS", "Windows", "Linux"}.
The user's default shell is: {user shell, e.g., "bash", "zsh"}. 
When you generate terminal commands, please generate them correctly for this shell.
</environment_info>
<workspace_info>
I am working in a workspace with the following folders:
- {path to the root folder of the workspace}
I am working in a workspace that has the following structure:
```
{tree of the workspace}
```
This is the state of the context at this point in the conversation. 
The view of the workspace structure may be truncated. You can use tools to collect more context if needed.
</workspace_info>
```

## ユーザ入力された場合のプロンプト(runSubAgentツールだけを有効にした場合)

### #がついたツールがユーザ入力にある場合、そのことをプロンプトに含めている
```markdown
<toolReferences>
The user attached the following tools to this message. The userRequest may refer to them using the tool name with "#". These tools are likely relevant to the user's query:
- runSubagent 
</toolReferences>
```

### 日付・開かれているファイル・リマインド指示を含める
```markdown
<context>
The current date is {current date}.
</context>
<editorContext>
The user's current file is {path to current file}. 
</editorContext>
<reminderInstructions>
You are an agent - you must keep going until the user's query is completely resolved, before ending your turn and yielding back to the user. ONLY terminate your turn when you are sure that the problem is solved, or you absolutely cannot continue.
You take action when possible- the user is expecting YOU to take action and go to work for them. Don't ask unnecessary questions about the details if you can simply DO something useful instead.
</reminderInstructions>
```

### ユーザプロンプトをそのまま含める
```markdown
<userRequest>
#runSubagent 出来るだけ短いなぞなぞをサブエージェントに書かせて、ベストなものを提示して
</userRequest>
```
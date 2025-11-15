# runSubAgentツール
サブエージェントに、特定のタスクの処理を委譲するためのツールです。

## ツール呼び出しJSON
```json
tools: [
    {
        "function": {
            "name": "runSubagent",
            "description": "Launch a new agent to handle complex, multi-step tasks autonomously. This tool is good at researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries, use this agent to perform the search for you.\n\n- Agents do not run async or in the background, you will wait for the agent's result.\n- When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.\n- Each agent invocation is stateless. You will not be able to send additional messages to the agent, nor will the agent be able to communicate with you outside of its final report. Therefore, your prompt should contain a highly detailed task description for the agent to perform autonomously and you should specify exactly what information the agent should return back to you in its final and only message to you.\n- The agent's outputs should generally be trusted\n- Clearly tell the agent whether you expect it to write code or just to do research (search, file reads, web fetches, etc.), since it is not aware of the user's intent",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "A detailed description of the task for the agent to perform"
                    },
                    "description": {
                        "type": "string",
                        "description": "A short (3-5 word) description of the task"
                    }
                },
                "required": [
                    "prompt",
                    "description"
                ]
            }
        },
        "type": "function"
    }
]
```

### descriptionの日本語訳

```markdown
複雑な複数ステップのタスクを自律的に処理する新しいエージェントを起動します。このツールは、複雑な質問の調査、コードの検索、複数ステップのタスクの実行に優れています。キーワードやファイルを検索していて、最初の数回の試行で正しい結果が見つかる自信がない場合は、このエージェントに検索を実行させてください。  

- エージェントは非同期またはバックグラウンドで実行されず、エージェントの結果を待つことになります。
- エージェントが完了すると、単一のメッセージが返されます。エージェントから返される結果はユーザーには表示されません。ユーザーに結果を表示するには、結果の簡潔な要約を含むテキストメッセージをユーザーに送信する必要があります。
- 各エージェントの呼び出しはステートレスです。エージェントに追加のメッセージを送信することはできず、エージェントも最終レポート以外であなたと通信することはできません。したがって、プロンプトにはエージェントが自律的に実行するための非常に詳細なタスク説明を含める必要があり、エージェントが最終的かつ唯一のメッセージで返すべき情報を正確に指定する必要があります。
- エージェントの出力は一般的に信頼されるべきです
- エージェントはユーザーの意図を認識していないため、コードを書くことを期待しているのか、単に調査（検索、ファイル読み取り、Web取得など）を行うことを期待しているのかを明確に伝えてください
```
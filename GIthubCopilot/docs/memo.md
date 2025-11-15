Github Copilotのoutputを見ると、以下のようなログが出力されていることがあります。
2025-11-14 21:25:16.263 [info] [fetchCompletions] Request d7cfe07c-68f6-4a07-b262-407866d0829d at <https://proxy.individual.githubcopilot.com/v1/engines/gpt-41-copilot/completions> finished with 200 status after 238.90458299964666ms
つまり、内部的には、Github Copilotはエンドポイントとして、https://proxy.individual.githubcopilot.com/v1/engines/gpt-41-copilot/completionsを使用していることがわかります。

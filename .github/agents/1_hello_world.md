---
name: HelloWorldAgent
description: サンプル用のHELLO =>WORLDの順番で返すエージェントです。
argument-hint: 指示通りに行なってください。
model: GPT-4.1
target: github-copilot
mcp-servers: {}
handoffs:
  - label: say world
    agent: agent
    prompt: Worldと返してください。
    send: true
---
"Hello"と返してください。
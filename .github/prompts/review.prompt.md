---
description: ワークスペース全体を探索し、レビューするプロンプトファイルです。
name: ReviewPrompts
argument-hint: このプロンプトはワークスペース全体を探索し、レビューします。
agent: agent
model: GPT-4.1
tools: ['search']
---
以下の順序で、ワークスペース全体を探索し、レビューしてください。
1. #tool:search/listDirectoryを「/」に適用して、全てのディレクトリとファイルをリストアップします。
2. #tool:search/fileSearchを「**.md」に適用して、全てのMarkdownファイルを見つけます。
3. 各Markdownファイルに対して、#tool:search/readFileを使用して、最初の10行を読み取ります。
4. 最も重要と考えられるMarkdownファイルを3つ選び、その内容を#tool:search/readFileで完全に読み取ります。
5. 重要と思われるキーワードを3つ選び、#tool:search/textSearchを使用して、ワークスペース全体でそのキーワードを検索します。
6. 最後に、ここまでで収集した情報を基に、ワークスペース全体のレビューを行います。
# Workflowsについて

- ```.clinerules/workflows```フォルダ配下に作成するMDファイルは、WorkflowsとしてCLINEに読み込まれます。
    - Workflowsは、複数のステップからなる一連のタスクを自動化するための機能です。
    - ただし、書き方自体は、通常のCLINEルールと同じです。
    - clineruleと同様に、直下のファイルだけでなく、サブフォルダ配下のファイルも読み込まれます。
- スラッシュコマンドを使って、Workflowsを実行できます。
    - 例: ```/workflow_test.md``` （.clinerules/workflows/test/workflow_test.mdを実行）
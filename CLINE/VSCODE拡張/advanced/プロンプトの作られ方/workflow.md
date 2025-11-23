# スラッシュコマンドからWORKFLOWを実行
ユーザプロンプトの代わりに以下のようなプロンプトが先頭に追加されます

````xml
<explicit_instructions type="workflow_test.md">
1. check current cwd
```bash
pwd
````

2. check files

```bash
ls -la
```

3. answer where you are and what files are there
 </explicit_instructions>
````

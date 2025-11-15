### Requests例
```json
{
  jsonrpc: "2.0";
  // ユニークなNULLでない識別子
  id: string | number; 
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

### Responses例
```json
{
  jsonrpc: "2.0";
  id: string | number;
  // resultかerrorのどちらか片方だけを設定する
  result?: {
    [key: string]: unknown;
  }
  error?: {
    // エラーコードは数値である必要がある
    code: number;
    message: string;
    data?: unknown;
  }
}
```

### Notifications例
- clientからもserverからも一方通行メッセージとして送信可能。受信者は応答を返さない
```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```
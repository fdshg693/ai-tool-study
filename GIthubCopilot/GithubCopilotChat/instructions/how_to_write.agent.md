---
description: サンプル指示ファイルです。
name: SampleInstructions
applyTo: '**'
---
### description
descriptionには、この指示ファイルの内容を簡潔に説明するテキストを指定できます。
この説明は、指示ファイルと共に、AIに提供されます。

### name
nameには、この指示ファイルをUI上で識別するための名前を指定できます。
指定されない場合、ファイル名が使用されます。

### applyTo
applyToにはGLOBパターンを指定できます。
例えば、`applyTo: 'infrastructure/**'`のように指定すると、そのフォルダ内のすべてのファイルに対してこの指示が適用されます。

また、複数パターンをカンマで区切って指定することも可能です。
例えば、`applyTo: 'infrastructure/**,docs/**'`のように指定すると、`infrastructure`フォルダと`docs`フォルダ内のすべてのファイルに対してこの指示が適用されます。
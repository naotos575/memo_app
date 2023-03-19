## memo_app
メニュー画面に従って数字を選択するとタスクの追加、表示、削除や機能の終了することができるアプリです。

**memoapp.py**は記憶しないメモ帳、**emo_memo.py**は記録した内容がポジティブかネガティブか判断するものです。

- 環境構築
```
conda env create -f memo.yml
```

- メモアプリ起動例
```
python memo_app.py
```

### 表示画面例

<img width="177" alt="スクリーンショット 2023-03-20 4 52 11" src="https://user-images.githubusercontent.com/95089385/226205713-7978b0a0-0661-478f-8982-1635e215b325.png">

### 今後の計画
- 自作のファインチューニングモデルの使用
- positive, negative以外の評価
- dataの表示
- テストコード

### 必要なこと
- Sqliteに対する理解
- アプリのフレームワーク理解

などなど

### 参考文献
- Hugging Face Piplines [[site]](https://huggingface.co/docs/transformers/main_classes/pipelines)
- Pretrained Japanese Sentimental Analysis [[site]](https://huggingface.co/jarvisx17/japanese-sentiment-analysis)
- sqlite3 [[site]](https://docs.python.org/3.10/library/sqlite3.html)

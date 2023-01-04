# tesseractのインストール
```
# リポジトリの追加
add-apt-repository ppa:alex-p/tesseract-ocr5
apt-get update
```

```
# tesseractのインストール
apt install -y tesseract-ocr
```

```
# バージョン確認
tesseract --version
```


# tesseractに日本語設定

```
# 利用可能な言語の表示
tesseract --list-langs
```

```
# 日本語化パッケージの検索
apt search tesseract-ocr-jpn
```

```
# 検索にヒットしたパッケージのインストール
apt-get update
apt install -y tesseract-ocr-jpn
apt install -y tesseract-ocr-jpn-vert
```

```
# 利用可能な言語の表示
tesseract --list-langs
```

# tesseractの使い方

```
# 日本語(横)
tesseract [画像データ] - -l jpn
# 日本語(縦)
tesseract [画像データ] - -l jpn_vert
# 英語
tesseract [画像データ] -
tesseract [画像データ] - -l eng
```
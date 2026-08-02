# atcoder-programming

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)
![Formatter](https://img.shields.io/badge/formatter-ruff-000000.svg)

## 概要

AtCoderの問題を解くための個人プロジェクトです。週1回のABC（AtCoder Beginner Contest）チャレンジや、AHC（AtCoder Heuristic Contest）もこのリポジトリで実施します。過去ABC問題もこのプロジェクトの管理対象に含みます。

## ディレクトリ構成

- `contests/` — コンテストごとにフォルダを分けてABC問題を管理する
  - `contests/<contest_name>/<problem_letter>_test/` — サンプルケース置き場（`dt` でダウンロードされる）
- `tools/create_new_contest.py` — 新規コンテストのひな形を作成するスクリプト
- `tools/download_test.py` / `tools/run_test.py` — サンプルケースのダウンロード・実行用スクリプト
- `dt` / `rt` — 上記2スクリプトの短縮実行ラッパー
- `cc` — `tools/create_new_contest.py` の短縮実行ラッパー
- `tools/contest_utils.py` — `contest_name` の数字省略形（例: `426` → `abc426`）を解決する共有ヘルパー
- `template.py` — 新規解答用のテンプレート
- `tests/` — プロジェクト初期化時のサンプルで、コンテスト解答のテストとは無関係
- `pyproject.toml` / `uv.lock` — [uv](https://docs.astral.sh/uv/) による依存関係管理
- `LICENSE.txt` — ライセンス

## 使い方

1コンテストを解く一連の流れを、`abc426` を例に説明します。

### 1. 新規コンテストのひな形作成

```
./cc 426
```

`template.py` を `contests/abc426/a.py` 〜 `g.py` としてコピーします。`contest_name` には `abc426` のようなフルネームの他、数字のみ（`426`）も指定でき、その場合は `abc<3桁ゼロ埋め>`（`abc426`）として扱われます。特定の問題だけ作りたい場合は `problems` 引数で文字を指定します（例: `./cc 426 ab` でA, B問題のみ作成）。`cc` は `uv run python tools/create_new_contest.py` を呼ぶだけの短縮ラッパーで、フルコマンドで直接叩いても同じです。

### 2. サンプルケースのダウンロード

A問題のサンプルをダウンロードします。ABC問題のURLは `contest_name`/`problem_letter` から機械的に決まるため、URLは省略できます。

```
./dt 426 a
```

省略時は `https://atcoder.jp/contests/abc426/tasks/abc426_a` が自動生成されます。サンプルは `contests/abc426/a_test/` に保存されます。ABC以外の形式などURLを明示したい場合は3番目の引数として渡します（例: `./dt abc426 a https://atcoder.jp/contests/abc426/tasks/abc426_a`）。

### 3. 解答を書く

`contests/abc426/a.py` を編集して解答を実装します。

### 4. サンプルケースでテスト実行

```
./rt 426 a
```

ダウンロード済みのサンプルケースに対して解答を実行し、期待出力と一致するか確認します。`contest_name` は `dt`/`cc` と同様、数字のみ（`426`）も指定できます。複数問題をまとめてテストしたい場合は `./rt 426 ab` のように文字を並べて指定します。

### 5. Lint

```
uv run ruff check .
```

提出前に構文・スタイルチェックを行います。

## ライセンス

このプロジェクトは [MIT License](./LICENSE.txt) のもとで公開されています。

# CLAUDE.md

AtCoder（ABC/AHC）の解答を管理する個人リポジトリ。Python 3.12+、依存関係は `uv` で管理（`pyproject.toml` / `uv.lock`）。

## ディレクトリ構成

- `contests/<contest_name>/<problem_letter>.py` — コンテストごとにフォルダを分けて解答を管理する。例: `contests/abc426/c.py`
  - `contests/abc999/` は動作確認用のサンプルフォルダであり、実コンテストではない（`.gitignore` で中身を除外済み）
- `template.py` — 新規解答用テンプレート（ルート直下）
- `tools/create_new_contest.py` — 新規コンテストのひな形を作成するスクリプト
- `tools/download_test.py` / `tools/run_test.py` — サンプルケースのダウンロード・実行用スクリプト
- `tools/contest_utils.py` — `contest_name` の数字省略形（例: `426` → `abc426`）を解決する共有ヘルパー。`create_new_contest.py` / `download_test.py` から参照される
- `dt` / `rt` — 上記2スクリプトの短縮実行ラッパー（ルート直下、実行可能ファイル）
- `cc` — `tools/create_new_contest.py` の短縮実行ラッパー（ルート直下、実行可能ファイル）
- `contests/<contest_name>/<problem_letter>_test/` — 各問題のサンプルケース置き場。例: `contests/abc426/c_test/sample-1.in`
- `snippets/` — アルゴリズムスニペット置き場（現状空、将来用）
- `tests/` — プロジェクト初期化時のサンプルで、コンテスト解答のテストとは無関係

## 新規コンテストの作成

```
./cc <contest_name> [problems]
```

- `cc` は `uv run python tools/create_new_contest.py` を呼ぶだけの短縮ラッパー（`dt`/`rt` と同様、`chmod +x` 済み、リポジトリ外のディレクトリからでも動作する）。フルコマンド（`uv run tools/create_new_contest.py <contest_name> [problems]`）で直接叩いても同じ
- `contest_name`: 例 `abc426`（小文字 + 番号）。数字のみ（例: `463`）を渡すと `abc<3桁ゼロ埋め>`（`abc463`）として扱われる
- `problems`: 作成する問題文字を並べたもの。省略時は `abcdefg`（a〜gの7問分を作成）
- `template.py` を `contests/<contest_name>/<letter>.py` としてコピーするだけの処理。既に同名のコンテストフォルダがあると失敗する

## 解答テンプレートの規約（template.py）

- `input = sys.stdin.readline` による高速入力
- `bisect` / `collections`（`Counter`, `defaultdict`, `deque`）/ `heapq` を先出しでimport
- `INF = 10**18`、`MOD = 998244353` を定義済み
- テンプレートおよび `contests/**/*.py` は未使用import（ruffのF401）を意図的に無視する設定になっている（先出しimportを許容するため）

## Lint

`ruff` を使用（line-length 120）。

```
uv run ruff check .
```

## テスト・動作確認

`online-judge-tools`（`oj`）をラップした `tools/download_test.py` / `tools/run_test.py` を使う。サンプルは `contests/<contest_name>/<problem_letter>_test/` に問題ごとに配置される（衝突を避けるため、`oj download` のデフォルト保存先である直下の `test/` は使わない）。

```
./dt <contest_name> <problem_letter> [問題URL]
./rt <contest_name> <problems>
```

- `dt` は `uv run python tools/download_test.py`、`rt` は `uv run python tools/run_test.py` を呼ぶだけの短縮ラッパー（`chmod +x` 済み、リポジトリ外のディレクトリからでも動作する）。フルコマンドで直接叩いても同じ
- `contest_name` は `create_new_contest.py` と同様、数字のみ（例: `426`）を渡すと `abc426` として扱われる
- 問題URLは省略可能。省略時は `https://atcoder.jp/contests/<contest_name>/tasks/<contest_name>_<problem_letter>` の形式で自動生成される（ABC以外の形式など、自動生成に合わないURLを使いたい場合のみ明示的に指定する）
- `problems` は `create_new_contest.py` と同様、複数文字を並べて一括実行可能（例: `ab` でa, b問題を順にテスト）

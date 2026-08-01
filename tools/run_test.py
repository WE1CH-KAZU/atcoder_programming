import subprocess
import sys
from pathlib import Path

# ルートディレクトリ
ROOT = Path(__file__).resolve().parent.parent

CONTESTS = ROOT / "contests"


def main():
    if len(sys.argv) != 3:
        print("Usage: uv run tools/run_test.py <contest> <problems>")
        print("  contest: e.g. abc426")
        print("  problems: テストする問題の文字を並べたもの (e.g. ab)")
        sys.exit(1)

    contest_name, problems = sys.argv[1], sys.argv[2]

    if not contest_name or "/" in contest_name or contest_name in (".", ".."):
        print(f"Invalid contest name: {contest_name}")
        sys.exit(1)

    ok = True

    for problem in problems:
        problem_file = CONTESTS / contest_name / f"{problem}.py"
        if not problem_file.exists():
            print(f"[{problem}] Problem file not found: {problem_file}")
            ok = False
            continue

        test_dir = CONTESTS / contest_name / f"{problem}_test"
        if not test_dir.exists():
            print(f"[{problem}] Test dir not found: {test_dir} (先に download_test.py でサンプルを取得してください)")
            ok = False
            continue

        print(f"[{problem}] Running tests...", flush=True)
        command = f'"{sys.executable}" "{problem_file}"'
        result = subprocess.run(["oj", "test", "-c", command, "-d", str(test_dir)], check=False)
        if result.returncode != 0:
            ok = False

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

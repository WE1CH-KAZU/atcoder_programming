import subprocess
import sys
from pathlib import Path

# ルートディレクトリ
ROOT = Path(__file__).resolve().parent.parent

CONTESTS = ROOT / "contests"


def main():
    if len(sys.argv) != 4:
        print("Usage: uv run tools/download_test.py <contest> <problem> <url>")
        print("  contest: e.g. abc426")
        print("  problem: e.g. a")
        print("  url: 問題ページのURL")
        sys.exit(1)

    contest_name, problem, url = sys.argv[1], sys.argv[2], sys.argv[3]

    if not contest_name or "/" in contest_name or contest_name in (".", ".."):
        print(f"Invalid contest name: {contest_name}")
        sys.exit(1)

    if not problem or "/" in problem or problem in (".", ".."):
        print(f"Invalid problem: {problem}")
        sys.exit(1)

    problem_file = CONTESTS / contest_name / f"{problem}.py"
    if not problem_file.exists():
        print(f"Problem file not found: {problem_file}")
        sys.exit(1)

    test_dir = CONTESTS / contest_name / f"{problem}_test"
    if test_dir.exists():
        print(f"{test_dir} already exists.")
        sys.exit(1)

    test_dir.mkdir(parents=True)

    result = subprocess.run(["oj", "download", url, "-d", str(test_dir)], check=False)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

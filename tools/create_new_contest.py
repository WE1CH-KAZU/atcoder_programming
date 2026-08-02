import shutil
import sys
from pathlib import Path

from contest_utils import resolve_contest_name

# ルートディレクトリ
ROOT = Path(__file__).resolve().parent.parent

TEMPLATE = ROOT / "template.py"
CONTESTS = ROOT / "contests"

DEFAULT_PROBLEMS = "abcdefg"


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: uv run tools/create_new_contest.py <contest_name> [problems]")
        print("  contest_name: e.g. abc426 (数字のみの場合は abc<3桁> として扱う。例: 463 -> abc463)")
        print(f"  problems: 作成する問題の文字を並べたもの (省略時: {DEFAULT_PROBLEMS})")
        sys.exit(1)

    contest_name = resolve_contest_name(sys.argv[1])
    problems = sys.argv[2] if len(sys.argv) == 3 else DEFAULT_PROBLEMS

    if not contest_name or "/" in contest_name or contest_name in (".", ".."):
        print(f"Invalid contest name: {contest_name}")
        sys.exit(1)

    if not TEMPLATE.exists():
        print(f"Template not found: {TEMPLATE}")
        sys.exit(1)

    contest_dir = CONTESTS / contest_name

    if contest_dir.exists():
        print(f"{contest_name} already exists.")
        sys.exit(1)

    contest_dir.mkdir(parents=True)

    for problem in problems:
        dst = contest_dir / f"{problem}.py"
        shutil.copy(TEMPLATE, dst)

    print(f"Created {contest_dir}")


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""Check Markdown files for common quality issues."""

import argparse
import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+\S")
EMPTY_LINK_RE = re.compile(r"\[[^\]]+\]\(\s*\)")


def check_file(path):
    """Return a list of issues found in one Markdown file."""
    issues = []

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return [f"{path}: could not read file: {error}"]

    lines = text.splitlines()

    if not any(HEADING_RE.search(line) for line in lines):
        issues.append(f"{path}:1: missing Markdown heading")

    for line_number, line in enumerate(lines, start=1):
        if line.endswith((" ", "\t")):
            issues.append(
                f"{path}:{line_number}: trailing whitespace"
            )

        if EMPTY_LINK_RE.search(line):
            issues.append(
                f"{path}:{line_number}: empty link destination"
            )

    return issues


def main():
    parser = argparse.ArgumentParser(
        description="Check Markdown files for common quality issues."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Markdown files or directories to check",
    )
    args = parser.parse_args()

    files = []
    had_error = False

    for item in args.paths:
        path = Path(item)

        if not path.exists():
            print(f"Error: {path} does not exist.", file=sys.stderr)
            had_error = True
        elif path.is_dir():
            files.extend(path.rglob("*.md"))
        elif path.is_file() and path.suffix.lower() == ".md":
            files.append(path)
        else:
            print(
                f"Error: {path} is not a Markdown file or directory.",
                file=sys.stderr,
            )
            had_error = True

    files = sorted(set(files))

    if not files:
        if not had_error:
            print("No Markdown files found.")
        return 1

    all_issues = []

    for path in files:
        all_issues.extend(check_file(path))

    if all_issues:
        print("Markdown quality issues found:\n")
        for issue in all_issues:
            print(f"- {issue}")

        print(f"\nFound {len(all_issues)} issue(s).")
        return 1

    print(f"All checks passed! Checked {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

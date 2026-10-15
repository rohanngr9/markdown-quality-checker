
"""Tests for the Markdown quality checker."""

import tempfile
import unittest
from pathlib import Path

from markdown_checker import check_file


class TestMarkdownChecker(unittest.TestCase):
    def check_text(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.md"
            path.write_text(text, encoding="utf-8")
            return check_file(path)

    def test_clean_markdown_passes(self):
        issues = self.check_text("# Example\n\nThis is clean.\n")
        self.assertEqual(issues, [])

    def test_missing_heading_is_reported(self):
        issues = self.check_text("Just some text.\n")
        self.assertTrue(
            any("missing Markdown heading" in issue for issue in issues)
        )

    def test_trailing_whitespace_is_reported(self):
        issues = self.check_text("# Example\nText with spaces   \n")
        self.assertTrue(
            any("trailing whitespace" in issue for issue in issues)
        )

    def test_empty_link_is_reported(self):
        issues = self.check_text("# Example\n[Click here]()\n")
        self.assertTrue(
            any("empty link destination" in issue for issue in issues)
        )


if __name__ == "__main__":
    unittest.main()

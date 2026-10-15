# Markdown Quality Checker

A lightweight Python tool that checks Markdown files for common quality issues.

[![Python Tests](https://github.com/rohanngr9/markdown-quality-checker/actions/workflows/tests.yml/badge.svg)](https://github.com/rohanngr9/markdown-quality-checker/actions/workflows/tests.yml)

## Features

- Detects missing Markdown headings.
- Reports trailing whitespace.
- Finds Markdown links with empty destinations.
- Checks individual Markdown files or directories.
- Runs automated tests using GitHub Actions.

## Requirements

- Python 3.10 or later.
- No third-party dependencies.

## Usage

Check a single Markdown file:

```bash
python markdown_checker.py README.md
```

Check Markdown files in the current directory:

```bash
python markdown_checker.py .
```

## Run Tests

Run the automated tests with:

```bash
python -m unittest -v
```

## Contributing

Suggestions, bug reports, and pull requests are welcome. Please open an issue to discuss larger changes before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Project Status

This is an early-stage open-source project. Contributions, feedback, and suggestions are welcome as it develops.

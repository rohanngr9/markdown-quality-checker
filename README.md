# Markdown Quality Checker

A lightweight Python tool that checks Markdown files for common quality issues.

[![Python Tests](https://github.com/rohanngr9/markdown-quality-checker/actions/workflows/tests.yml/badge.svg)](https://github.com/rohanngr9/markdown-quality-checker/actions/workflows/tests.yml)

## Features

- Detects missing Markdown headings.
- Reports trailing whitespace.
- Finds Markdown links with empty destinations.
- Checks individual files or directories.
- Runs automated tests using GitHub Actions.

## Requirements

- Python 3.10 or later.
- No third-party dependencies.

## Usage

Check a single file:

```bash
python markdown_checker.py README.md
```

Check Markdown files in a directory:

```bash
python markdown_checker.py .
```

## Run tests

```bash
python -m unittest -v
```

## Contributing

Suggestions, bug reports, and pull requests are welcome. Please open an issue to discuss larger changes before submitting a pull request.

## License

This project is intended to use the MIT License. See the `LICENSE` file once it has been added.

## Project status

This is an early-stage open-source project. Contributions and feedback are welcome as it develops.

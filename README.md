# learn-python

A small learning project to practice Python fundamentals and tooling on the path to becoming an Agentic AI developer.

## Project overview

- Source code located under src
- Tests located in [tests] using pytest.

## Tools & configuration

- Python: configured for $3.14$ in [.python-version](.python-version)
- Test runner: pytest (declared in [pyproject.toml](pyproject.toml))
- Linter/formatter: ruff (VS Code default formatter in [.vscode/settings.json](.vscode/settings.json))
- Recommended VS Code extensions in [.vscode/extensions.json](.vscode/extensions.json)
- Install UV Pythong package manager [uv](https://docs.astral.sh/uv/)

## Install uv and dependencies of the project
```sh
pip install uv
uv sync
```

## Quick start

1. Create and activate a virtual environment (using a Python 3.14 interpreter):
```sh
uv sync
uv run src/main.py
```

2. Run tests:
```sh
uvx pytest
```

VS Code is configured to discover tests with pytest and to use the workspace `.venv` interpreter — see [.vscode/settings.json](.vscode/settings.json).

## Development notes

- The main utilities are intentionally tiny and in [src/main.py](src/main.py) so you can iterate quickly and test behavior from [tests/test_main.py](tests/test_main.py).
- Keep the virtual environment out of source control (see [.gitignore](.gitignore)).

## Contributing

- Edit code under `src/`, add tests under `tests/`, and run `pytest`.
- Run `uvx ruff check` to catch style issues if you use ruff locally.
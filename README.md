# Python Base Code Sample

[![Python application](https://github.com/fbrcode/sample-python-tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/fbrcode/sample-python-tests/actions/workflows/python-app.yml)

In order to generate a good a verifiable python code, this base code will provide a good starting point with dependency management, unit testing and code coverage.

## Dependencies

- `pyenv` - Define python versions to work on and manage them
- `poetry` - Python package manager (<https://python-poetry.org/>)

## Install and run

Install dependencies:

```shell
poetry config virtualenvs.in-project true
poetry install
```

Execute main application:

```shell
poetry run start
```

Execute tests on activated virtual environment:

```shell
pytest tests --cov=app --cov-report term-missing --cov-report html --cov-branch -v
```

Execute tests using poetry:

```shell
poetry run pytest tests --cov=app --cov-report term-missing --cov-report html --cov-branch -v
```

Run tests with minimal 80% coverage threshold:

```shell
poetry run pytest tests --cov=app --cov-report term-missing --cov-branch -v --cov-fail-under=80
```

## Setup

### Poetry project setup

Initialize poetry project:

```shell
poetry new sample-python-tests
```

Check poetry environment:

```shell
poetry env info
```

Show package dependencies:

```shell
poetry show --tree
```

## References

- <https://blog.jmswaney.com/poetry-a-yarn-like-package-manager-for-python>

Yarn references:

- `poetry = yarn / npm`
- `pyproject.toml = package.json`
- `poetry.lock = yarn.lock / package-lock.json`

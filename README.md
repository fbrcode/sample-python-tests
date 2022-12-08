# Python Base Code Sample

In order to generate a good a verifiable python code, this base code will provide a good starting point with dependency management, unit testing and code coverage.

## Dependencies

- `pyenv` - Define python versions to work on and manage them
- `poetry` - Python package manager (<https://python-poetry.org/>)
- `pre-commit` - Manage and maintain multi-language pre-commit hooks (<https://pre-commit.com/>)

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

### Pre-commit setup

Install pre-commit on git hooks:

```shell
pre-commit install
```

Generate pre-commit sample configuration file:

```shell
pre-commit sample-config > .pre-commit-config.yaml
```

Run pre-commit on all files:

```shell
pre-commit run --all-files
```

## References

- <https://blog.jmswaney.com/poetry-a-yarn-like-package-manager-for-python>

Yarn references:

- `poetry = yarn / npm`
- `pyproject.toml = package.json`
- `poetry.lock = yarn.lock / package-lock.json`

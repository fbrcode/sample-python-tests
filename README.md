# Python Base Code Sample

In order to generate a good a verifiable python code, this base code will provide a good starting point with dependency management, unit testing and code coverage.

## Dependencies

- `pyenv` - Define python versions to work on and manage them
- `pyenv-virtualenv` - Create virtual environments for python versions
- `poetry` - Python package manager (<https://python-poetry.org/>)

## Setup

### Poetry

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

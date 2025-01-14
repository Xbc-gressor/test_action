# test_action

[![GitHub Actions Demo](https://github.com/jhj0411jhj/test_action/actions/workflows/github-actions-demo.yml/badge.svg)](https://github.com/jhj0411jhj/test_action/actions/workflows/github-actions-demo.yml)
[![Test](https://github.com/jhj0411jhj/test_action/actions/workflows/test.yml/badge.svg)](https://github.com/jhj0411jhj/test_action/actions/workflows/test.yml)
[![Version](https://img.shields.io/github/v/release/jhj0411jhj/test_action.svg)](https://github.com/jhj0411jhj/test_action/releases)
[![codecov](https://codecov.io/gh/Xbc-gressor/test_action/graph/badge.svg?token=nscJuGFy8A)](https://codecov.io/gh/Xbc-gressor/test_action)

This is a repo for testing Github Actions.

This is the `README.md` file.

## For Python Packaging

See [pyproject.toml](pyproject.toml) and [MANIFEST.in](MANIFEST.in).

Tutorial:
* https://packaging.python.org/en/latest/tutorials/packaging-projects/
* https://setuptools.pypa.io/en/latest/userguide/quickstart.html

**Caution:** In this repo, package will be uploaded to TestPyPI 
by GitHub Actions triggered by publishing a release.

Commands:
```bash
python -m pip install --upgrade pip setuptools build twine

# Build
python -m build --sdist --wheel
# For quick build, you may use --no-isolation option.

# Check
tar tf dist/*.tar.gz
unzip -l dist/*.whl
twine check dist/* --strict


# Caution: In this repo, package will be uploaded to TestPyPI 
#          by GitHub Actions triggered by publishing a release.
# Manually upload
# twine upload --repository testpypi dist/*

# Install
pip install -i https://test.pypi.org/simple/ ${package_name}
```

## For pytest

See `[tool.pytest.ini_options]` in [pyproject.toml](pyproject.toml).

Example command:
```bash
pytest -rap test
pytest -h  # show help
```

Documentation: https://docs.pytest.org/

## For GitHub Actions

See [.github/workflows](.github/workflows).

Tutorial:
* https://docs.github.com/en/actions/quickstart
* https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

End of README.md

# tmux_utils

**Helper scripts for working with tmux more efficiently.**

_project status badges:_

[![CI Workflow](https://github.com/bbugyi200/tmux-utils/actions/workflows/ci.yml/badge.svg)](https://github.com/bbugyi200/tmux-utils/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/bbugyi200/tmux-utils/branch/master/graph/badge.svg)](https://codecov.io/gh/bbugyi200/tmux-utils)
[![Documentation Status](https://readthedocs.org/projects/tmux_utils/badge/?version=latest)](https://tmux_utils.readthedocs.io/en/latest/?badge=latest)
[![Package Health](https://snyk.io/advisor/python/tmux_utils/badge.svg)](https://snyk.io/advisor/python/tmux_utils)

_version badges:_

[![Project Version](https://img.shields.io/pypi/v/tmux_utils)](https://pypi.org/project/tmux_utils/)
[![Python Versions](https://img.shields.io/pypi/pyversions/tmux_utils)](https://pypi.org/project/tmux_utils/)
[![Cookiecutter: cc-python](https://img.shields.io/static/v1?label=cc-python&message=2022.01.04&color=d4aa00&logo=cookiecutter&logoColor=d4aa00)](https://github.com/python-boltons/cc-python)
[![Docker: pythonboltons/main](https://img.shields.io/static/v1?label=pythonboltons%20%2F%20main&message=2021.12.22&color=8ec4ad&logo=docker&logoColor=8ec4ad)](https://github.com/python-boltons/docker-python)


## Installation 🗹

### Using `pipx` to Install (preferred)

This package _could_ be installed using pip like any other Python package (in
fact, see the section below this one for instructions on how to do just that).
Given that we only need this package's entry points, however, we recommend that
[pipx][11] be used instead:

```shell
# install and setup pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# install tmux_utils
pipx install tmux_utils
```

### Using `pip` to Install

To install `tmux_utils` using [pip][9], run the following
commands in your terminal:

``` shell
python3 -m pip install --user tmux_utils  # install tmux_utils
```

If you don't have pip installed, this [Python installation guide][10] can guide
you through the process.


## Useful Links 🔗

* [API Reference][3]: A developer's reference of the API exposed by this
  project.
* [cc-python][4]: The [cookiecutter][5] that was used to generate this project.
  Changes made to this cookiecutter are periodically synced with this project
  using [cruft][12].
* [CHANGELOG.md][2]: We use this file to document all notable changes made to
  this project.
* [CONTRIBUTING.md][7]: This document contains guidelines for developers
  interested in contributing to this project.
* [Create a New Issue][13]: Create a new GitHub issue for this project.
* [Documentation][1]: This project's full documentation.


[1]: https://tmux_utils.readthedocs.io/en/latest
[2]: https://github.com/bbugyi200/tmux-utils/blob/master/CHANGELOG.md
[3]: https://tmux_utils.readthedocs.io/en/latest/modules.html
[4]: https://github.com/python-boltons/cc-python
[5]: https://github.com/cookiecutter/cookiecutter
[6]: https://docs.readthedocs.io/en/stable/
[7]: https://github.com/bbugyi200/tmux-utils/blob/master/CONTRIBUTING.md
[8]: https://github.com/bbugyi200/tmux-utils
[9]: https://pip.pypa.io
[10]: http://docs.python-guide.org/en/latest/starting/installation/
[11]: https://github.com/pypa/pipx
[12]: https://github.com/cruft/cruft
[13]: https://github.com/bbugyi200/tmux-utils/issues/new/choose

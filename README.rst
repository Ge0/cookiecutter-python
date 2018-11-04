Python project template
=======================

An opinionated Cookiecutter template for Python projects.

Features
--------

* Package into a ``src/`` directory.
* Command-line argument parsing with argparse_ or Click_.
* Extensive linting with Flake8_, isort_ and Mypy_.
* Code formatting with Black_.
* Unit testing with Pytest_ and Coverage.py_.
* Sphinx_ support with automatic API documentation.
* Automated testing with tox_.
* Git_ repository initialization.
* Continuous integration with `GitLab CI`_ or `Travis CI`_.

References
----------

* https://hynek.me/articles/testing-packaging/
* https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
* https://github.com/python-attrs/attrs
* https://github.com/audreyr/cookiecutter-pypackage/

Quickstart
----------

Install the latest Cookiecutter_ if you haven't installed it yet,
preferably in a virtualenv:

.. code-block:: bash

   pip install cookiecutter

Generate a Python package project:

.. code-block:: bash

    cookiecutter . -o ~/repos/

Configuration
-------------

The following configuration keys are available:

``author_name`` and ``author_email``: Name and email address of the author.
Used in package metadata.

``project_title``: The project display title, with capitals, whitespaces and
whatnots. Used in the README file and in the project documentation.

``project_slug``: The lowercase, dash-separated version of the project title.
Used as toplevel directory name and in package metadata.

``project_description``: A short sentence to describe the project.
Used in the README file, project docstrings and package metadata.

``project_url``: Homepage of the project. Used in package metadata.

``project_license``: License of the project.
Used to generate the license file and in package metadata.

``project_copyright``: Copyright notice.
Used in the project documentation and package metadata.

``project_package``: Name of the toplevel Python package.

``project_prog``: If the project is a program,
the name of the main console script.

``version_scheme``: Versioning scheme used by the project,
either `semantic versioning`_ or `calendar versioning`_.
Used in the project changelog.

``project_version``: The initial project version.

``python_min_version``: Minimum Python version to be supported.

``cli_parser``: Command-line parsing library to use in the entry point,
either Click_ or argparse_. If not set, no console script is generated.

``linter``: Optional source code linter (Flake8_).

``type_checker``: Optional type checker (Mypy_).

``code_formatter``: Optional source code formatter (Black_).

``test_suite``: Optional framework to run unit tests
(Pytest_ with Coverage.py_).

``doc_generator``: Optional documentation generator (Sphinx_).

``vcs``: Optionally initialize a new SCM repository (Git_).

``ci``: Optionally generate a CI configuration file.
Both `GitLab CI`_ and `Travis CI`_ are supported.

.. _argparse: https://docs.python.org/3/library/argparse.html
.. _Black: https://black.readthedocs.io/en/stable/
.. _calendar versioning: https://calver.org/
.. _calver: https://calver.org/
.. _Click: http://click.pocoo.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Coverage.py: https://github.com/nedbat/coveragepy
.. _Flake8: http://flake8.pycqa.org/en/latest/
.. _Git: https://git-scm.com/
.. _GitLab CI: https://docs.gitlab.com/ce/ci/
.. _isort: https://timothycrosley.github.io/isort/
.. _Mypy: http://mypy-lang.org/
.. _Pytest: https://docs.pytest.org/en/latest/
.. _semantic versioning: https://semver.org/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _Travis CI: https://travis-ci.org/

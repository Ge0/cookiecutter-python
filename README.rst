Python project template
=======================

An opinionated Cookiecutter template for Python projects.

This is inspired from

* https://github.com/audreyr/cookiecutter-pypackage/.
* https://hynek.me/articles/testing-packaging/.

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet:

.. code-block:: bash

   $ pip install -U cookiecutter

To generate a new Python project:

.. code-block:: bash

    $ cookiecutter . -o ~/repos/

Configuration
-------------

The following configuration keys are available:

``project_title``: The project display title, with capitals, whitespaces and
whatnots. Used in ``README.rst`` and documentation.

``project_name``: The lowercase, well behaved version of the project title.
Used in documentation and project metadata.

``project_description``: A short sentence to describe the project. Used in
``README.rst``, docstrings and project metadata.

``project_url``: Homepage of the project. Used in project metadata.

``author_name`` and ``author_email``: Name and email address of the author.
Used in project metadata.

``project_license``: License of the project. Used to generate the license file
and in project metadata.

``project_copyright``: Copyright notice. Used in documentation and project
metadata.

``project_prog``: Name of the executable script (aka entry point), if there is
one.

``project_package``: Name of the toplevel Python package.

``project_version``: The initial project version.

``project_cli``: CLI library used for argument parsing, e.g. `Click`_.

``project_doc``: Documentation generator, e.g. `Sphinx`_.

``vcs``: Version control system to manage the project with, e.g. Git.

``gitlab_ci``: Generate a file ``.gitlab-ci.yml``.

``travis_ci``: Generate a file ``.travis.yml``.

.. _Click: http://click.pocoo.org/
.. _Sphinx: http://www.sphinx-doc.org/

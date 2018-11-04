"""{{ cookiecutter.project_description}}"""
{%- if cookiecutter.python_min_version == "2.7" %}

from __future__ import print_function
{%- endif %}

from .__about__ import (
    __author__,
    __copyright__,
    __email__,
{%- if cookiecutter.project_license != "none" %}
    __license__,
{%- endif %}
    __slug__,
    __summary__,
    __title__,
    __uri__,
    __version__,
)


__all__ = [
    "__author__",
    "__copyright__",
    "__email__",
{%- if cookiecutter.project_license != "none" %}
    "__license__",
{%- endif %}
    "__slug__",
    "__summary__",
    "__title__",
    "__uri__",
    "__version__",
    "hello",
]


def hello():
    """Example function."""
    print("Hello world!")

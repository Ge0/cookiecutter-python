"""{{ cookiecutter.project_description}}"""

from .__about__ import (__author__, __copyright__, __email__,{% if cookiecutter.project_license != 'none' %} __license__,{% endif %}
                        __summary__, __title__, __uri__, __version__)


__all__ = [
    '__author__',
    '__copyright__',
    '__email__',
{%- if cookiecutter.project_license != 'none' %}
    '__license__',
{%- endif %}
    '__summary__',
    '__title__',
    '__uri__',
    '__version__',
    'hello',
]


def hello():
    """Return a welcome message."""
    return "Hello world!"

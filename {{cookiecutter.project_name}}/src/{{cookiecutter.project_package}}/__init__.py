"""{{ cookiecutter.project_description}}"""

__version__ = '{{ cookiecutter.project_version }}'

__title__ = '{{ cookiecutter.project_title }}'
__name__ = '{{ cookiecutter.project_name }}'
__description__ = '{{ cookiecutter.project_description }}'
__uri__ = '{{ cookiecutter.project_url }}'

__author__ = '{{ cookiecutter.author_name }}'
__email__ = '{{ cookiecutter.author_email }}'

{% if cookiecutter.project_license != 'none' -%}
__license__ = '{{ cookiecutter.project_license }}'
{% endif -%}
__copyright__ = '{{ cookiecutter.project_copyright }}'


def hello():
    """Return a welcome message."""
    return 'Hello world!'

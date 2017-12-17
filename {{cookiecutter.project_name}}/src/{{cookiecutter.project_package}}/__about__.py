"""Project metadata."""

__version__ = '{{ cookiecutter.project_version }}'

__title__ = '{{ cookiecutter.project_name }}'
__summary__ = '{{ cookiecutter.project_description }}'
__uri__ = '{{ cookiecutter.project_url }}'

__author__ = '{{ cookiecutter.author_name }}'
__email__ = '{{ cookiecutter.author_email }}'

{% if cookiecutter.project_license == 'lgpl' -%}
__license__ = 'LGPL'
{% elif cookiecutter.project_license == 'mit' -%}
__license__ = 'MIT'
{% elif cookiecutter.project_license == 'bsd' -%}
__license__ = 'BSD'
{% endif -%}
__copyright__ = '{{ cookiecutter.project_copyright }}'

"""{{ cookiecutter.project_description}}"""
{%- if cookiecutter.python_min_version == "2.7" %}

from __future__ import print_function
{%- endif %}

__version__ = "{{ cookiecutter.project_version }}"

__title__ = "{{ cookiecutter.project_title }}"
__description__ = "{{ cookiecutter.project_description }}"
__uri__ = "{{ cookiecutter.project_url }}"

__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"
{%- if cookiecutter.project_license == "mit" %}
__license__ = "MIT"
{%- elif cookiecutter.project_license == "gpl" %}
__license__ = "GPL"
{%- endif %}
__copyright__ = "{{ cookiecutter.project_copyright }}"


def hello():
    """Example function."""
    print("Hello world!")

Welcome to {{ cookiecutter.project_title }}
==========={{ cookiecutter.project_title|length * '=' }}

{{ cookiecutter.project_description }}
{%- if cookiecutter.cli_parser != "none" %}

.. command-output:: {{ cookiecutter.project_prog }} --help
{%- endif %}

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   api
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Welcome to {{ cookiecutter.project_title }}
==========={{ cookiecutter.project_title|length * '=' }}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   changelog

{% if cookiecutter.project_cli != 'none' -%}
CLI reference
=============

.. command-output:: {{ cookiecutter.project_prog }} --help

{% endif -%}
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

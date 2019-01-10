from setuptools import setup


setup({% if cookiecutter.python_min_version < "3.0" %}package_dir={"": "src"}{% endif %})

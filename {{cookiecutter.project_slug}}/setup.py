from os.path import dirname, join

from setuptools import find_packages, setup


KEYWORDS = []
CLASSIFIERS = [
    "Intended Audience :: Developers",
{%- if cookiecutter.project_license == "mit" %}
    "License :: OSI Approved :: MIT License",
{%- elif cookiecutter.project_license == "gpl" %}
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
{%- endif %}
{%- if cookiecutter.python_min_version == "2.7" %}
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
{%- endif %}
    "Programming Language :: Python :: 3",
{%- if cookiecutter.python_min_version <= "3.4" %}
    "Programming Language :: Python :: 3.4",
{%- endif %}
{%- if cookiecutter.python_min_version <= "3.5" %}
    "Programming Language :: Python :: 3.5",
{%- endif %}
{%- if cookiecutter.python_min_version <= "3.6" %}
    "Programming Language :: Python :: 3.6",
{%- endif %}
{%- if cookiecutter.python_min_version <= "3.7" %}
    "Programming Language :: Python :: 3.7",
{%- endif %}
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python",
    "Topic :: Software Development",
{%- if cookiecutter.cli_parser != "none" %}
    "Topic :: Utilities",
{%- endif %}
]
DEPENDENCIES = [{% if cookiecutter.cli_parser == "click" %}"click"{% endif %}]
DEV_DEPENDENCIES = [
{%- if cookiecutter.code_formatter == "black" %}
    "black",
{%- endif %}
{%- if cookiecutter.test_suite != "none" %}
    "coverage",
{%- endif %}
{%- if cookiecutter.linter == "flake8" %}
    "flake8",
{%- endif %}
    "isort",
{%- if cookiecutter.type_checker == "mypy" %}
    "mypy",
{%- endif %}
{%- if cookiecutter.test_suite == "pytest" %}
    "pytest",
{%- endif %}
{%- if cookiecutter.doc_generator == "sphinx" %}
    "sphinx",
{%- if cookiecutter.cli_parser != "none" %}
    "sphinxcontrib-programoutput",
{%- endif %}
    "tox",
{%- endif %}
]


PROJECT_DIR = dirname(__file__)
README_FILE = join(PROJECT_DIR, "README.rst")
ABOUT_FILE = join(PROJECT_DIR, "src", "{{ cookiecutter.project_package }}", "__about__.py")


def load_readme():
    with open(README_FILE) as fileobj:
        return fileobj.read()


def load_about():
    about = {}
    with open(ABOUT_FILE) as fileobj:
        exec(fileobj.read(), about)
    return about


ABOUT = load_about()


setup(
    name=ABOUT["__slug__"],
    version=ABOUT["__version__"],
    description=ABOUT["__summary__"],
    long_description=load_readme(),
    author=ABOUT["__author__"],
    author_email=ABOUT["__email__"],
{%- if cookiecutter.project_license != "none" %}
    license=ABOUT["__license__"],
{%- endif %}
    url=ABOUT["__uri__"],
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    package_dir={"": "src"},
    packages=find_packages("src"),
{%- if cookiecutter.cli_parser != "none" %}
    entry_points={
        "console_scripts": ["{{ cookiecutter.project_prog }}={{ cookiecutter.project_package }}.__main__:main"]
    },
{%- endif %}
    install_requires=DEPENDENCIES,
    extras_require={"dev": DEV_DEPENDENCIES},
    python_requires=">={{ cookiecutter.python_min_version }}, {% if cookiecutter.python_min_version == "2.7" %}!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, {% endif %}{% if cookiecutter.python_min_version >= "3.5" %}!=3.4.*, {% endif %}{% if cookiecutter.python_min_version >= "3.6" %}!=3.5.*, {% endif%}{% if cookiecutter.python_min_version >= "3.7" %}!=3.6.*, {% endif %}<4",
    zip_safe=False,
)

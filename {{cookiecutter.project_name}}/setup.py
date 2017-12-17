from os.path import dirname, join

from setuptools import find_packages, setup


CLASSIFIERS = [
    'Intended Audience :: Developers',
{%- if cookiecutter.project_license == 'lgpl' %}
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
{%- elif cookiecutter.project_license == 'mit' %}
    'License :: OSI Approved :: MIT License',
{%- elif cookiecutter.project_license == 'bsd' %}
    'License :: OSI Approved :: BSD License',
{%- endif %}
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python',
    'Topic :: Software Development',
{%- if cookiecutter.project_cli != 'none' %}
    'Topic :: Utilities',
{%- endif %}
]
INSTALL_REQUIRES = [
{%- if cookiecutter.project_cli == 'click' %}
    'click',
{% endif -%}
]


PROJECT_DIR = dirname(__file__)
README_FILE = join(PROJECT_DIR, 'README.rst')
ABOUT_FILE = join(PROJECT_DIR, 'src', '{{ cookiecutter.project_package }}', '__about__.py')


def get_readme():
    with open(README_FILE) as fileobj:
        return fileobj.read()


def get_about():
    about = {}
    with open(ABOUT_FILE) as fileobj:
        exec(fileobj.read(), about)
    return about


ABOUT = get_about()


setup(
    name=ABOUT['__name__'],
    version=ABOUT['__version__'],
    description=ABOUT['__summary__'],
    long_description=get_readme(),
    author=ABOUT['__author__'],
    author_email=ABOUT['__email__'],
{%- if cookiecutter.project_license != 'none' %}
    license=ABOUT['__license__'],
{%- endif %}
    url=ABOUT['__uri__'],
    classifiers=CLASSIFIERS,
    package_dir={'': 'src'},
    packages=find_packages('src'),
{%- if cookiecutter.project_cli != 'none' %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_prog }}={{ cookiecutter.project_package }}.__main__:main',
        ],
    },
{%- endif %}
    install_requires=INSTALL_REQUIRES,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
)

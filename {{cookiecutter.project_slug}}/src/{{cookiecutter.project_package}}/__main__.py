"""Entry point."""
{%- if cookiecutter.cli_parser == "argparse" %}

import argparse
{%- elif cookiecutter.cli_parser == "click" %}

import click
{%- endif %}

from . import hello
from .__about__ import __version__
{%- if cookiecutter.cli_parser == "argparse" %}


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_description }}"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {}".format(__version__),
    )
    parser.parse_args()
    hello()
{%- elif cookiecutter.cli_parser == "click" %}


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def cli():
    """{{ cookiecutter.project_description }}"""
    hello()


def main():
    """Entry point."""
    cli(auto_envvar_prefix="{{ cookiecutter.project_prog.replace('-', '_').upper() }}")
{%- endif %}


if __name__ == "__main__":
    main()

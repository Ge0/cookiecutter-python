"""Entry point."""

{% if cookiecutter.project_cli == 'argparse' -%}
from __future__ import print_function

import argparse
{%- elif cookiecutter.project_cli == 'click' -%}
import click
{%- endif %}

from . import hello


{% if cookiecutter.project_cli == 'argparse' -%}
def main(args=None):
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_description }}")
    parser.parse_args(args)
    print(hello())
{%- elif cookiecutter.project_cli == 'click' -%}
@click.command(context_settings={'help_option_names': ['-h', '--help']})
def main():
    """{{ cookiecutter.project_description }}"""
    click.echo(hello())
{%- endif %}


if __name__ == '__main__':
    main()

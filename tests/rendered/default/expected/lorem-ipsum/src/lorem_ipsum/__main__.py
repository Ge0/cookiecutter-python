"""Entry point."""

import click

from . import __version__, hello


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def cli():
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit."""
    hello()


def main():
    """Entry point."""
    cli(auto_envvar_prefix="LOREM_IPSUM")


if __name__ == "__main__":
    main()

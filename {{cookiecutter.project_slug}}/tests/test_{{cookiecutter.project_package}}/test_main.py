{% if cookiecutter.cli_parser == "argparse" -%}
from {{ cookiecutter.project_package }}.__main__ import main


def test_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "Hello world!\n"
    assert err == ""
{% elif cookiecutter.cli_parser == "click" -%}
from click.testing import CliRunner

from {{ cookiecutter.project_package }}.__main__ import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert result.exit_code == 0
    assert result.output == "Hello world!\n"
{% endif -%}

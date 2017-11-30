{% if cookiecutter.project_cli == 'argparse' -%}
from {{ cookiecutter.project_package }}.__main__ import main


def test_main(capsys):
    main([])
    out, err = capsys.readouterr()
    assert out == 'Hello world!\n'
    assert err == ''
{%- elif cookiecutter.project_cli == 'click' -%}
from click.testing import CliRunner

from {{ cookiecutter.project_package }}.__main__ import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0
    assert result.output == 'Hello world!\n'
{%- endif %}

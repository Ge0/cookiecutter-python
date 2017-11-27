from {{ cookiecutter.project_package }} import hello


def test_hello():
    assert hello() == 'Hello world!'

from pathlib import Path


RENDERED_DIR = Path(__file__).parent / "rendered"


def pytest_generate_tests(metafunc):
    if "case_path" in metafunc.fixturenames:
        metafunc.parametrize("case_path", RENDERED_DIR.iterdir())

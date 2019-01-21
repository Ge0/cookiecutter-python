import shutil
from filecmp import dircmp
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter

PROJECT_PATH = Path(__file__).parent.parent


def check_same_dirs(left, right):
    to_compare = [(left, right)]
    while to_compare:
        left, right = to_compare.pop()
        comp = dircmp(left, right)
        assert not comp.left_only, "extra files on {}".format(left)
        assert not comp.right_only, "extra files on {}".format(right)
        assert not comp.common_funny, "funny files on {} and {}".format(
            left, right
        )
        assert not comp.diff_files, "files differ on {} and {}".format(
            left, right
        )
        assert (
            not comp.funny_files
        ), "could not compare files on {} and {}".format(left, right)
        for subdir in comp.subdirs:
            to_compare.append((left / subdir, right / subdir))


@pytest.mark.freeze_time("2019-01-20T12:34:56", tz_offset=1)
def test_rendered(case_path):
    expected_path = case_path / "expected"
    output_path = case_path / "output"
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir()
    config_path = case_path / "cookiecutter.yaml"
    cookiecutter(
        template=str(PROJECT_PATH),
        no_input=True,
        output_dir=str(output_path),
        config_file=str(config_path),
    )
    for git_path in output_path.glob("**/.git"):
        shutil.rmtree(git_path)
    check_same_dirs(output_path, expected_path)

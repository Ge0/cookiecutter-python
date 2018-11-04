import os
import shutil
from os.path import join
from subprocess import check_call


SOURCE_DIR = join("src", "{{ cookiecutter.project_package }}")
TEST_DIR = join("tests", "test_{{ cookiecutter.project_package }}")


def remove_license():
    if "{{ cookiecutter.project_license }}" == "none":
        os.remove("LICENSE.txt")


def remove_main():
    if "{{ cookiecutter.cli_parser }}" == "none":
        os.remove(join(SOURCE_DIR, "__main__.py"))
        os.remove(join(TEST_DIR, "test_main.py"))


def setup_linter():
    if "{{ cookiecutter.linter }}" != "flake8":
        os.remove(".flake8")


def remove_tests():
    if "{{ cookiecutter.test_suite }} " == "none":
        os.remove(".coveragerc")
        os.remove("pytest.ini")
        shutil.rmtree("tests")


def remove_docs():
    if "{{ cookiecutter.doc_generator }}" == "none":
        shutil.rmtree("docs")


def setup_vcs():
    if "{{ cookiecutter.vcs }}" == "git":
        check_call(["git", "init"])
    else:
        os.remove(".gitignore")
        os.remove("docs/_static/.gitignore")


def setup_ci():
    if "{{ cookiecutter.ci }}" != "gitlab":
        os.remove(".gitlab-ci.yml")
    if "{{ cookiecutter.ci }}" != "travis":
        os.remove(".travis.yml")


if __name__ == "__main__":
    remove_license()
    remove_main()
    setup_linter()
    remove_tests()
    remove_docs()
    setup_vcs()
    setup_ci()

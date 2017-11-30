import os
from os.path import join
from subprocess import DEVNULL, check_call


SOURCE_DIR = join('src', '{{ cookiecutter.project_package }}')
TEST_DIR = 'tests'


def remove_main():
    if '{{ cookiecutter.project_cli }}' != 'none':
        return
    os.remove(join(SOURCE_DIR, '__main__.py'))
    os.remove(join(TEST_DIR, 'test_main.py'))


def remove_license():
    if '{{ cookiecutter.project_license }}' != 'none':
        return
    os.remove('LICENSE.txt')


def pip_compile():
    check_call([
        'pip-compile', '--no-header', '--no-annotate',
        '--output-file', 'requirements.txt', 'requirements.in',
    ], stdout=DEVNULL)


if __name__ == '__main__':
    remove_main()
    remove_license()
    pip_compile()

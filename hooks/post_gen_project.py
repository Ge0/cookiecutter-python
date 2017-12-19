import os
import shutil
from os.path import join
from subprocess import check_call


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


def remove_doc():
    if '{{ cookiecutter.project_doc }}' != 'none':
        return
    shutil.rmtree('docs')


def setup_vcs():
    if '{{ cookiecutter.vcs }}' == 'git':
        check_call(['git', 'init'])
    else:
        os.remove('.gitignore')


def setup_ci():
    if '{{ cookiecutter.gitlab_ci }}' == 'no':
        os.remove('.gitlab-ci.yml')
    if '{{ cookiecutter.travis_ci }}' == 'no':
        os.remove('.travis-ci.yml')


if __name__ == '__main__':
    remove_main()
    remove_license()
    remove_doc()
    setup_vcs()
    setup_ci()

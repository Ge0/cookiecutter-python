from subprocess import DEVNULL, check_call


def pip_compile():
    check_call([
        'pip-compile', '--no-header', '--no-annotate',
        '--output-file', 'requirements.txt', 'requirements.in',
    ], stdout=DEVNULL)


if __name__ == '__main__':
    pip_compile()

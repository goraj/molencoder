from setuptools import setup, find_packages

NAME = 'molencoder'
VERSION = '0.1a'


def read(filename):
    import os
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r') as fi:
        return fi.read()


def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)


setup(
    name=NAME,
    version=VERSION,
    author="Carlos Xavier Hernandez",
    author_email="cxh@stanford.edu",
    url='https://github.com/cxhernandez/%s' % NAME,
    download_url='https://github.com/cxhernandez/%s/tarball/master' % NAME,
    license='MIT',
    packages=find_packages(),
    zip_safe=True,
    install_requires=readlist('requirements.txt'),
    entry_points={
        'console_scripts': [
            '%s = %s.cli.main:main' % (NAME, NAME),
        ],
    },
)

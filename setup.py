#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='py-convox',
    version='0.1.14',
    author='AJ Bowen',
    license='MIT',
    author_email='aj@convox.com',
    packages=find_packages(),
    description='Convox CLI',
    long_description=open('README.rst').read(),
    url='https://github.com/soulshake/py-convox',
    keywords='convox aws',
    install_requires=['click==6.0',
                      'arrow==0.5.4',
                      'requests==2.7.0',
                      'tabulate==0.7.5'],
    entry_points="""\
[console_scripts]
py-convox = convox.__main__:main
""",
    )

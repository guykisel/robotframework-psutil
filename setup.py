#!/usr/bin/env python
from setuptools import setup

short_description = ('Robot Framework wrapper for psutil, '
                     'a cross-platform process and system utilities module')
try:
    description = open('README.rst').read()
except IOError:
    description = short_description


classifiers = """
Development Status :: 1 - Planning
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Software Development :: Testing
Topic :: Software Development :: Quality Assurance
""".strip().splitlines()

setup(
    name='robotframework-psutil',
    package_dir={'': 'robotframework-psutil'},
    packages=['PsutilLibrary'],  # this must be the same as the name above
    version='0.0.1.dev0',
    description=short_description,
    author='Guy Kisel',
    author_email='guy.kisel@gmail.com',
    url='https://github.com/guykisel/robotframework-psutil',
    download_url='https://pypi.python.org/pypi/robotframework-psutil',
    keywords=('robotframework testing '
              'test automation testautomation '
              'atdd bdd psutil'),  # arbitrary keywords
    install_requires=['psutil', 'robotframework', 'wrapt'],
    long_description=description,
    license='MIT',
    classifiers=classifiers,
    platforms='any'
)

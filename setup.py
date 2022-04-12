#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_namespace_packages as find_packages
except ImportError:
    from distutils.core import setup
    find_packages = None

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='credmark-model-framework',
    version='0.8.8',
    description='Credmark model development framework',
    long_description=readme + '\n\n' + history,
    author='Credmark',
    author_email='info@credmark.com',
    url='https://github.com/credmark/credmark-model-framework-py',
    python_requires='>=3.9.0',
    packages=find_packages() if find_packages is not None else ['credmark'],
    package_dir={'credmark':
                 'credmark'},
    include_package_data=True,
    install_requires=required,
    entry_points={
        'console_scripts': [
            'credmark-dev = credmark.cmf.credmark_dev:main'
        ]
    },
    license="MIT",
    zip_safe=False,
    keywords='Credmark crypto risk model develop',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
    ],
    tests_require=[
    ],
    test_suite='',
)

#!/usr/bin/env python

from setuptools import setup

VERSION = '2.1.0-rc1'

setup(
    name='python-slugify2',
    version=VERSION,
    packages=['slugify'],
    url='https://github.com/roniemartinez/python-slugify2',
    download_url='https://github.com/roniemartinez/python-slugify2/tarball/{}'.format(VERSION),
    license='MIT',
    author='Ronie Martinez',
    author_email='ronmarti18@gmail.com',
    description='An attempt fix issue #68 of Python Slugify',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=[],
    extras_require={
        '': 'Unidecode>=0.04.16',
        'unicodecode': 'Unidecode>=0.04.16',
        'text-unidecode': 'text-unidecode==1.2'
    },
    entry_points={'console_scripts': ['slugify=slugify.slugify:main']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)

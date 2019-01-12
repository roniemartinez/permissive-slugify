# python-slugify2

Fork of [un33k/python-slugify](https://github.com/un33k/python-slugify) to fix [issue 68](https://github.com/un33k/python-slugify/issues/68).

<table>
    <tr>
        <td>License</td>
        <td><img src='https://img.shields.io/pypi/l/python-slugify2.svg'></td>
        <td>Version</td>
        <td><img src='https://img.shields.io/pypi/v/python-slugify2.svg'></td>
    </tr>
    <tr>
        <td>Travis CI</td>
        <td><img src='https://travis-ci.org/roniemartinez/python-slugify2.svg?branch=develop'></td>
        <td>Coverage</td>
        <td><img src='https://codecov.io/gh/roniemartinez/python-slugify2/branch/develop/graph/badge.svg'></td>
    </tr>
    <tr>
        <td>AppVeyor</td>
        <td><img src='https://ci.appveyor.com/api/projects/status/srpweajn7vq7hq02/branch/develop?svg=true'></td>
        <td>Supported versions</td>
        <td><img src='https://img.shields.io/pypi/pyversions/python-slugify2.svg'></td>
    </tr>
    <tr>
        <td>Wheel</td>
        <td><img src='https://img.shields.io/pypi/wheel/python-slugify2.svg'></td>
        <td>Implementation</td>
        <td><img src='https://img.shields.io/pypi/implementation/python-slugify2.svg'></td>
    </tr>
    <tr>
        <td>Status</td>
        <td><img src='https://img.shields.io/pypi/status/python-slugify2.svg'></td>
        <td>Downloads</td>
        <td><img src='https://img.shields.io/pypi/dm/python-slugify2.svg'></td>
    </tr>
    <tr>
        <td>Show your support</td>
        <td><a href='https://saythanks.io/to/roniemartinez'><img src='https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg'></a></td>
    </tr>
</table>

## Overview

**Best attempt** to create slugs from unicode strings while keeping it **DRY**.

## Notice

By default, this modules installs and uses [Unidecode](https://github.com/avian2/unidecode) *(GPL)* for its decoding needs.  However if you wish to use [text-unidecode](https://github.com/kmike/text-unidecode) *(GPL & Perl Artistic)* instead, please ensure it is installed prior to `python-slugify` installation.

In cases where both `Unidecode` and `text-unidecode` are installed, `Unidecode` is used as the default decoding module.


## How to install

1. easy_install python-slugify2
2. pip install python-slugify2
3. git clone http://github.com/roniemartinez/python-slugify2
    a. cd python-slugify2
    b. python setup.py install
4. wget https://github.com/roniemartinez/python-slugify2/zipball/master
    a. unzip the downloaded file
    b. cd python-slugify2-*
    c. python setup.py install


## How to use

```python
# -*- coding: utf-8 -*-
from slugify import slugify

txt = "This is a test ---"
r = slugify(txt)
assert r == "this-is-a-test"

txt = '影師嗎'
r = slugify(txt)
assert r == "ying-shi-ma"

txt = 'C\'est déjà l\'été.'
r = slugify(txt)
assert r == "c-est-deja-l-ete"

txt = 'Nín hǎo. Wǒ shì zhōng guó rén'
r = slugify(txt)
assert r == "nin-hao-wo-shi-zhong-guo-ren"

txt = 'Компьютер'
r = slugify(txt)
assert r == "kompiuter"

txt = 'jaja---lol-méméméoo--a'
r = slugify(txt, max_length=9)
assert r == "jaja-lol"

txt = 'jaja---lol-méméméoo--a'
r = slugify(txt, max_length=15, word_boundary=True)
assert r == "jaja-lol-a"

txt = 'jaja---lol-méméméoo--a'
r = slugify(txt, max_length=20, word_boundary=True, separator=".")
assert r == "jaja.lol.mememeoo.a"

txt = 'one two three four five'
r = slugify(txt, max_length=13, word_boundary=True, save_order=True)
assert r == "one-two-three"

txt = 'the quick brown fox jumps over the lazy dog'
r = slugify(txt, stopwords=['the'])
assert r == 'quick-brown-fox-jumps-over-lazy-dog'

txt = 'the quick brown fox jumps over the lazy dog in a hurry'
r = slugify(txt, stopwords=['the', 'in', 'a', 'hurry'])
assert r == 'quick-brown-fox-jumps-over-lazy-dog'

txt = 'thIs Has a stopword Stopword'
r = slugify(txt, stopwords=['Stopword'], lowercase=False)
assert r == 'thIs-Has-a-stopword'

txt = "___This is a test___"
regex_pattern = r'[^-a-z0-9_]+'
r = slugify(txt, regex_pattern=regex_pattern)
assert r == "___this-is-a-test___"

txt = "___This is a test___"
regex_pattern = r'[^-a-z0-9_]+'
r = slugify(txt, separator='_', regex_pattern=regex_pattern)
assert r != "_this_is_a_test_"

txt = '10 | 20 %'
r = slugify(txt, replacements=[['|', 'or'], ['%', 'percent']])
assert r == "10-or-20-percent"

```


## Running the tests

To run the tests against the current environment:

```bash
pytest -v
```

Reference: https://github.com/pypa/setuptools/issues/1139 
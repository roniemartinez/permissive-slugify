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

## Improvements

- Support for `extras_require` and `cmdclass`
- Refactored
- Deploy from Travis CI
- Added Appveyor Integration
- Uses `pytest`
- Uses CodeCov

## How to install

By default, python-slugify2 uses [Unidecode](https://github.com/avian2/unidecode) as decoder which is GPL-licensed.

```bash
pip install python-slugify2
```

### Specifying decoder

You can specify which decoder will be used:

- [Unidecode](https://github.com/avian2/unidecode) - *(GPL-licensed)*.

    ```bash
    pip install python-slugify2[unidecode]
    easy_install python-slugify2[unidecode]
    ```

- [text-unidecode](https://github.com/kmike/text-unidecode) *(GPL & Perl Artistic)*

    ```bash
    pip install python-slugify2[text-unidecode]
    easy_install python-slugify2[text-unidecode]
    ```

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

## References

- [Add ability to specify "default" extras_require](https://github.com/pypa/setuptools/issues/1139)
- [setup.py not ran on wheels](https://stackoverflow.com/questions/40433168/running-custom-code-with-pip-install-fails#comment75920547_40434969)

## Author

- Original - [Val Neekman](https://github.com/un33k/python-slugify)
- Modified by [Ronie Martinez](mailto:ronmarti18@gmail.com)
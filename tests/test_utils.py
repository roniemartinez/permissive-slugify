#!/usr/bin/env python
from slugify.slugify import smart_truncate


def test_smart_truncate_no_max_length():
    txt = '1,000 reasons you are #1'
    r = smart_truncate(txt)
    assert r == txt


def test_smart_truncate_no_seperator():
    txt = '1,000 reasons you are #1'
    r = smart_truncate(txt, max_length=100, separator='_')
    assert r == txt

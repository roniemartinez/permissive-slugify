#!/usr/bin/env python
from slugify.slugify import smart_truncate


def test_smart_truncate_no_max_length():
    txt = '1,000 reasons you are #1'
    slug = smart_truncate(txt)
    assert slug == txt


def test_smart_truncate_no_separator():
    txt = '1,000 reasons you are #1'
    slug = smart_truncate(txt, max_length=100, separator='_')
    assert slug == txt


def test_smart_truncate_with_max_length():
    txt = '1,000 reasons you are #1'*2
    slug = smart_truncate(txt, max_length=20, separator='_', word_boundary=True)
    assert slug == (txt*10)[:20]

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slugify.slugify import slugify


def test_extraneous_separators():
    txt = "This is a test ---"
    r = slugify(txt)
    assert r == "this-is-a-test"

    txt = "___This is a test ---"
    r = slugify(txt)
    assert r == "this-is-a-test"

    txt = "___This is a test___"
    r = slugify(txt)
    assert r == "this-is-a-test"


def test_non_word_characters():
    txt = "This -- is a ## test ---"
    r = slugify(txt)
    assert r == "this-is-a-test"


def test_phonetic_conversion_of_eastern_scripts():
    txt = '影師嗎'
    r = slugify(txt)
    assert r == "ying-shi-ma"


def test_accented_text():
    txt = 'C\'est déjà l\'été.'
    r = slugify(txt)
    assert r == "c-est-deja-l-ete"

    txt = 'Nín hǎo. Wǒ shì zhōng guó rén'
    r = slugify(txt)
    assert r == "nin-hao-wo-shi-zhong-guo-ren"


def test_accented_text_with_non_word_characters():
    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt)
    assert r == "jaja-lol-mememeoo-a"


def test_cyrillic_text():
    txt = 'Компьютер'
    r = slugify(txt)
    assert r == "kompiuter"


def test_max_length():
    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=9)
    assert r == "jaja-lol"

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=15)
    assert r == "jaja-lol-mememe"


def test_max_length_cutoff_not_required():
    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=50)
    assert r == "jaja-lol-mememeoo-a"


def test_word_boundary():
    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=15, word_boundary=True)
    assert r == "jaja-lol-a"

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=17, word_boundary=True)
    assert r == "jaja-lol-mememeoo"

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=18, word_boundary=True)
    assert r == "jaja-lol-mememeoo"

    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=19, word_boundary=True)
    assert r == "jaja-lol-mememeoo-a"


def test_custom_separator():
    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=20, word_boundary=True, separator=".")
    assert r == "jaja.lol.mememeoo.a"


def test_multi_character_separator():
    txt = 'jaja---lol-méméméoo--a'
    r = slugify(txt, max_length=20, word_boundary=True, separator="ZZZZZZ")
    assert r == "jajaZZZZZZlolZZZZZZmememeooZZZZZZa"


def test_save_order():
    txt = 'one two three four five'
    r = slugify(txt, max_length=13, word_boundary=True, save_order=True)
    assert r == "one-two-three"

    txt = 'one two three four five'
    r = slugify(txt, max_length=13, word_boundary=True, save_order=False)
    assert r == "one-two-three"

    txt = 'one two three four five'
    r = slugify(txt, max_length=12, word_boundary=True, save_order=False)
    assert r == "one-two-four"

    txt = 'one two three four five'
    r = slugify(txt, max_length=12, word_boundary=True, save_order=True)
    assert r == "one-two"


def test_stopword_removal():
    txt = 'this has a stopword'
    r = slugify(txt, stopwords=['stopword'])
    assert r == 'this-has-a'


def test_stopword_removal_case_sensitive():
    txt = 'thIs Has a stopword Stopword'
    r = slugify(txt, stopwords=['Stopword'], lowercase=False)
    assert r == 'thIs-Has-a-stopword'


def test_multiple_stopword_occurences():
    txt = 'the quick brown fox jumps over the lazy dog'
    r = slugify(txt, stopwords=['the'])
    assert r == 'quick-brown-fox-jumps-over-lazy-dog'


def test_differently_cased_stopword_match():
    txt = 'Foo A FOO B foo C'
    r = slugify(txt, stopwords=['foo'])
    assert r == 'a-b-c'

    txt = 'Foo A FOO B foo C'
    r = slugify(txt, stopwords=['FOO'])
    assert r == 'a-b-c'


def test_multiple_stopwords():
    txt = 'the quick brown fox jumps over the lazy dog in a hurry'
    r = slugify(txt, stopwords=['the', 'in', 'a', 'hurry'])
    assert r == 'quick-brown-fox-jumps-over-lazy-dog'


def test_stopwords_with_different_separator():
    txt = 'the quick brown fox jumps over the lazy dog'
    r = slugify(txt, stopwords=['the'], separator=' ')
    assert r == 'quick brown fox jumps over lazy dog'


def test_html_entities():
    txt = 'foo &amp; bar'
    r = slugify(txt)
    assert r == 'foo-bar'


def test_starts_with_number():
    txt = '10 amazing secrets'
    r = slugify(txt)
    assert r == '10-amazing-secrets'


def test_contains_numbers():
    txt = 'buildings with 1000 windows'
    r = slugify(txt)
    assert r == 'buildings-with-1000-windows'


def test_ends_with_number():
    txt = 'recipe number 3'
    r = slugify(txt)
    assert r == 'recipe-number-3'


def test_numbers_only():
    txt = '404'
    r = slugify(txt)
    assert r == '404'


def test_numbers_and_symbols():
    txt = '1,000 reasons you are #1'
    r = slugify(txt)
    assert r == '1000-reasons-you-are-1'


def test_regex_pattern_keep_underscore():
    txt = "___This is a test___"
    regex_pattern = r'[^-a-z0-9_]+'
    r = slugify(txt, regex_pattern=regex_pattern)
    assert r == "___this-is-a-test___"


def test_regex_pattern_keep_underscore_with_underscore_as_separator():
    """
    The regex_pattern turns the power to the caller.
    Hence the caller must ensure that a custom separator doesn't clash
    with the regex_pattern.
    """
    txt = "___This is a test___"
    regex_pattern = r'[^-a-z0-9_]+'
    r = slugify(txt, separator='_', regex_pattern=regex_pattern)
    assert r != "_this_is_a_test_"


def test_replacements():
    txt = '10 | 20 %'
    r = slugify(txt, replacements=[['|', 'or'], ['%', 'percent']])
    assert r == "10-or-20-percent"

    txt = 'I ♥ 🦄'
    r = slugify(txt, replacements=[['♥', 'amour'], ['🦄', 'licorne']])
    assert r == "i-amour-licorne"

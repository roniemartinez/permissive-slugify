#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slugify.slugify import slugify


def test_extraneous_separators():
    txt = "This is a test ---"
    slug = slugify(txt)
    assert slug == "this-is-a-test"

    txt = "___This is a test ---"
    slug = slugify(txt)
    assert slug == "this-is-a-test"

    txt = "___This is a test___"
    slug = slugify(txt)
    assert slug == "this-is-a-test"


def test_non_word_characters():
    txt = "This -- is a ## test ---"
    slug = slugify(txt)
    assert slug == "this-is-a-test"


def test_phonetic_conversion_of_eastern_scripts():
    txt = '影師嗎'
    slug = slugify(txt)
    assert slug == "ying-shi-ma"


def test_accented_text():
    txt = 'C\'est déjà l\'été.'
    slug = slugify(txt)
    assert slug == "c-est-deja-l-ete"

    txt = 'Nín hǎo. Wǒ shì zhōng guó rén'
    slug = slugify(txt)
    assert slug == "nin-hao-wo-shi-zhong-guo-ren"


def test_accented_text_with_non_word_characters():
    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt)
    assert slug == "jaja-lol-mememeoo-a"


def test_cyrillic_text():
    txt = 'Компьютер'
    slug = slugify(txt)
    assert slug == "kompiuter"


def test_max_length():
    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt, max_length=9)
    assert slug == "jaja-lol"

    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt, max_length=15)
    assert slug == "jaja-lol-mememe"


def test_max_length_cutoff_not_required():
    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt, max_length=50)
    assert slug == "jaja-lol-mememeoo-a"


def test_word_boundary():
    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt, max_length=15, word_boundary=True)
    assert slug == "jaja-lol-a"

    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt, max_length=17, word_boundary=True)
    assert slug == "jaja-lol-mememeoo"

    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt, max_length=18, word_boundary=True)
    assert slug == "jaja-lol-mememeoo"

    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt, max_length=19, word_boundary=True)
    assert slug == "jaja-lol-mememeoo-a"


def test_custom_separator():
    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt, max_length=20, word_boundary=True, separator=".")
    assert slug == "jaja.lol.mememeoo.a"


def test_multi_character_separator():
    txt = 'jaja---lol-méméméoo--a'
    slug = slugify(txt, max_length=20, word_boundary=True, separator="ZZZZZZ")
    assert slug == "jajaZZZZZZlolZZZZZZmememeooZZZZZZa"


def test_save_order():
    txt = 'one two three four five'
    slug = slugify(txt, max_length=13, word_boundary=True, save_order=True)
    assert slug == "one-two-three"

    txt = 'one two three four five'
    slug = slugify(txt, max_length=13, word_boundary=True, save_order=False)
    assert slug == "one-two-three"

    txt = 'one two three four five'
    slug = slugify(txt, max_length=12, word_boundary=True, save_order=False)
    assert slug == "one-two-four"

    txt = 'one two three four five'
    slug = slugify(txt, max_length=12, word_boundary=True, save_order=True)
    assert slug == "one-two"


def test_stopword_removal():
    txt = 'this has a stopword'
    slug = slugify(txt, stopwords=['stopword'])
    assert slug == 'this-has-a'


def test_stopword_removal_case_sensitive():
    txt = 'thIs Has a stopword Stopword'
    slug = slugify(txt, stopwords=['Stopword'], lowercase=False)
    assert slug == 'thIs-Has-a-stopword'


def test_multiple_stopword_occurences():
    txt = 'the quick brown fox jumps over the lazy dog'
    slug = slugify(txt, stopwords=['the'])
    assert slug == 'quick-brown-fox-jumps-over-lazy-dog'


def test_differently_cased_stopword_match():
    txt = 'Foo A FOO B foo C'
    slug = slugify(txt, stopwords=['foo'])
    assert slug == 'a-b-c'

    txt = 'Foo A FOO B foo C'
    slug = slugify(txt, stopwords=['FOO'])
    assert slug == 'a-b-c'


def test_multiple_stopwords():
    txt = 'the quick brown fox jumps over the lazy dog in a hurry'
    slug = slugify(txt, stopwords=['the', 'in', 'a', 'hurry'])
    assert slug == 'quick-brown-fox-jumps-over-lazy-dog'


def test_stopwords_with_different_separator():
    txt = 'the quick brown fox jumps over the lazy dog'
    slug = slugify(txt, stopwords=['the'], separator=' ')
    assert slug == 'quick brown fox jumps over lazy dog'


def test_html_entities():
    txt = 'foo &amp; bar'
    slug = slugify(txt)
    assert slug == 'foo-bar'


def test_starts_with_number():
    txt = '10 amazing secrets'
    slug = slugify(txt)
    assert slug == '10-amazing-secrets'


def test_contains_numbers():
    txt = 'buildings with 1000 windows'
    slug = slugify(txt)
    assert slug == 'buildings-with-1000-windows'


def test_ends_with_number():
    txt = 'recipe number 3'
    slug = slugify(txt)
    assert slug == 'recipe-number-3'


def test_numbers_only():
    txt = '404'
    slug = slugify(txt)
    assert slug == '404'


def test_numbers_and_symbols():
    txt = '1,000 reasons you are #1'
    slug = slugify(txt)
    assert slug == '1000-reasons-you-are-1'


def test_regex_pattern_keep_underscore():
    txt = "___This is a test___"
    regex_pattern = r'[^-a-z0-9_]+'
    slug = slugify(txt, regex_pattern=regex_pattern)
    assert slug == "___this-is-a-test___"


def test_regex_pattern_keep_underscore_with_underscore_as_separator():
    """
    The regex_pattern turns the power to the caller.
    Hence the caller must ensure that a custom separator doesn't clash
    with the regex_pattern.
    """
    txt = "___This is a test___"
    regex_pattern = r'[^-a-z0-9_]+'
    slug = slugify(txt, separator='_', regex_pattern=regex_pattern)
    assert slug != "_this_is_a_test_"


def test_replacements():
    txt = '10 | 20 %'
    slug = slugify(txt, replacements=[['|', 'or'], ['%', 'percent']])
    assert slug == "10-or-20-percent"

    txt = 'I ♥ 🦄'
    slug = slugify(txt, replacements=[['♥', 'amour'], ['🦄', 'licorne']])
    assert slug == "i-amour-licorne"

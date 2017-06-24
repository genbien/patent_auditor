import pytest
from nlp import lemmatize_word

def test_lemmatize_verb():
	expected = 'dormir'
	computed = lemmatize_word('dors')
	assert expected == computed

def test_lemmatize_noun():
	expected = 'animal'
	computed = lemmatize_word('animaux')
	assert expected == computed

def test_lemmatize_gibberish():
	expected = 'glarghish'
	computed = lemmatize_word('glarghish')
	assert expected == computed

def test_lemmatize_punctuation():
	expected = '!'
	computed = lemmatize_word('!')
	assert expected == computed
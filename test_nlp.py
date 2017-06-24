from nlp import lemmatize_word, tag_word_pos

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

def test_pos_noun():
	expected = 'NOUN'
	computed = tag_word_pos('animaux')
	assert expected == computed

def test_pos_verb():
	expected = 'VERB'
	computed = tag_word_pos('dormir')
	assert expected == computed

def test_pos_adj():
	expected = 'ADJ'
	computed = tag_word_pos('vertes')
	assert expected == computed

def test_pos_gibberish():
	expected = 'UNKNOWN'
	computed = tag_word_pos('glarghish')
	assert expected == computed
from nlp import clean_tag, tag_text


def test_clean_tag_verb():
	computed = clean_tag(['dors', 'VER', 'dormir'])
	expected = { 'word': 'dors', 'lemma': 'dormir', 'pos': 'VERB' }
	assert computed == expected

def test_clean_tag_noun():
	computed = clean_tag(['animaux', 'NOM', 'animal'])
	expected = { 'word': 'animaux', 'lemma': 'animal', 'pos': 'NOUN' }
	assert computed == expected

def test_clean_tag_adjective():
	computed = clean_tag(['vertes', 'ADJ', 'vert'])
	expected = { 'word': 'vertes', 'lemma': 'vert', 'pos': 'ADJ' }
	assert computed == expected

def test_clean_tag_unkown():
	computed = clean_tag(['glarghish', 'NOM', '<unknown>'])
	expected = { 'word': 'glarghish', 'lemma': 'glarghish', 'pos': 'UNKNOWN' }
	assert computed == expected

def test_clean_tag_other():
	computed = clean_tag(['elle', 'DET', 'elle'])
	expected = None
	assert computed == expected

def test_tag_text():
	expected = [
		{ 'word': 'animaux', 'lemma': 'animal', 'pos': 'NOUN' },
		{ 'word': 'dorment', 'lemma': 'dormir', 'pos': 'VERB' },
		{ 'word': 'glarghish', 'lemma': 'glarghish', 'pos': 'UNKNOWN' },
		{ 'word': 'verte', 'lemma': 'vert', 'pos': 'ADJ' },
	]
	computed = tag_text("Les animaux dorment sur la glarghish verte")
	assert expected == computed

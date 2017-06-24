# python - treetagger interface
from treetagger import TreeTagger

tt = TreeTagger(language='french')


def lemmatize_word(word):
	lemma = tt.tag(word)[0][2]
	if lemma == '<unknown>':
		lemma = word
	return lemma

def tag_word_pos(word):
	pos = tt.tag(word)[0][1]
	if tt.tag(word)[0][2] == '<unknown>':
		pos = 'UNKNOWN'
	elif pos == 'NOM':
		pos = 'NOUN'
	elif pos.startswith('VER'):
		pos = 'VERB'
	return pos
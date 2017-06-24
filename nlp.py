# python - treetagger interface
from treetagger import TreeTagger

tt = TreeTagger(language='french')


def lemmatize_word(word):
	lemma = tt.tag(word)[0][2]
	if lemma == '<unknown>':
		lemma = word
	return lemma
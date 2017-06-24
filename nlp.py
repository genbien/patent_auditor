# python - treetagger interface
from treetagger import TreeTagger

tt = TreeTagger(language='french')

def clean_tag(tag):
	word, pos, lemma = tag
	if lemma == '<unknown>':
		return { 'word': word, 'lemma': word, 'pos': 'UNKNOWN' }
	elif pos == 'NOM':
		return { 'word': word, 'lemma': lemma, 'pos': 'NOUN' }
	elif pos.startswith('VER'):
		return { 'word': word, 'lemma': lemma, 'pos': 'VERB' }
	elif pos.startswith('ADJ'):
		return { 'word': word, 'lemma': lemma, 'pos': 'ADJ' }
	return None


def tag_text(text):
	raw_tags = tt.tag(text)

	clean_tags = []
	for tag in raw_tags:
		tag = clean_tag(tag)
		if tag is not None:
			clean_tags.append(tag)
	return clean_tags

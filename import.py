from parse_patent import parse_patent
from nlp import tag_text
from pprint import pprint
import os

root = 'hasIpcCorr'

for path, subdirs, files in os.walk(root):
	for name in files:
		if os.path.join(path, name).endswith('.txt'):
			parsed = parse_patent(os.path.join(path, name))
			print("INSERT INTO patent(code, date) VALUES ('{}', '{}');".format(parsed['code'], parsed['date']))
			tagged = tag_text(parsed['abstract'])
			for t in tagged:
				print("INSERT INTO patent_claim_words(patent_code, word, lemma, pos) VALUES('{}', '{}', '{}', '{}');".format(parsed['code'], t['word'], t['lemma'], t['pos']))



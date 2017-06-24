from parse_patent import parse_patent
from nlp import tag_text
from pprint import pprint
import os

# root = 'hasIpcCorr'
root = 'hasIpcCorr/2000'

for path, subdirs, files in os.walk(root):
	for name in files:
		if os.path.join(path, name).endswith('.txt'):
			parsed = parse_patent(os.path.join(path, name))
			print("INSERT INTO patent(code, date) VALUES ('{}', '{}');".format(parsed['code'], parsed['date']))
			for ipc in parsed['ipc']:
				print("INSERT INTO patent_ipcs(patent_code, ipc) VALUES('{}', '{}');".format(parsed['code'], ipc))
			tagged = tag_text(parsed['abstract'])
			values = []

			for t in tagged:
				values.append("('{}', '{}', '{}', '{}')".format(parsed['code'], t['word'], t['lemma'], t['pos']))
			print("INSERT INTO patent_claim_words(patent_code, word, lemma, pos) VALUES {} ;".format(','.join(values)))



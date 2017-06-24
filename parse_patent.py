
def parse_patent(patent_file):
	patents = {}

	with open(patent_file, 'r') as file:
		patent_data = file.readlines()

	for line in patent_data:
		line = line.rstrip()
		data = line.split(' ::: ')
		if len(data) == 2:
			patents[data[0]] = data[1]

	return patents


stuff = parse_patent('fixtures/patent_definition.txt')
print(stuff)

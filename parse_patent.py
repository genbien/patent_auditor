
def parse_patent(patent_file):
	patent = {}

	with open(patent_file, 'r') as file:
		patent_data = file.readlines()

	for line in patent_data:
		line = line.rstrip()
		data = line.split(' ::: ')
		if len(data) == 2:
			if data[0] not in patent:
				patent[data[0]] = data[1]
			else:
				patent[data[0]] += ','+data[1]
	return patent

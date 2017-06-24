
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

	if 'date' in patent:
		year = patent['date'][0:4]
		month = patent['date'][4:6]
		day = patent['date'][6:8]
		patent['date'] = "{}-{}-{}".format(year, month, day)

	if 'ipc' in patent:
		patent['ipc'] = patent['ipc'].split(',')


	return patent

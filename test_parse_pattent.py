from parse_patent import clean_patent, parse_patent

def test_clean_patent():
	expected = {
		'code': '',
		'basename': '',
		'file': '',
		'ipc': [],
		'abstract': '',
		'date': '1990-01-01',
		'description': '',
		'claims': '',
	}
	computed = clean_patent({})
	assert expected == computed

def test_parse_patent():
	expected = {
		'code': 'ITEMCODE001',
		'basename': 'BASENAME001',
		'file': 'test_path/test_file.xml',
		'ipc': ['A01K 1/015','A01K 1/02'],
		'abstract': 'Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression.',
		'date': '2000-06-28',
		'description': 'Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression.',
		'claims': "On sait depuis longtemps que travailler avec du texte lisible et contenant du sens est source de distractions."
	}
	computed = parse_patent('fixtures/patent_definition.txt')
	assert expected == computed


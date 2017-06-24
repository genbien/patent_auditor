import pytest
from parse_patent import parse_patent

def test_parse_patent():
  expected = {}
  computed = parse_patent('fixtures/patent_definition.txt')
  assert expected == computed


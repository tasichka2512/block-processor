import pytest
from pydantic import ValidationError
from lab6 import Block, Source, Vote, Person

def test_block():
    block = Block(id = 'ADC143B2', view = 3, desc = 'block n', img = b"")
    assert block.id == 'ADC143B'
    assert block.view == 3
    assert block.desc == 'block n'

def test_block_id_len():
    with pytest.raises(ValidationError):
        Block(id='ADC143', view = 3, desc = 'block n', img = b"")

def test_block_id_symbols():
    with pytest.raises(ValidationError):
        Block(id='ADC143x2', view = 3, desc = 'block n', img = b"")

def test_block_view():
    with pytest.raises(ValidationError):
        Block(id='ADC143B2', view = -3, desc = 'block n', img = b"")

def test_block_desc():
    with pytest.raises(ValidationError):
        Block(id='ADC143B2', view = 3, desc = '', img = b"")

def test_source():
    source = Source(id = 2, ip_addr = '12.13.14.15', country_code = 'UK')
    assert source.id == 2
    assert source.ip_addr == '12.13.14.15'
    assert source.country_code == 'UK'

def test_source_id():
    with pytest.raises(ValidationError):
        Source(id = -2, ip_addr = '12.13.14.15', country_code = 'UK')

def test_source_ip_addr_min():
    with pytest.raises(ValidationError):
        Source(id = 2, ip_addr = '1111', country_code = 'UK')

def test_source_ip_addr_max():
    with pytest.raises(ValidationError):
        Source(id = 2, ip_addr = '1234.1234.1234.1234', country_code = 'UK')

def test_source_country_code_len():
    with pytest.raises(ValidationError):
        Source(id = 2, ip_addr = '12.13.14.15', country_code = 'United Kingdom')

def test_source_country_code_symbols():
    with pytest.raises(ValidationError):
        Source(id = 2, ip_addr = '12.13.14.15', country_code = 'uk')

def test_vote():
    vote = Vote(block_id = 'ADC143B2', voter_id = 2, timestamp = 'date', source_id = 2)
    assert vote.block_id == 'ADC143B2'
    assert vote.voter_id == 2
    assert vote.source_id == 2

def test_vote_block_id_len():
    with pytest.raises(ValidationError):
        Vote(block_id = 'ADC143', voter_id = 2, timestamp = 'date', source_id = 2)

def test_vote_block_id_symbols():
    with pytest.raises(ValidationError):
        Vote(block_id = 'ADC143x2', voter_id = 2, timestamp = 'date', source_id = 2)

def test_vote_voter_id():
    with pytest.raises(ValidationError):
        Vote(block_id = 'ADC143B2', voter_id = -2, timestamp = 'date', source_id = 2)

def test_vote_source_id():
    with pytest.raises(ValidationError):
        Vote(block_id = 'ADC143B2', voter_id = 2, timestamp = 'date', source_id = -2)

def test_person():
    person = Person(id = 2, name = 'Jane', addr = 'Kyiv')
    assert person.id == 2
    assert person.name == 'Jane'
    assert person.addr == 'Kyiv'

def test_person_id():
    with pytest.raises(ValidationError):
        Person(id = -2, name = 'Jane', addr = 'Kyiv')

def test_person_name():
    with pytest.raises(ValidationError):
        Person(id = 2, name = 'J', addr = 'Kyiv')

def test_person_addr():
    with pytest.raises(ValidationError):
        Person(id = 2, name = 'Jane', addr = 'K')
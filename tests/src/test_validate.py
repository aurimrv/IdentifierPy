from Identifier import Identifier

def test_valido():
    id = Identifier()
    assert id.validateIdentifier("a1") is True

def test_invalido():
    id = Identifier()
    assert not id.validateIdentifier("123")

def test_invalido_meio():
    id = Identifier()
    assert not id.validateIdentifier("a#23")
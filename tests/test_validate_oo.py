from src.Identifier import Identifier
import pytest
class TestValidateIdentifier:
    _TIMEOUT=0.5 # 500 milliseconds
    def setup_method(self):
        self.id = Identifier()
    
    @pytest.mark.timeout(_TIMEOUT)
    def test_valido(self):
        assert self.id.validateIdentifier("a1")

    @pytest.mark.timeout(_TIMEOUT)
    def test_invalido_primeiro_invalido(self):
        assert not self.id.validateIdentifier("123")
    
    @pytest.mark.timeout(_TIMEOUT)    
    def test_invalido_vazio(self):
        assert not self.id.validateIdentifier("")
    
    @pytest.mark.timeout(_TIMEOUT)
    def test_invalido_maior_que_seis_caracteres(self):
        assert not self.id.validateIdentifier("A1b2C3d")
        
    @pytest.mark.timeout(_TIMEOUT)
    def test_invalido_caracter_nao_letra_ou_digito(self):
        assert not self.id.validateIdentifier("Z#12")
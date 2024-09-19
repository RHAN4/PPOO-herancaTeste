import pytest
from herancaEteste.models.pessoa import Pessoa
from herancaEteste.models.pessoaFisica import PessoaFisica
from herancaEteste.models.endereco import Endereco
from herancaEteste.models.enums.generos import Generos
from herancaEteste.models.enums.unidadeFederativa import UnidadeFederativa
from herancaEteste.models.enums.estadocivil import EstadoCivil

@pytest.fixture
def criar_pessoaFisica():
    pessoaF = PessoaFisica(Pessoa("Marta", "71999482597", "marta@gmail.com", "17/02/1998", 
                                  EstadoCivil(EstadoCivil.CASADO), 
                                  Endereco("Avenida 8", "Em frente a fármacia", "CEP: 48521-258", 
                                           "Salvador", UnidadeFederativa(UnidadeFederativa.BAHIA))))
    return pessoaF

def test_pessoaFisica_atributo_nome(criar_pessoaFisica):
    assert criar_pessoaFisica.pessoa == "Marta"#, "71999482597", "marta@gmail.com"
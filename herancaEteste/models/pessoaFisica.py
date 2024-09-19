from herancaEteste.models.pessoa import Pessoa
from herancaEteste.models.enums.estadocivil import EstadoCivil
from herancaEteste.models.enums.generos import Generos
from herancaEteste.models.endereco import Endereco

class PessoaFisica:
    def __init__(self, pessoa: Pessoa, dataNascimento: str, estadoCivil: EstadoCivil) -> None:
        self.pessoa = pessoa
        self.dataNascimento = dataNascimento
        self.estadoCivil = estadoCivil

    def __str__(self) -> str:
        return ("\nDados da pessoa física: "
                f"\n{self.pessoa.value}"
                f"\nData de nascimento: {self.dataNascimento}"
                f"\nEstado cívil: {self.estadoCivil}")
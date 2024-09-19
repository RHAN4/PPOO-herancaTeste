from herancaEteste.models.endereco import Endereco

class Pessoa:
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\nDados da pessoa: "
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\n{self.endereco}")
        
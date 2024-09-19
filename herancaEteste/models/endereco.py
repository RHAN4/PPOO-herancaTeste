from herancaEteste.models.enums.unidadeFederativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, complemento: str, CEP: str, cidade: str,
                 UF: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.complemento = complemento
        self.CEP = CEP
        self.cidade = cidade
        self.uf = UF    

    def __str__(self) -> str:
        return(f"\nDados do endereço do usuário: "
               f"\nLogradouro: {self.logradouro}"
               f"\nComplemento: {self.complemento}"
               f"\nCEP: {self.CEP}"
               f"\nCidade: {self.cidade}"
               f"\nUnidade federativa: {self.uf}")
        
class Pessoa:
    def __init__(self, id: int):
        self.id = id  
        self.__nome = None  

    @property
    def nome(self):
        return self.__nome  

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome  

pessoa = Pessoa(0)  
pessoa.nome = 'Fulano De Tal'  
print(pessoa.nome)  
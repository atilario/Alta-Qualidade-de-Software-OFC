from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf,):
        self.nome = nome
        self.cpf = cpf

    @abstractmethod
    def exibir_informacoes(self):
        pass
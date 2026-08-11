from abc import ABC, abstractmethod
from modelos.pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, cpf, plano_saude):
        super().__init__(nome, cpf)
        self.plano_saude = plano_saude

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Plano de Saúde: {self.plano_saude}")    
        
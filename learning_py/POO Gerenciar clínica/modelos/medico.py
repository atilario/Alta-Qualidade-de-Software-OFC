from abc import ABC, abstractmethod
from modelos.pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, cpf, crm, especialidade, senha):
        super().__init__(nome, cpf)
        self.crm = crm
        self.especialidade = especialidade
        self.senha = senha

    def autenticar(self, senha):
        return self.senha == senha

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"CRM: {self.crm}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Senha: {self.senha}")
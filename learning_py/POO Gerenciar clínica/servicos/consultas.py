from abc import ABC, abstractmethod

class Consulta(ABC):
    def __init__(self, paciente, medico, data_hora):
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora

    @abstractmethod
    def exibir_informacoes(self):
        pass

    def agendar(self):
        print(f"Consulta agendada para {self.paciente.nome} com o Dr. {self.medico.nome} no dia {self.data_hora}.")

    def cancelar(self):
        print(f"Consulta cancelada para {self.paciente.nome} com o Dr. {self.medico.nome} no dia {self.data_hora}.")

    def listar_consultas(self, consultas):
        print("Consultas agendadas:")
        for consulta in consultas:
            print(f"{consulta.paciente.nome} - Dr. {consulta.medico.nome} - {consulta.data_hora}")

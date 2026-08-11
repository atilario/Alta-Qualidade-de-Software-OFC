from abc import ABC, abstractmethod
from modelos.paciente import Paciente
from servicos.consultas import Consulta
from modelos.medico import Medico


def main():

    print("Bem-vindo ao sistema de gerenciamento de clínica médica!")
    print("O que deseja fazer?")
    print("1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Cadastrar médico")
    print("4. Listar médicos")
    print("5. Marcar consulta")
    print("6. Cancelar consulta")
    print("7. Exibir informações da consulta")
    print("8. Sair")

    pacientes = [
        Paciente("João Silva", "111.111.111-11", "Unimed"),
        Paciente("Maria Souza", "222.222.222-22", "Bradesco Saúde"),
        Paciente("Carlos Lima", "333.333.333-33", "SulAmérica"),
        Paciente("Ana Costa", "444.444.444-44", "Amil")
    ]

    medicos = [
        Medico("Dr. Ricardo Alves", "555.555.555-55",
               "12345", "Cardiologia", "1234"),
        Medico("Dra. Fernanda Rocha", "666.666.666-66",
               "23456", "Dermatologia", "1234"),
        Medico("Dr. Marcelo Santos", "777.777.777-77",
               "34567", "Ortopedia", "1234"),
        Medico("Dra. Juliana Mendes", "888.888.888-88",
               "45678", "Pediatria", "1234")
    ]

    while True:
        print("Bem-vindo ao sistema de gerenciamento de clínica médica!")
        print("O que deseja fazer?")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Cadastrar médico")
        print("4. Listar médicos")
        print("5. Marcar consulta")
        print("6. Cancelar consulta")
        print("7. Exibir informações da consulta")
        print("8. Sair")
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            nome = input("Digite o nome do paciente: ")
            cpf = input("Digite o CPF do paciente: ")
            plano_saude = input("Digite o plano de saúde do paciente: ")
            paciente = Paciente(nome, cpf, plano_saude)
            pacientes.append(paciente)
            print("Paciente cadastrado com sucesso!")

        elif escolha == "2":
            print("Lista de pacientes:")
            for paciente in pacientes:
                paciente.exibir_informacoes()
                print()

        elif escolha == "3":
            nome = input("Digite o nome do médico: ")
            cpf = input("Digite o CPF do médico: ")
            crm = input("Digite o CRM do médico: ")
            especialidade = input("Digite a especialidade do médico: ")
            senha = input("Digite a senha do médico: ")
            medico = Medico(nome, cpf, crm, especialidade, senha)
            medicos.append(medico)
            print("Médico cadastrado com sucesso!")

        elif escolha == "4":
            print("Lista de médicos:")
            for medico in medicos:
                medico.exibir_informacoes()
                print()
        elif escolha == "5":
            # buscar por cpf do paciente

            cpf_paciente = input("Digite o CPF do paciente: ")
            nome_medico = input("Digite o nome do médico: ")
            data_hora = input(
                "Digite a data e hora da consulta (dd/mm/aaaa hh:mm): ")
            paciente = next(
                (p for p in pacientes if p.cpf == cpf_paciente), None)
            medico = next((m for m in medicos if m.nome == nome_medico), None)
            if paciente and medico:
                consulta = Consulta(paciente, medico, data_hora)
                consulta.agendar()
            else:
                print("Paciente ou médico não encontrado.")

        elif escolha == "6":
            cpf_paciente = input("Digite o CPF do paciente: ")
            nome_medico = input("Digite o nome do médico: ")
            data_hora = input(
                "Digite a data e hora da consulta (dd/mm/aaaa hh:mm): ")
            paciente = next(
                (p for p in pacientes if p.cpf == cpf_paciente), None)
            medico = next((m for m in medicos if m.nome == nome_medico), None)
            if paciente and medico:
                consulta = Consulta(paciente, medico, data_hora)
                consulta.cancelar()
            else:
                print("Paciente ou médico não encontrado.")

        elif escolha == "7":
            cpf_paciente = input("Digite o CPF do paciente: ")
            nome_medico = input("Digite o nome do médico: ")
            data_hora = input(
                "Digite a data e hora da consulta (dd/mm/aaaa hh:mm): ")
            paciente = next(
                (p for p in pacientes if p.cpf == cpf_paciente), None)
            medico = next((m for m in medicos if m.nome == nome_medico), None)
            if paciente and medico:
                consulta = Consulta(paciente, medico, data_hora)
                consulta.exibir_informacoes()
            else:
                print("Paciente ou médico não encontrado.")

        elif escolha == "8":
            print("Saindo do sistema. Até mais!")
            break


main()

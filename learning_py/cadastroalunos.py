# uso pratico de dict

alunos = []

while True:
    print("\nCadastro de Aluno")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    curso = input("Digite seu curso: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if continuar != "s":
        break

print("\nLista de alunos cadastrados:")

for aluno in alunos:
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Curso:", aluno["curso"])
    print("----------------------------")

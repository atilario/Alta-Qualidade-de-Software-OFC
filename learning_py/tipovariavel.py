# ================================
# RANGE → sequência de números
# ================================

print("Exemplo de range:")
for numero in range(1, 6):  # gera números de 1 até 5
    print(numero)


# ================================
# LIST → sequência de valores mutáveis
# (pode aumentar e diminuir automaticamente)
# ================================

print("\nExemplo de list:")
lista = [10, 20, 30]
print("Lista inicial:", lista)

lista.append(40)  # adiciona elemento
print("Depois do append:", lista)

lista.remove(20)  # remove elemento
print("Depois do remove:", lista)


# ================================
# TUPLE → coleção ordenada (imutável)
# Ex: coordenadas
# ================================

print("\nExemplo de tuple:")
coordenadas = (12.5, -38.3)  # latitude e longitude
print("Coordenadas:", coordenadas)


# ================================
# DICT → coleção chave/valor (tipo tabela hash)


print("\nExemplo de dict:")
aluno = {
    "nome": "Átila",
    "idade": 19,
    "curso": "Engenharia de Computação"
}

print("Nome:", aluno["nome"])
print("Curso:", aluno["curso"])


# ================================

# SET → coleção de valores únicos (sem duplicatas) precisa usar {}

print("\nExemplo de set:")
números = {1, 2, 3, 3, 2, 1}
print("Set (sem duplicatas):", números)
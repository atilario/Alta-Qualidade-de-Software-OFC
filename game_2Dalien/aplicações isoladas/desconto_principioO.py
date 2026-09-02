from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class Normal(Desconto):
    def calcular(self, valor):
        return valor * 0.10

class Vip(Desconto):
    def calcular(self, valor):
        return valor * 0.20

class Premium(Desconto):
    def calcular(self, valor):
        return valor * 0.30


def main():
    tipo = input("Digite o tipo de cliente (normal, vip, premium): ").lower()
    valor_compra = float(input("Digite o valor da compra: R$ "))

    if tipo == "normal":
        estrategia = Normal()
    elif tipo == "vip":
        estrategia = Vip()
    elif tipo == "premium":
        estrategia = Premium()
    else:
        print("Tipo inválido! Escolha normal, vip ou premium.")
        return

    desconto = estrategia.calcular(valor_compra)
    valor_final = valor_compra - desconto

    print(f"\nCliente: {tipo}")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")


main()
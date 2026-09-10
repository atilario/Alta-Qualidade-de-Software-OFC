from abc import ABC, abstractmethod

#INTERFACES

class IDesconto(ABC):

    @abstractmethod
    def calcular(self, valor: float) -> float:
        raise NotImplementedError

class ICupom(ABC):

    @abstractmethod
    def aplicar_cupom(self, codigo: str) -> bool:
        raise NotImplementedError

class IVIP(ABC):

    @abstractmethod
    def validar_usuario_vip(self, usuario: str) -> bool:
        raise NotImplementedError

#DESCONTOSSSS

class DescontoNormal(IDesconto):

    def calcular(self, valor: float) -> float:
        return valor * 0.10

class DescontoVIP(IDesconto, ICupom, IVIP):

    def calcular(self, valor: float) -> float:
        return valor * 0.20

    def aplicar_cupom(self, codigo: str) -> bool:
        return True

    def validar_usuario_vip(self, usuario: str) -> bool:
        return usuario.lower() == "vip"

class DescontoPremium(IDesconto, ICupom):

    def calcular(self, valor: float) -> float:
        return valor * 0.30

    def aplicar_cupom(self, codigo: str) -> bool:
        return True

# APLICAÇÕES

def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)

def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)

class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)

Desconto = IDesconto
Normal = DescontoNormal
Vip = DescontoVIP
Premium = DescontoPremium

#TESTE

def teste():
    valor = 100.0

    print("=" * 60)
    print("DEMONSTRAÇÃO DOS PRINCÍPIOS SOLID (LSP, ISP e DIP)")
    print("=" * 60)

    print("\n--- 1. LSP (Liskov Substitution Principle) ---")
    print("Normal: ", aplicar_desconto(DescontoNormal(), valor))
    print("VIP:    ", aplicar_desconto(DescontoVIP(), valor))
    print("Premium:", aplicar_desconto(DescontoPremium(), valor))

    print("\n--- 2. ISP (Interface Segregation Principle) ---")
    normal = DescontoNormal()
    vip = DescontoVIP()
    print("Desconto normal:", aplicar_desconto(normal, valor))
    print("Desconto VIP:   ", aplicar_desconto(vip, valor))
    print("Cupom VIP:      ", aplicar_cupom(vip, "DESC10"))

    print("\n--- 3. DIP (Dependency Inversion Principle) ---")
    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVIP())
    pedido_premium = Pedido(DescontoPremium())

    print("Total Pedido Normal:  R$", pedido_normal.total(valor))
    print("Total Pedido VIP:     R$", pedido_vip.total(valor))
    print("Total Pedido Premium: R$", pedido_premium.total(valor))
    print("=" * 60)


if __name__ == "__main__":
    teste()

from src.desconto import IDesconto


class StubSemDesconto(IDesconto):
    def calcular(self, valor):
        return 0


class StubShip:
    """Dublê (Stub) da nave para testar eventos sem depender de Surface ou imagens do Pygame."""

    def __init__(self) -> None:
        self.moving_right = False
        self.moving_left = False

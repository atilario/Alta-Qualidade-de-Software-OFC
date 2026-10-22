import pygame

from src.desconto import Pedido
from src.game_events import GameEventHandler
from tests.doubles import StubSemDesconto, StubShip

# --- Testes de Pedido com Dublês (Slides 8 e 10) ---

def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100


def test_pedido_com_mock_desconto(mocker):
    mock_desconto = mocker.Mock()  # Criar mock do desconto
    mock_desconto.calcular.return_value = 10  # Definir comportamento do mock

    pedido = Pedido(mock_desconto)  # Injetar mock no Pedido
    resultado = pedido.total(100)  # Executar método

    assert resultado == 90  # Verificar resultado final

    mock_desconto.calcular.assert_called()  # verifica se o método calcular foi chamado
    mock_desconto.calcular.assert_called_once_with(100)  # verifica se o método calcular foi chamado uma única vez com o valor 100
    assert mock_desconto.calcular.call_count == 1  # verifica se o método calcular foi chamado exatamente uma vez


# --- Testes no jogo Game2D_Alien com Dublês (Slide 15 - Momento Interativo) ---

def test_game_event_handler_com_stub_ship():
    """Stub no Game2D_Alien: verifica se a nave ativa moving_right ao receber evento de seta para a direita."""
    stub_ship = StubShip()
    handler = GameEventHandler(ship=stub_ship, bullet_manager=None)

    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
    handler._handle_keydown(event)

    assert stub_ship.moving_right is True


def test_game_event_handler_com_mock_bullet_manager(mocker):
    """Mock no Game2D_Alien: verifica se o método _fire_bullet do bullet_manager foi chamado ao teclar ESPAÇO."""
    mock_bullet_manager = mocker.Mock()
    stub_ship = StubShip()
    handler = GameEventHandler(ship=stub_ship, bullet_manager=mock_bullet_manager)

    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    handler._handle_keydown(event)

    mock_bullet_manager._fire_bullet.assert_called_once()

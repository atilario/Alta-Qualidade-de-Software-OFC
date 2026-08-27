import pygame

class GameRenderer:
    def __init__(self, screen, bg_color, ship, bullets, aliens) -> None:
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()  # Deixa a tela mais recente visível

    def _draw_bullets(self):
        """Desenha todos os projéteis na tela."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
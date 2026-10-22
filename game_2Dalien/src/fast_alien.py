from alien import Alien

class FastAlien(Alien):
    """Representa um alienígena rápido."""

    def update(self):
        """Move o alienígena para a direita."""
        self.x += self.settings.fast_alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x
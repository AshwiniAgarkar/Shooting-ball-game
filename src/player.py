import pygame
from .settings import PLAYER_SPEED
from .colors import GREEN, BLUE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 50
        self.height = 50

        # Glow player style
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        pygame.draw.rect(self.image, GREEN, (0, 0, self.width, self.height), border_radius=12)
        pygame.draw.rect(self.image, BLUE, (0, 0, self.width, self.height), 3, border_radius=12)

        self.rect = self.image.get_rect(center=(x, y))
        self.speed = PLAYER_SPEED

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Screen boundaries
        self.rect.x = max(0, min(self.rect.x, 750))
        self.rect.y = max(0, min(self.rect.y, 550))

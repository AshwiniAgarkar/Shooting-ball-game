import pygame
import random
from .settings import ENEMY_SPEED
from .colors import RED, WHITE

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.size = 40
        self.image = pygame.Surface([self.size, self.size], pygame.SRCALPHA)
        pygame.draw.rect(self.image, RED, (0, 0, self.size, self.size), border_radius=10)
        pygame.draw.rect(self.image, WHITE, (0, 0, self.size, self.size), 3, border_radius=10)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 760)
        self.rect.y = -50
        self.speed = ENEMY_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 620:
            self.kill()

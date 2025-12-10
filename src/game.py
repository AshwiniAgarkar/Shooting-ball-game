import pygame
import random
from .settings import WIDTH, HEIGHT, FPS, BULLET_SPEED
from .player import Player
from .enemy import Enemy
from .ui import draw_text, draw_score, draw_game_over
from .colors import BG_SPACE, GREEN, WHITE, YELLOW


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Galaxy Gaming")
        self.clock = pygame.time.Clock()

        # Player
        self.player = Player(WIDTH // 2, HEIGHT - 80)

        # Groups
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = []

        self.all_sprites.add(self.player)

        self.score = 0
        self.running = True
        self.show_welcome_screen()
        # --------------------------

    
    # ------------------------------
    def show_welcome_screen(self):
        waiting = True

        while waiting:
            self.screen.fill(BG_SPACE)

            draw_text(self.screen, "WELCOME TO", 48, WIDTH // 2, HEIGHT // 2 - 60)
            draw_text(self.screen, "THE GAMING ZONE", 55, WIDTH // 2, HEIGHT // 2)
            draw_text(self.screen, "Press ENTER to Start", 32, WIDTH // 2, HEIGHT // 2 + 80)
            draw_text(self.screen, "Created by Ashwini Agarkar", 24, WIDTH // 2, HEIGHT - 40)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # ENTER key
                        waiting = False

    # ------------------------------

    def spawn_enemy(self):
        enemy = Enemy()
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def shoot(self):
        bullet = pygame.Rect(self.player.rect.centerx - 3,
                             self.player.rect.y - 10, 6, 12)
        self.bullets.append(bullet)

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.shoot()

            keys = pygame.key.get_pressed()

            # Spawn enemies
            if random.randint(1, 20) == 1:
                self.spawn_enemy()

            # Update
            self.player.update(keys)
            self.enemies.update()

            # Move bullets
            for bullet in self.bullets[:]:
                bullet.y -= BULLET_SPEED
                if bullet.y < -20:
                    self.bullets.remove(bullet)

            # Bullet collisions
            for enemy in self.enemies:
                for bullet in self.bullets[:]:
                    if enemy.rect.colliderect(bullet):
                        enemy.kill()
                        self.bullets.remove(bullet)
                        self.score += 10

            # Player collision
            for enemy in self.enemies:
                if enemy.rect.colliderect(self.player.rect):
                    self.game_over()

            self.draw()

        pygame.quit()

    def draw(self):
        self.screen.fill(BG_SPACE)

        # Stars
        for _ in range(50):
            pygame.draw.circle(
                self.screen, WHITE,
                (random.randint(0, WIDTH), random.randint(0, HEIGHT)), 1
            )

        # Bullets
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, GREEN, bullet)

        # Draw sprites
        self.all_sprites.draw(self.screen)

        # Score text
        draw_score(self.screen, self.score)

        pygame.display.flip()

    def game_over(self):
        self.screen.fill((0, 0, 0))
        draw_game_over(self.screen)
        pygame.display.flip()
        pygame.time.wait(2000)
        self.running = False

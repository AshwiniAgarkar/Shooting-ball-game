import pygame
from .colors import WHITE, YELLOW, PINK

def draw_text(screen, text, size, x, y, center=True):
    font = pygame.font.SysFont("arial", size, bold=True)
    label = font.render(text, True, PINK)

    rect = label.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    screen.blit(label, rect)

def draw_score(screen, score):
    font = pygame.font.SysFont("consolas", 26, bold=True)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def draw_game_over(screen):
    font = pygame.font.SysFont("arialblack", 60)
    text = font.render("GAME OVER!", True, PINK)
    screen.blit(text, (250, 260))

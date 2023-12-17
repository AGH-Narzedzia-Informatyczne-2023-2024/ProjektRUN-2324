import pygame
import sys
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prawie Mario")

# Kolory
white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Gracz
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 5
jump_height = 15
fall_speed = 0
jumping = False

# Platformy
platform_width = 100
platform_height = 20
platforms = [
    (screen_width // 2 - platform_width // 2, screen_height - platform_height - 50),
    (200, 400),
    (500, 300),
    (50, 200),
    (600, 150)
]

# Monety
coin_size = 30
coins = [(random.randint(0, screen_width - coin_size), random.randint(100, screen_height - coin_size - 50))
         for _ in range(5)]

# Przeszkody
obstacle_size = 50
obstacles = [(random.randint(0, screen_width - obstacle_size), random.randint(100, screen_height - obstacle_size - 50))
             for _ in range(3)]

# Grawitacja
gravity = 1

# Wynik
score = 0

# Główna pętla gry
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        fall_speed = -jump_height

    # Grawitacja
    fall_speed += gravity
    player_y += fall_speed

    # Sprawdzenie kolizji z platformami
    on_platform = False
    for platform in platforms:
        if platform[0] < player_x < platform[0] + platform_width and platform[1] < player_y < platform[1] + platform_height:
            on_platform = True
            player_y = platform[1] - player_size
            fall_speed = 0
            break

    if not on_platform and player_y > screen_height - player_size:
        player_y = screen_height - player_size
        fall_speed = 0

    # Sprawdzenie kolizji z monetami
    for coin in coins:
        if (coin[0] <= player_x <= coin[0] + coin_size or coin[0] <= player_x + player_size <= coin[0] + coin_size) \
                and (coin[1] <= player_y <= coin[1] + coin_size or coin[1] <= player_y + player_size <= coin[1] + coin_size):
            coins.remove(coin)
            score += 10

    # Sprawdzenie kolizji z przeszkodami
    for obstacle in obstacles:
        if (obstacle[0] <= player_x <= obstacle[0] + obstacle_size or obstacle[0] <= player_x + player_size <= obstacle[0] + obstacle_size) \
                and (obstacle[1] <= player_y <= obstacle[1] + obstacle_size or obstacle[1] <= player_y + player_size <= obstacle[1] + obstacle_size):
            pygame.time.delay(1000)
            running = False

    # Rysowanie tła
    screen.fill(white)

    # Rysowanie gracza
    pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))

    # Rysowanie platform
    for platform in platforms:
        pygame.draw.rect(screen, blue, (platform[0], platform[1], platform_width, platform_height))

    # Rysowanie monet
    for coin in coins:
        pygame.draw.rect(screen, yellow, (coin[0], coin[1], coin_size, coin_size))

    # Rysowanie przeszkód
    for obstacle in obstacles:
        pygame.draw.rect(screen, white, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))

    # Wyświetlanie wyniku
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, blue)
    screen.blit(text, (10, 10))

    # Aktualizacja ekranu
    pygame.display.flip()

    # Ustawienie liczby klatek na sekundę
    clock.tick(60)

# Zakończenie gry
pygame.quit()
sys.exit()

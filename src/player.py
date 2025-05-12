import pygame
import sys
import os
from player import Player

# Path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, '..', 'assets')
IMG_DIR = os.path.join(ASSETS_DIR, 'images')
CHAR_DIR = os.path.join(IMG_DIR, 'Characters')
TILESET_DIR = os.path.join(IMG_DIR, 'tilesets')

# Setup Pygame
pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Wandermaze")
clock = pygame.time.Clock()

TILE_SIZE = 32

# Load tileset (satu baris tileset A5 untuk awal)
tileset_image = pygame.image.load(os.path.join(TILESET_DIR, "FG_Cellar_A5.png")).convert_alpha()
tiles = []
for i in range(tileset_image.get_width() // TILE_SIZE):
    tiles.append(tileset_image.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE)))

# Tilemap 10x10
tilemap = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 2, 2, 2, 2, 2, 2, 1, 0],
    [0, 1, 2, 3, 3, 3, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 3, 3, 3, 2, 1, 0],
    [0, 1, 2, 2, 2, 2, 2, 2, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Inisialisasi player
player = Player(CHAR_DIR)
player_group = pygame.sprite.Group(player)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Gambar tilemap
    for y, row in enumerate(tilemap):
        for x, tile_id in enumerate(row):
            if tile_id < len(tiles):
                screen.blit(tiles[tile_id], (x * TILE_SIZE, y * TILE_SIZE))

    # Gambar player
    player_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)

import pygame
import sys
import os

# Setup path dasar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, '..', 'assets')
IMG_DIR = os.path.join(ASSETS_DIR, 'images')
CHAR_DIR = os.path.join(IMG_DIR, 'Characters')
TILESET_DIR = os.path.join(IMG_DIR, 'tilesets')

# Inisialisasi
pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Wandermaze")
clock = pygame.time.Clock()

TILE_SIZE = 32

# Load tileset (pakai tileset A5 dulu, nanti bisa gabungkan)
tileset_image = pygame.image.load(os.path.join(TILESET_DIR, "FG_Cellar_A5.png")).convert_alpha()

# Ambil tile per 32x32 dari satu baris tileset
tiles = []
tileset_cols = tileset_image.get_width() // TILE_SIZE
for i in range(tileset_cols):
    tile = tileset_image.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE))
    tiles.append(tile)

# Load karakter
player_img = pygame.image.load(os.path.join(CHAR_DIR, "Knight_10_Walk_Down.png")).convert_alpha()
player_frame = player_img.subsurface((0, 0, TILE_SIZE, TILE_SIZE))
player_pos = [5 * TILE_SIZE, 5 * TILE_SIZE]

# Array tilemap
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

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gerakan bebas tanpa collision
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 2
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 2
    if keys[pygame.K_UP]:
        player_pos[1] -= 2
    if keys[pygame.K_DOWN]:
        player_pos[1] += 2

    # Gambar tilemap
    for y, row in enumerate(tilemap):
        for x, tile_id in enumerate(row):
            if tile_id < len(tiles):
                screen.blit(tiles[tile_id], (x * TILE_SIZE, y * TILE_SIZE))

    # Gambar karakter
    screen.blit(player_frame, player_pos)

    pygame.display.flip()
    clock.tick(60)

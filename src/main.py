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

TILE_SIZE = 32

# Array tilemap
tilemap = [
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 2, 0, 0, 2, 2, 0, 1],
    [1, 0, 2, 1, 1, 1, 1, 2, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 2, 1, 1, 1, 1, 2, 0, 1],
    [1, 0, 2, 2, 0, 0, 2, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Hitung ukuran layar berdasarkan ukuran tilemap
SCREEN_WIDTH = len(tilemap[0]) * TILE_SIZE
SCREEN_HEIGHT = len(tilemap) * TILE_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wandermaze")
clock = pygame.time.Clock()

# Load tileset
tileset_image = pygame.image.load(os.path.join(TILESET_DIR, "TS1.png")).convert_alpha()

# Ambil tile per 32x32 dari satu baris tileset
tiles = []
tileset_cols = tileset_image.get_width() // TILE_SIZE
for i in range(tileset_cols):
    tile = tileset_image.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE))
    tiles.append(tile)

# Load karakter
player_img = pygame.image.load(os.path.join(CHAR_DIR, "Knight_10_Walk_Down.png")).convert_alpha()
player_frame = player_img.subsurface((0, 0, TILE_SIZE, TILE_SIZE))
player_pos = [TILE_SIZE, TILE_SIZE]  # Posisi awal pemain (x, y)

# Fungsi collision
def can_move(new_x, new_y):
    tile_x = new_x // TILE_SIZE
    tile_y = new_y // TILE_SIZE

    if tile_x < 0 or tile_y < 0 or tile_x >= len(tilemap[0]) or tile_y >= len(tilemap):
        return False

    return tilemap[tile_y][tile_x] == 0 or tilemap[tile_y][tile_x] == 2

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gerakan dengan collision detection
    keys = pygame.key.get_pressed()
    new_x, new_y = player_pos[0], player_pos[1]
    if keys[pygame.K_LEFT]:
        new_x -= 2
    if keys[pygame.K_RIGHT]:
        new_x += 2
    if keys[pygame.K_UP]:
        new_y -= 2
    if keys[pygame.K_DOWN]:
        new_y += 2

    # Periksa collision sebelum memperbarui posisi
    if can_move(new_x, player_pos[1]):
        player_pos[0] = new_x
    if can_move(player_pos[0], new_y):
        player_pos[1] = new_y

    # Gambar tilemap
    for y, row in enumerate(tilemap):
        for x, tile_id in enumerate(row):
            if tile_id < len(tiles):
                screen.blit(tiles[tile_id], (x * TILE_SIZE, y * TILE_SIZE))

    # Gambar karakter
    screen.blit(player_frame, player_pos)

    pygame.display.flip()
    clock.tick(60)

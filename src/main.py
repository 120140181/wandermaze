import pygame
import json
from pathlib import Path

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
TILE_SIZE = 16
SCALE = 2
SCALED_TILE_SIZE = TILE_SIZE * SCALE

# Path setup
BASE_DIR = Path(__file__).resolve().parent.parent
LDTK_PATH = BASE_DIR / "assets" / "images" / "tilesets" / "levels.ldtk"
TILESET_BASE_PATH = BASE_DIR / "assets" / "images" / "tilesets" / "0x72_DungeonTilesetII_v1.7"

# Pygame init
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wandermaze - Multiple Tilesets")
clock = pygame.time.Clock()

# Load LDtk project
with open(LDTK_PATH, "r", encoding="utf-8") as f:
    ldtk_data = json.load(f)

level_data = next(level for level in ldtk_data["levels"] if level["identifier"] == "Level_0")
layer_instances = level_data["layerInstances"]

# Load all tilesets used in LDtk file
def load_tileset_image(path):
    image = pygame.image.load(path).convert_alpha()
    tiles = []
    image_width, image_height = image.get_size()

    for y in range(0, image_height, TILE_SIZE):
        for x in range(0, image_width, TILE_SIZE):
            tile = image.subsurface((x, y, TILE_SIZE, TILE_SIZE))
            scaled_tile = pygame.transform.scale(tile, (TILE_SIZE * SCALE, TILE_SIZE * SCALE))
            tiles.append(scaled_tile)

    return tiles

# Map tilesetRelPath to list of tiles
tileset_images = {}
tileset_uid_map = {}

for def_set in ldtk_data["defs"]["tilesets"]:
    rel_path = def_set.get("relPath")
    uid = def_set["uid"]
    if not rel_path:
        continue
    full_path = (TILESET_BASE_PATH / Path(rel_path).name).resolve()
    if not full_path.exists():
        print(f"Tileset not found: {full_path}")
        continue
    tileset_images[uid] = load_tileset_image(full_path)
    tileset_uid_map[uid] = Path(rel_path).name  # optional debug

print("Tilesets loaded:")
for k in tileset_images:
    print("-", k)

# Dummy color entity markers
ENTITY_COLORS = {
    "Player_Spawn": (0, 0, 255),
    "Checkpoint": (0, 255, 0),
    "Trap": (255, 0, 0)
}

# Draw tile layer with matching tileset
def draw_layer_tiles(layer):
    tileset_uid = layer.get("__tilesetDefUid")
    if tileset_uid is None or tileset_uid not in tileset_images:
        print(f"[SKIP] No tileset for layer {layer['__identifier']}")
        return
    tileset = tileset_images[tileset_uid]

    for tile in layer["gridTiles"]:
        tile_id = tile["t"]
        px = tile["px"]  # posisi pixel (belum diskalakan)
        pos = (px[0] * SCALE, px[1] * SCALE)

        if 0 <= tile_id < len(tileset):
            screen.blit(tileset[tile_id], pos)
        else:
            print(f"[WARN] Tile ID {tile_id} out of range for tileset UID {tileset_uid}")

# Draw entities as colored boxes
def draw_entities(screen, layer):
    for entity in layer.get("entityInstances", []):
        x = entity["px"][0] * SCALE
        y = entity["px"][1] * SCALE
        identifier = entity["__identifier"]

        color = ENTITY_COLORS.get(identifier, (255, 255, 255))  # default: white
        pygame.draw.rect(screen, color, (x, y, SCALED_TILE_SIZE, SCALED_TILE_SIZE))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for layer in reversed(layer_instances):
        if layer["__type"] == "Tiles":
            draw_layer_tiles(layer)
        elif layer["__type"] == "Entities":
            draw_entities(screen, layer)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

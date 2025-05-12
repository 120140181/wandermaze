import pygame
import os

class Level:
    def __init__(self, player):
        self.player = player
        self.tile_size = player.tile_size
        self.tileset = self.load_tileset()
        self.map_data = self.load_map()

    def load_tileset(self):
        path = "assets/images/tilesets/FG_Cellar_C.png"
        tileset_image = pygame.image.load(path).convert_alpha()
        tiles = []

        tiles_wide = tileset_image.get_width() // self.tile_size
        tiles_high = tileset_image.get_height() // self.tile_size

        for y in range(tiles_high):
            for x in range(tiles_wide):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                tile = tileset_image.subsurface(rect)
                tiles.append(tile)

        return tiles

    def load_map(self):
        # 0 = lantai, 1 = dinding, 2 = jebakan
        return [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 2, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def draw(self, surface):
        for y, row in enumerate(self.map_data):
            for x, tile_id in enumerate(row):
                if tile_id == 1:
                    tile = self.tileset[1]  # Misal dinding
                elif tile_id == 2:
                    tile = self.tileset[2]  # Misal jebakan
                else:
                    tile = self.tileset[0]  # Lantai
                surface.blit(tile, (x * self.tile_size, y * self.tile_size))

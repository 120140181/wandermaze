import pygame

def load_image(path, colorkey=None):
    """
    Fungsi untuk memuat gambar dari path dengan dukungan transparansi.
    """
    try:
        image = pygame.image.load(path).convert_alpha()
        if colorkey is not None:
            image.set_colorkey(colorkey)
        return image
    except pygame.error as e:
        print(f"Gagal memuat gambar: {path} | {e}")
        return None

def split_spritesheet(sheet, width, height):
    """
    Memotong spritesheet menjadi list frame berdasarkan ukuran tile.
    """
    frames = []
    sheet_width, sheet_height = sheet.get_size()
    for y in range(0, sheet_height, height):
        for x in range(0, sheet_width, width):
            rect = pygame.Rect(x, y, width, height)
            frames.append(sheet.subsurface(rect))
    return frames

def draw_text(surface, text, pos, font, color=(255, 255, 255)):
    """
    Menampilkan teks di layar dengan font dan posisi tertentu.
    """
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

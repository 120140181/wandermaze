import pygame

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, image, effect_type="reset"):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.effect_type = effect_type  # "reset", "teleport", "illusion"

    def trigger(self, player, level):
        """
        Efek yang terjadi ketika pemain menyentuh jebakan.
        """
        if self.effect_type == "reset":
            print("‼️ Trap: Reset level!")
            level.reset_level()
        elif self.effect_type == "teleport":
            print("🌀 Trap: Teleport player!")
            player.teleport_to_start()
        elif self.effect_type == "illusion":
            print("🧠 Trap: Reverse controls!")
            player.reverse_controls(temporary=True)

class FakeCheckpoint(pygame.sprite.Sprite):
    def __init__(self, x, y, image, real=False):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_real = real

    def activate(self, player):
        if self.is_real:
            print("✅ Checkpoint activated!")
            player.set_checkpoint(self.rect.topleft)
        else:
            print("❌ Fake checkpoint! Resetting...")
            player.teleport_to_start()

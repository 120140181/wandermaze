class Trap:
    def __init__(self, position):
        self.position = position
        self.is_active = True

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def trigger(self, player):
        if self.is_active:
            # Implement the effect on the player when the trap is triggered
            player.take_damage()
            return True
        return False

    def draw(self, screen):
        if self.is_active:
            # Load and draw the trap image at its position
            trap_image = pygame.image.load('assets/images/trap.png')
            screen.blit(trap_image, self.position)
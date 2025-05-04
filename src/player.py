class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = self.load_image()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def load_image(self):
        # Load the player image from assets
        return pygame.image.load('assets/images/player.png').convert_alpha()

    def move(self, direction):
        if direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed
        elif direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed
        
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)
import pygame
import sys
from player import Player
from level import Level
from utils import load_image, load_sound

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wandermaze")

# Load assets
assets = load_image(), load_sound()

# Create game objects
player = Player(100, 100, assets['player_image'])
level = Level(assets['tileset_image'], assets['trap_image'])

# Main game loop
def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update game state
        player.update()
        level.update()

        # Render
        screen.fill((0, 0, 0))  # Clear the screen
        level.draw(screen)
        player.draw(screen)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
def load_assets():
    """Load all necessary assets for the game."""
    assets = {}
    try:
        assets['player_image'] = load_image('assets/player.png')
        assets['background_music'] = load_sound('assets/background_music.mp3')
    except Exception as e:
        print(f"Error loading assets: {e}")
    return assets

def load_image(file_path):
    """Load an image from the specified file path."""
    try:
        image = pygame.image.load(file_path)
        return image
    except pygame.error as e:
        print(f"Unable to load image at {file_path}: {e}")
        return None

def load_sound(file_path):
    """Load a sound from the specified file path."""
    try:
        sound = pygame.mixer.Sound(file_path)
        return sound
    except pygame.error as e:
        print(f"Unable to load sound at {file_path}: {e}")
        return None

def check_collision(rect1, rect2):
    """Check for collision between two rectangles."""
    return rect1.colliderect(rect2)

def reset_game_state():
    """Reset the game state to its initial conditions."""
    # Placeholder for resetting game variables
    pass

def display_message(screen, message, position, font, color=(255, 255, 255)):
    """Display a message on the screen."""
    text_surface = font.render(message, True, color)
    screen.blit(text_surface, position)
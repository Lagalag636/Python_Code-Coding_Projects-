import pygame
import sys

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Example')

text_color = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (200, 200, 255)
GREEN = (100, 255, 100)
BLACK = (0, 0, 0)
LIGHT_GRAY = (211, 211, 211)
MID_GRAY = (130, 130, 130)

rect_x = 10
rect_y = 15
rect_length = 30
rect_width = 33
rect_speed = 50

tile_size = 50  # Size of each tile
rows = screen_height // tile_size
cols = screen_width // tile_size

default_font = pygame.font.Font(None, 36)  # General font for other text
npc_font = pygame.font.Font(None, 18)    # Custom font for multiline text


#write a class for the npc squares
class NPC(pygame.sprite.Sprite):
    def __init__(self, color, x, y, length, width, description="", x_offset=0, y_offset=0, proximity_radius=50, interaction_zone=None):
        super().__init__()
        self.image = pygame.Surface((length, width))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.centery = self.rect.centery
        self.top = self.rect.top
        self.description = description
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.is_interacting = False  # Track interaction state
        self.proximity_radius = proximity_radius
        # Define the interaction zone if provided, else use the NPC's own rect
        if interaction_zone:
            self.interaction_zone = pygame.Rect(interaction_zone)
        else:
            self.interaction_zone = self.rect  # Default interaction zone is the NPC's rect


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def show_text(self, screen, font, color=WHITE, x_offset=0, y_offset=0, line_spacing=5, bg_opacity=128):
        """
        Displays single-line or multi-line text at a position relative to the NPC.
    
        Parameters:
        - screen: Pygame surface to render the text on
        - font: Pygame font to use for the text
        - color: Color of the text (default is black)
        - x_offset: Horizontal offset from NPC position
        - y_offset: Vertical offset from NPC position
        - line_spacing: Space between lines for multi-line text
        - bg_opacity: Opacity level for the background box (0-255)
        """
        # Position to start rendering the text, relative to the NPC's rect
        x, y = self.rect.x + x_offset, self.rect.y + y_offset
    
        # Split the text into lines in case it has line breaks
        lines = self.description.splitlines()
        text_width = max(font.size(line)[0] for line in lines)  # Find the width of the longest line
        text_height = len(lines) * (font.get_height() + line_spacing) - line_spacing  # Total text height

            # Create the background box with transparency
        bg_surface = pygame.Surface((text_width + 10, text_height + 10))  # Padding for aesthetics
        bg_surface.set_alpha(bg_opacity)  # Set transparency level
        bg_surface.fill((0, 0, 0))  # Fill with black color

        # Draw the background box on the screen first
        screen.blit(bg_surface, (x - 5, y - 5))  # Offset slightly for padding

    
        # Render each line individually
        for i, line in enumerate(lines):
            # Render the line and create a surface for it
            line_surface = font.render(line, True, color)
            # Position each line surface on the screen with the calculated vertical offset
            screen.blit(line_surface, (x, y + i * (font.get_height() + line_spacing)))
        
    def interact(self, character_rect, screen, font, x_offset=0, y_offset=0, character_position=None):
        """
        Checks if the character is near enough to interact and, if so, displays the NPC's text.
    
        Parameters:
        - character_rect: Pygame rect of the character to check collision with the NPC
        - screen: Pygame surface to render the interaction text on
        - font: Pygame font to use for the interaction text
        """

        # Check if the character's rectangle collides with the NPC's rectangle
        if self.interaction_zone.colliderect(character_rect):
            # Detect spacebar press for interaction
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.is_interacting:
                self.is_interacting = True
            if self.is_interacting:
                self.show_text(screen, font, x_offset=self.x_offset, y_offset=self.y_offset)
            # Hide text if the character has moved away
            if character_position and character_position != (character_rect.x, character_rect.y):
                self.is_interacting = False  # Reset interaction state



    

west_npc = NPC(WHITE, 10, 315, rect_length, rect_width, "I represent the West path!\nHead down this path to face\nchallenges and to test your\ntalents. You must choose a path.", x_offset=5, y_offset=-95, interaction_zone=(50, 300, 50, 50))
east_npc = NPC(WHITE, 760, 265, rect_length, rect_width, "I represent the East path!\nHead this way to find your\nwild side and get dangerous.\nYou must choose a path.", x_offset=-145, y_offset=52, interaction_zone=(700, 250, 50, 50))
north_npc = NPC(WHITE, 360, 15, rect_length, rect_width, "I represent the North path!\nChoose my path complete harrowing\nice puzzles for a reward.\nYou must choose a path.", x_offset=-241, y_offset=0, interaction_zone=(350, 50, 50, 50))
south_npc = NPC(WHITE, 410, 565, rect_length, rect_width, "I represent the South path!\nFollow my path and find\nmirrors and mystery.\nYou must choose a path.", x_offset=55, y_offset=-45, interaction_zone=(400, 500, 50, 50))
npcs_group = pygame.sprite.Group()
#npcs_group.add(NPC())

while True:
    screen.fill((255, 255, 255))

    for row in range(rows):
        for col in range(cols):
            color = MID_GRAY if (row + col) % 2 == 0 else LIGHT_GRAY
            pygame.draw.rect(screen, color, (col * tile_size, row * tile_size, tile_size, tile_size))

        # Track character movement by comparing positions
    character = pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_length, rect_width))
    current_character_position = character.topleft
    '''if current_character_position != character_position:
        character_position = current_character_position'''

    for npc in [north_npc, south_npc, east_npc, west_npc]:  # Iterate over each NPC instance
        npc.draw(screen)
        npc.interact(character, screen, npc_font, character_position=current_character_position)  # Now calling interact on each NPC instance

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = event.pos
                print(f"Left mouse button clicked at ({mouse_x}, {mouse_y})")

        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            elif keys[pygame.K_SPACE]:
                print("Space key pressed")
            elif keys[pygame.K_DOWN]:
                rect_y += rect_speed
            elif keys[pygame.K_UP]:
                rect_y -= rect_speed
            elif keys[pygame.K_LEFT]:
                rect_x -= rect_speed
            elif keys[pygame.K_RIGHT]:
                rect_x += rect_speed
     
    text_surface = default_font.render('Press SPACE or click!', True, text_color)
    screen.blit(text_surface, (260, 280))
    # Update previous position
    previous_character_position = current_character_position

    pygame.display.flip()

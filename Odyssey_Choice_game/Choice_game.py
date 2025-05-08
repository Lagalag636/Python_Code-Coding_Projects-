import pygame
import sys
import csv

pygame.init()
screen_width, screen_height = 1200, 800
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

rect_x = 560
rect_y = 365
rect_length = 30
rect_width = 33
rect_speed = 50

tile_size = 50  # Size of each tile
rows = screen_height // tile_size
cols = screen_width // tile_size

default_font = pygame.font.Font(None, 36)  # General font for other text
npc_font = pygame.font.Font(None, 32)    # Custom font for multiline text


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
        
    def interact(self, main_character, screen, font, x_offset=0, y_offset=0, character_position=None):
        """
        Checks if the character is near enough to interact and, if so, displays the NPC's text.
    
        Parameters:
        - character_rect: Pygame rect of the character to check collision with the NPC
        - screen: Pygame surface to render the interaction text on
        - font: Pygame font to use for the interaction text
        """

        # Check if the character's rectangle collides with the NPC's rectangle
        if self.interaction_zone.colliderect(main_character):
            # Detect spacebar press for interaction
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.is_interacting:
                self.is_interacting = True
            if self.is_interacting:
                self.show_text(screen, font, x_offset=self.x_offset, y_offset=self.y_offset)
            # Hide text if the character has moved away
            if character_position and character_position != (main_character.x, main_character.y):
                self.is_interacting = False  # Reset interaction state


class Room:
    def __init__(self, screen, colors, npcs, character, text, font):
        self.screen = screen
        self.tile_size = 50 
        self.rows = screen_height // tile_size
        self.cols = screen_width // tile_size
        self.light_color, self.dark_color = colors
        self.npcs = npcs
        self.character = character
        self.text = text
        self.font = font

    def draw_tiles(self):
        """Draws the tiled background."""
        for row in range(self.rows):
            for col in range(self.cols):
                color = self.dark_color if (row + col) % 2 == 0 else self.light_color
                pygame.draw.rect(
                    self.screen, color,
                    (col * self.tile_size, row * self.tile_size, 
                     self.tile_size, self.tile_size)
                )

    def draw_character(self):
        """Draws the character."""
        pygame.draw.rect(self.screen, (255, 0, 0), self.character)

    def draw_npcs(self):
        """Draws NPCs and triggers interactions."""
        for npc in self.npcs:
            npc.draw(self.screen)  # Draw NPC's image

    def draw_text(self):
        """Displays the prompt text."""
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text_surface, (460, 330))

    def draw(self):
        """Calls all drawing functions."""
        self.screen.fill((255, 255, 255))
        self.draw_tiles()
        self.draw_character()
        self.draw_npcs()
        self.draw_text()

west_npc = NPC(
    WHITE,
    10,
    415,
    rect_length,
    rect_width,
    "I represent the West path!\n"
    "Head down this path to face\n"
    "challenges and to test your\n"
    "talents. You must choose a path.",
    x_offset=5,
    y_offset=-95,
    interaction_zone=(50, 400, 50, 50)
)

east_npc = NPC(
    WHITE,
    1160,
    365,
    rect_length,
    rect_width,
    "I represent the East path!\n"
    "Head this way to find your\n"
    "wild side and get dangerous.\n"
    "You must choose a path.",
    x_offset=-145,
    y_offset=52,
    interaction_zone=(1100, 350, 50, 50)
)

north_npc = NPC(
    WHITE,
    560,
    15,
    rect_length,
    rect_width,
    "I represent the North path!\n"
    "Choose my path to complete harrowing\n"
    "ice puzzles for a reward.\n"
    "You must choose a path.",
    x_offset=-241,
    y_offset=0,
    interaction_zone=(550, 50, 50, 50)
)

south_npc = NPC(
    WHITE,
    610,
    765,
    rect_length,
    rect_width,
    "I represent the South path!\n"
    "Follow my path and find\n"
    "mirrors and mystery.\n"
    "You must choose a path.",
    x_offset=55,
    y_offset=-45,
    interaction_zone=(600, 700, 50, 50)
)


def save_room_to_csv(room, room_id="start_room", filename="rooms.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow([
            "room_id", "screen_width", "screen_height",
            "light_color", "dark_color",
            "character_x", "character_y",
            "npcs", "text"
        ])

        # Write the room data
        writer.writerow([
            room_id,  # Now a string like "start_room"
            room.screen.get_width("Why am I here?"),
            room.screen.get_height("Why am I here?"),
            str(room.light_color),
            str(room.dark_color),
            room.character.x,
            room.character.y,
            "|".join([npc.name for npc in room.npcs]),  # Convert NPCs list to string
            room.text
        ])

def load_room_from_csv(screen, npcs_dict, font, filename="rooms.csv", room_id="start_room"):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["room_id"] == room_id:  # Match the requested room ID
                screen_width = int(row["screen_width"])
                screen_height = int(row["screen_height"])
                light_color = eval(row["light_color"])  # Convert string to tuple
                dark_color = eval(row["dark_color"])  # Convert string to tuple
                character = pygame.Rect(int(row["character_x"]), int(row["character_y"]), 40, 40)

                # Convert NPC names from string back into NPC objects
                npc_names = row["npcs"].split("|")
                npcs = [npcs_dict[name] for name in npc_names if name in npcs_dict]

                text = row["text"]

                # Return a new Room instance
                return Room(screen, (light_color, dark_color), npcs, character, text, font)

    return None  # Return None if no matching room_id is found

npcs_group = pygame.sprite.Group()
#npcs_group.add(NPC())
#TODO: create a class for rooms instead of screens
print("Desktop sizes:", pygame.display.get_desktop_sizes())

# Main game loop
while True:
    main_character = pygame.Rect(rect_x, rect_y, rect_length, rect_width)

    room = Room(
        screen,
        (LIGHT_GRAY, MID_GRAY), 
        [north_npc, south_npc, east_npc, west_npc], 
        main_character, 
        "Press SPACE or click!", 
        default_font
    )
    room.draw()

    # Check for collisions with NPCs
    for npc in [north_npc, south_npc, east_npc, west_npc]:
        npc.interact(main_character, screen, npc_font, character_position=main_character.topleft)
        if npc.rect.colliderect(main_character):
            rect_x -= rect_speed if keys[pygame.K_RIGHT] else 0
            rect_x += rect_speed if keys[pygame.K_LEFT] else 0
            rect_y -= rect_speed if keys[pygame.K_DOWN] else 0
            rect_y += rect_speed if keys[pygame.K_UP] else 0

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
            #elif keys[pygame.K_SPACE] and main_character in interaction_zone:
            #    npc.show_text(screen, font, x_offset=5, y_offset=-95)
            elif keys[pygame.K_SPACE]:
                print("Space key pressed")
            elif keys[pygame.K_DOWN]:
                rect_y += rect_speed
                if rect_y + rect_length > screen_height:
                    rect_y -= rect_speed
            elif keys[pygame.K_UP]:
                rect_y -= rect_speed
                if rect_y < 0:
                    rect_y += rect_speed
            elif keys[pygame.K_LEFT]:
                rect_x -= rect_speed
                if rect_x < 0:
                    rect_x += rect_speed
            elif keys[pygame.K_RIGHT]:
                rect_x += rect_speed
                if rect_x + rect_length > screen_width:
                    rect_x -= rect_speed

    pygame.display.flip()

import pygame
import os
import random
from collections import Counter, defaultdict

# --- Constants ---
CARD_WIDTH = 60
CARD_HEIGHT = 100
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
TABLE_MARGIN = 50

BG_GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 220, 0)
RED = (220, 60, 60)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# --- Card Properties ---
SUITS = ['H', 'D', 'S', 'C']  # Hearts, Diamonds, Spades, Clubs
RANKS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
RANK_VALUE = {r: int(r) for r in RANKS}
RANK_VALUE['1'] = 14  # Ace
RANK_VALUE['2'] = 15  # Two (highest)

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARD_FOLDER = os.path.join(BASE_DIR, 'Cards')
BACK_IMAGE_PATH = os.path.join(CARD_FOLDER, "Back2.png")  # New back texture

# --- Pygame Init ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Presidents (Prototype)")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 24)
BIG = pygame.font.SysFont(None, 36)

# --- Load the full deck ---
def load_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            card_id = f"{suit}{rank}"
            file_path = os.path.join(CARD_FOLDER, f"{card_id}.png")
            try:
                card_image = pygame.image.load(file_path).convert_alpha()
                card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
                deck.append((card_id, card_image))
            except Exception as e:
                print(f"Failed to load {file_path}: {e}")
    return deck

# --- Load card back texture for AI ---
def load_card_back():
    try:
        back = pygame.image.load(BACK_IMAGE_PATH).convert_alpha()
        back = pygame.transform.scale(back, (CARD_WIDTH, CARD_HEIGHT))
        return back
    except Exception as e:
        print(f"Failed to load {BACK_IMAGE_PATH}: {e}")
        return None

# --- Deal cards to players ---
def deal(deck, num_players=4):
    random.shuffle(deck)
    hands = [[] for _ in range(num_players)]
    i = 0
    while deck:
        hands[i % num_players].append(deck.pop())
        i += 1
    return hands

# --- Helpers ---
def card_rank(card_id): return card_id[1:]
def card_value(card_id): return RANK_VALUE[card_rank(card_id)]
def same_rank(cards): return len(set(card_rank(cid) for cid, _ in cards)) == 1
def group_by_rank(hand):
    buckets = defaultdict(list)
    for cid, img in hand:
        buckets[card_rank(cid)].append((cid, img))
    return buckets
def find_starting_player(hands):
    for idx, hand in enumerate(hands):
        if any(cid == 'C3' for cid, _ in hand):
            return idx
    return min(range(len(hands)), key=lambda i: min(card_value(cid) for cid, _ in hands[i]))

# --- Layout ---
SPACING = CARD_WIDTH - 15

def get_hand_positions(hand, position):
    positions = []
    n = len(hand)
    if position in (0, 3):
        total_width = n * SPACING
        start_x = (SCREEN_WIDTH - total_width) // 2
        y = 50 if position == 0 else SCREEN_HEIGHT - CARD_HEIGHT - 50
        for i, (cid, img) in enumerate(hand):
            x = start_x + i * SPACING
            rot = pygame.transform.rotate(img, 180) if position == 0 else img
            positions.append((pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT), rot, (cid, img)))
    elif position == 1:
        total_height = n * SPACING
        x = TABLE_MARGIN
        start_y = (SCREEN_HEIGHT - total_height) // 2
        for i, (cid, img) in enumerate(hand):
            rot = pygame.transform.rotate(img, -90)
            positions.append((rot.get_rect(topleft=(x, start_y + i * SPACING)), rot, (cid, img)))
    elif position == 2:
        total_height = n * SPACING
        x = SCREEN_WIDTH - CARD_HEIGHT - TABLE_MARGIN
        start_y = (SCREEN_HEIGHT - total_height) // 2
        for i, (cid, img) in enumerate(hand):
            rot = pygame.transform.rotate(img, 90)
            positions.append((rot.get_rect(topleft=(x, start_y + i * SPACING)), rot, (cid, img)))
    return positions

def draw_hand(hand, position, selected_ids=None, hide=False, back=None):
    selected_ids = selected_ids or set()
    positions = get_hand_positions(hand, position)
    clickable = []

    for rect, img_or_rot, (cid, orig_img) in positions:
        to_draw = img_or_rot

        # If hiding AI hands (0–2) → use back texture
        if hide and position != 3:
            if back:  
                # Rotate back image depending on AI hand position
                if position == 0:
                    to_draw = pygame.transform.rotate(back, 180)
                elif position == 1:
                    to_draw = pygame.transform.rotate(back, -90)
                elif position == 2:
                    to_draw = pygame.transform.rotate(back, 90)
                screen.blit(to_draw, rect.topleft)
            else:
                # fallback if back not loaded
                pygame.draw.rect(screen, GRAY, rect, border_radius=8)
                pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
        else:
            # Human hand → show real cards
            screen.blit(to_draw, rect.topleft)

        # Selection highlight for human hand only
        if position == 3 and cid in selected_ids:
            pygame.draw.rect(screen, YELLOW, rect.inflate(6, 6), 4, border_radius=10)

        # Make human hand cards clickable
        if position == 3:
            clickable.append((rect, cid))

    return clickable

def draw_pile(last_play):
    """
    Draw the last play (list of (cid, img)) in the center of the table.
    """
    cx = SCREEN_WIDTH // 2
    cy = SCREEN_HEIGHT // 2
    if not last_play:
        # draw empty pile outline
        w = CARD_WIDTH + 30
        h = CARD_HEIGHT + 30
        rect = pygame.Rect(cx - w//2, cy - h//2, w, h)
        pygame.draw.rect(screen, (50, 90, 50), rect, border_radius=12)
        pygame.draw.rect(screen, (30, 40, 30), rect, 2, border_radius=12)
        txt = FONT.render("Discard Pile", True, WHITE)
        screen.blit(txt, (rect.centerx - txt.get_width()//2, rect.centery - txt.get_height()//2))
        return

    # fan them slightly
    n = len(last_play)
    start_x = cx - (n * (SPACING//2)) // 2
    y = cy - CARD_HEIGHT // 2
    for i, (cid, img) in enumerate(last_play):
        x = start_x + i * (SPACING//2)
        screen.blit(img, (x, y))
        pygame.draw.rect(screen, BLACK, (x, y, CARD_WIDTH, CARD_HEIGHT), 2, border_radius=8)

def can_play_set(selected_cards, current_count, current_min_value, must_start_with_c3=False):
    """
    Validate a candidate play.
    - selected_cards: list of (cid, img)
    - current_count: cards required to match (None means free to choose)
    - current_min_value: value to beat (None when starting)
    - must_start_with_c3: only for the first move of the game
    """
    if not selected_cards:
        return False, "Select cards to play."
    if not same_rank(selected_cards):
        return False, "All selected cards must be the same rank."
    count = len(selected_cards)
    rank = card_rank(selected_cards[0][0])
    val = RANK_VALUE[rank]

    if must_start_with_c3:
        need = set(cid for cid, _ in selected_cards)
        if 'C3' not in need or count != 1:
            return False, "Game must start with C3 as a single."
        return True, ""

    if current_count is not None and count != current_count:
        return False, f"You must play {current_count} card(s)."
    if current_min_value is None:
        return True, ""  # starting a new trick: any set is OK

    # must beat strictly higher
    if val <= current_min_value:
        return False, "Your set must be higher rank than the pile."
    return True, ""

def best_ai_play(hand, current_count, current_min_value):
    """
    Very simple AI: play the lowest legal set; else pass.
    Allows singles, pairs, triples, fours.
    Clears on rank '2' automatically by rules outside (not here).
    """
    by_rank = group_by_rank(hand)
    # candidate sets: length must match current_count (if given), else 1..4
    lengths = [current_count] if current_count else [1, 2, 3, 4]
    for L in lengths:
        # collect ranks that have at least L
        candidates = []
        for r, cards in by_rank.items():
            if len(cards) >= L:
                val = RANK_VALUE[r]
                candidates.append((val, r, cards[:L]))
        # sort by value ascending and pick first that beats current_min_value (if any)
        candidates.sort(key=lambda t: t[0])
        for val, r, cards in candidates:
            if current_min_value is None or val > current_min_value:
                return cards  # list of L cards
    return []  # pass

def remove_cards_from_hand(hand, cards_to_remove):
    remove_ids = {cid for cid, _ in cards_to_remove}
    return [(cid, img) for (cid, img) in hand if cid not in remove_ids]

# --- Main Game Loop ---
def main():
    running = True
    deck = load_deck()
    hands = deal(deck, num_players=4)
    back_texture = load_card_back()  # <-- Load Back2.png once here

    # --- Game state ---
    current_turn = find_starting_player(hands)
    trick_required_count = None
    trick_min_value = None
    last_play = []
    consecutive_passes = 0
    first_move = True
    selected_ids = set()
    message = "Game start: player with C3 leads."
    winner = None
    ai_move_cooldown = 0

    while running:
        dt = clock.tick(60)
        screen.fill(BG_GREEN)

        # --- INPUT ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle clicks for human (position 3)
            if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                mx, my = pygame.mouse.get_pos()
                if current_turn == 3:
                    # Build clickable rects
                    clickable = draw_hand(hands[3], 3, selected_ids, hide=False)
                    for rect, cid in clickable:
                        if rect.collidepoint(mx, my):
                            # toggle selection
                            if cid in selected_ids:
                                selected_ids.remove(cid)
                            else:
                                selected_ids.add(cid)

            # Keyboard controls for human
            if event.type == pygame.KEYDOWN and winner is None and current_turn == 3:
                if event.key == pygame.K_p:
                    # pass
                    consecutive_passes += 1
                    message = "You passed."
                    current_turn = (current_turn + 1) % 4
                    ai_move_cooldown = 400
                if event.key == pygame.K_SPACE:
                    # attempt to play selection
                    selected_cards = [(cid, img) for (cid, img) in hands[3] if cid in selected_ids]
                    must_c3 = first_move and current_turn == 3
                    ok, reason = can_play_set(selected_cards, trick_required_count, trick_min_value, must_start_with_c3=must_c3)
                    if ok:
                        # apply play
                        rank_val = card_value(selected_cards[0][0])
                        last_play = [(cid, img) for (cid, img) in selected_cards]
                        hands[3] = remove_cards_from_hand(hands[3], selected_cards)
                        selected_ids.clear()
                        message = f"You played {len(selected_cards)} x rank {card_rank(selected_cards[0][0])}."
                        first_move = False

                        # Update trick rules
                        if trick_required_count is None:
                            trick_required_count = len(selected_cards)
                        trick_min_value = rank_val
                        consecutive_passes = 0

                        # Clear on 2s or 4-of-a-kind (bomb)
                        if rank_val == RANK_VALUE['2'] or len(selected_cards) == 4:
                            message = "Pile cleared!"
                            last_play = []
                            trick_required_count = None
                            trick_min_value = None
                            consecutive_passes = 0
                            # same player continues after clear
                        else:
                            current_turn = (current_turn + 1) % 4
                            ai_move_cooldown = 400
                    else:
                        message = reason

        # --- AI TURNS ---
        if winner is None and current_turn != 3 and ai_move_cooldown <= 0:
            # Decide AI action
            if first_move and current_turn != 3:
                # If AI must start with C3 as a single
                ai_has_c3 = any(cid == 'C3' for cid, _ in hands[current_turn])
                if ai_has_c3:
                    # play single C3
                    play = [next((cid, img) for (cid, img) in hands[current_turn] if cid == 'C3')]
                else:
                    play = []
            else:
                play = best_ai_play(hands[current_turn], trick_required_count, trick_min_value)

            if play:
                rank_val = card_value(play[0][0])
                last_play = play[:]
                hands[current_turn] = remove_cards_from_hand(hands[current_turn], play)
                message = f"Player {current_turn} played {len(play)} x rank {card_rank(play[0][0])}."
                first_move = False
                consecutive_passes = 0
                # Update trick requirements
                if trick_required_count is None:
                    trick_required_count = len(play)
                trick_min_value = rank_val

                # Clear on 2s or 4-of-a-kind
                if rank_val == RANK_VALUE['2'] or len(play) == 4:
                    message = f"Player {current_turn} cleared the pile!"
                    last_play = []
                    trick_required_count = None
                    trick_min_value = None
                    consecutive_passes = 0
                    # same AI continues
                else:
                    current_turn = (current_turn + 1) % 4
                    ai_move_cooldown = 400
            else:
                consecutive_passes += 1
                message = f"Player {current_turn} passed."
                # If everyone else passed, clear pile and next player starts
                if consecutive_passes >= 3 and last_play:
                    message = f"Trick ended. Player {(current_turn - 1) % 4} leads."
                    last_play = []
                    trick_required_count = None
                    trick_min_value = None
                    consecutive_passes = 0
                current_turn = (current_turn + 1) % 4
                ai_move_cooldown = 400

        ai_move_cooldown = max(0, ai_move_cooldown - dt)

        # --- Win check ---
        if winner is None:
            for i in range(4):
                if len(hands[i]) == 0:
                    winner = i
                    message = f"Player {i} went out! (Prototype ends here.)"
                    break

        # --- DRAW ---
        # Table labels
        turn_text = f"Turn: Player {current_turn}" if winner is None else f"Winner: Player {winner}"
        screen.blit(BIG.render(turn_text, True, WHITE), (20, 10))
        screen.blit(FONT.render("Space = Play | P = Pass | Click to select cards (your hand)", True, WHITE), (20, 50))
        screen.blit(FONT.render(message, True, YELLOW if "!" in message else WHITE), (20, 75))

        # Draw hands (hide AI cards)
        draw_hand(hands[0], 0, hide=True, back=back_texture)
        draw_hand(hands[1], 1, hide=True, back=back_texture)
        draw_hand(hands[2], 2, hide=True, back=back_texture)
        clickable_for_human = draw_hand(hands[3], 3, selected_ids=selected_ids, hide=False)

        draw_pile(last_play)

        # Show counts under names
        labels = [
            ("P0 (Top)", (SCREEN_WIDTH//2 - 60, 20)),
            ("P1 (Left)", (20, SCREEN_HEIGHT//2 - 20)),
            ("P2 (Right)", (SCREEN_WIDTH - 140, SCREEN_HEIGHT//2 - 20)),
            ("You (Bottom)", (SCREEN_WIDTH//2 - 70, SCREEN_HEIGHT - 150)),
        ]
        for text, pos in labels:
            screen.blit(FONT.render(text, True, WHITE), pos)

        # Highlight current player area
        if winner is None:
            if current_turn == 0:
                pygame.draw.rect(screen, YELLOW, pygame.Rect(0, 0, SCREEN_WIDTH, 120), 3, border_radius=6)
            elif current_turn == 1:
                pygame.draw.rect(screen, YELLOW, pygame.Rect(0, 120, 180, SCREEN_HEIGHT-240), 3, border_radius=6)
            elif current_turn == 2:
                pygame.draw.rect(screen, YELLOW, pygame.Rect(SCREEN_WIDTH-180, 120, 180, SCREEN_HEIGHT-240), 3, border_radius=6)
            elif current_turn == 3:
                pygame.draw.rect(screen, YELLOW, pygame.Rect(0, SCREEN_HEIGHT-150, SCREEN_WIDTH, 150), 3, border_radius=6)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

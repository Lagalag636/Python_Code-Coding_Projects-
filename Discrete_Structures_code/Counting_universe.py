import random
import math

# ================================================
# CONFIG DATA
# ================================================

# --- Player heroic attribute titles (20 total) ---
HEROIC_TITLES = [
    "Wyrm Slayer", "Animal Whisperer", "Flea Fighter", "Dinosaur Wrangler",
    "Troll Puncher", "Storm Tamer", "Goblin Diplomat", "Phoenix Hugger",
    "Thunder Diver", "Sand Serpent Rider", "Colossus Wrestler", "Nightshade Tracker",
    "Crystal Singer", "Moonlight Skater", "Iron Oak Climber", "Boulder Breaker",
    "Frost Whisperer", "Specter Negotiator", "Starborn Jumper", "Void Runner"
]

# --- Stats used for numerical stat block ---
STAT_NAMES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

# --- Shop items ---
SHOP_ITEMS = [
    "Rune Key", "Flag Kit", "Herbalist Gloves", "Stabilizer Rod", "Torch",
    "Healing Potion", "Compass", "Map Fragment", "Dagger", "Magic Tallow"
]

ITEM_COST = 2
STARTING_GOLD = 10

# ================================================
# MATH UTILITIES
# ================================================

def nCr(n, r):
    return math.comb(n, r)

def nPr(n, r):
    return math.perm(n, r)

def stars_and_bars(balls, bins):
    return math.comb(balls + bins - 1, bins - 1)

def probability_at_least_once(p, trials):
    return 1 - (1 - p) ** trials

# ================================================
# CHARACTER CREATION
# ================================================

def choose_attributes():
    print("\n--- Choose Your Heroic Titles ---")
    for i, title in enumerate(HEROIC_TITLES, start=1):
        print(f"{i:2}. {title}")
    print("\nChoose 3 heroic attributes by number (comma-separated).")

    chosen = []
    while True:
        raw = input("Your choices: ").strip()
        try:
            indices = [int(x) for x in raw.split(",")]
            if len(indices) != 3:
                print("Choose exactly 3.")
                continue
            if any(i < 1 or i > len(HEROIC_TITLES) for i in indices):
                print("Invalid number, try again.")
                continue
            chosen = [HEROIC_TITLES[i-1] for i in indices]
            break
        except:
            print("Invalid input, try again.")
    return chosen

def roll_3d6():
    return sum(random.randint(1,6) for _ in range(3))

def create_stats():
    """
    Two options:
      1) Roll 3d6 for each stat.
      2) Point buy: each stat starts at base 10, and the player has exactly 10 extra points
         to distribute among the six stats (each allocation >= 0). The sum of allocated
         extras must equal 10.
    """
    print("\n--- Stat Generation ---")
    print("1) Roll 3d6 for each stat")
    print("2) Point buy (each stat starts at base 10; you have exactly 10 extra points to distribute)")
    choice = input("Choose [1/2]: ").strip() or "1"

    stats = {}

    if choice == "1":
        for stat in STAT_NAMES:
            val = roll_3d6()
            stats[stat] = val
            print(f"{stat}: {val}")
        return stats

    # Point-buy path: base 10 + distribute exactly 10 extra points
    TOTAL_EXTRA = 10
    remaining = TOTAL_EXTRA
    allocations = {stat: 0 for stat in STAT_NAMES}
    print(f"\nEach stat starts at base 10. You have {TOTAL_EXTRA} extra points to distribute across {len(STAT_NAMES)} stats.")
    print("You may assign 0 or more extra points to each stat. The total assigned must be exactly 10.")

    for i, stat in enumerate(STAT_NAMES):
        # For the last stat, auto-assign the remaining points
        if i == len(STAT_NAMES) - 1:
            allocations[stat] = remaining
            print(f"{stat}: +{allocations[stat]} (auto-assigned remaining)")
            remaining = 0
            break

        # For others, prompt with remaining shown
        while True:
            try:
                prompt = f"Extra points to add to {stat} (0 to {remaining}): "
                val_str = input(prompt).strip()
                val = int(val_str) if val_str != "" else 0
                if val < 0:
                    print("Enter a non-negative integer.")
                    continue
                if val > remaining:
                    print(f"You cannot assign more than the remaining {remaining} points.")
                    continue
                allocations[stat] = val
                remaining -= val
                print(f"Assigned +{val} to {stat}. Remaining extras: {remaining}")
                break
            except ValueError:
                print("Enter a valid integer.")

    # Build final stats = base 10 + allocations
    for stat in STAT_NAMES:
        stats[stat] = 10 + allocations[stat]

    print("\nFinal stats (base 10 + extras):")
    for stat in STAT_NAMES:
        print(f" {stat}: {stats[stat]}")

    return stats

# ================================================
# SHOP
# ================================================

def shop_interaction(inventory, gold):
    print("\n--- The Shop ---")
    print(f"You have {gold} gold. Items cost {ITEM_COST} each.")

    for i, item in enumerate(SHOP_ITEMS, start=1):
        print(f"{i:2}. {item}")

    raw = input("Buy items by number (comma-separated) or Enter to skip: ").strip()
    if not raw:
        return inventory, gold

    try:
        nums = [int(x) for x in raw.split(",")]
    except:
        print("Invalid input. No purchases.")
        return inventory, gold

    for n in nums:
        if 1 <= n <= len(SHOP_ITEMS):
            if gold >= ITEM_COST:
                item = SHOP_ITEMS[n-1]
                inventory.append(item)
                gold -= ITEM_COST
                print(f"Bought {item}. Gold left: {gold}")
            else:
                print("Not enough gold.")
                break
        else:
            print(f"No item {n}.")

    return inventory, gold

# ================================================
# EVENTS: each has a puzzle + bypass item
# ================================================

# Each event returns (True/False) for success/fail

def puzzle_stars_and_bars():
    print("\nEVENT: Rune Vault")
    print("Puzzle: How many ways to distribute 5 indistinguishable orbs into 3 slots?")
    ans = input("Answer: ")
    try:
        return int(ans) == stars_and_bars(5,3)
    except:
        return False

def puzzle_permutation():
    print("\nEVENT: Flag Ridge")
    print("Puzzle: How many ordered arrangements of 3 flags chosen from 5?")
    ans = input("Answer: ")
    try:
        return int(ans) == nPr(5,3)
    except:
        return False

def puzzle_combination():
    print("\nEVENT: Alchemist's Door")
    print("Puzzle: How many ways to choose 3 herbs from 10 (unordered)?")
    ans = input("Answer: ")
    try:
        return int(ans) == nCr(10,3)
    except:
        return False

def puzzle_probability():
    print("\nEVENT: Chance Crossing")
    print("Puzzle: A trap triggers with p=0.25 each attempt.")
    print("What's the probability it triggers at least once in 3 attempts? (round to 4 decimals)")
    ans = input("Answer: ")
    try:
        return abs(float(ans) - probability_at_least_once(0.25,3)) < 1e-4
    except:
        return False

def puzzle_dark_corridor():
    print("\nEVENT: Shadow Corridor")
    print("Puzzle: A torch flickers with probability 0.4 per 10 seconds.")
    print("In 2 intervals, what's the probability it flickers at least once? (round to 4 decimals)")
    ans = input("Answer: ")
    correct = probability_at_least_once(0.4, 2)
    try:
        return abs(float(ans) - correct) < 1e-4
    except:
        return False

# Each event: puzzle, bypass item name
EVENTS = [
    ("Rune Vault",        puzzle_stars_and_bars,  "Rune Key",         0.15),
    ("Flag Ridge",        puzzle_permutation,     "Flag Kit",         0.25),
    ("Alchemist's Door",  puzzle_combination,     "Herbalist Gloves", 0.25),
    ("Chance Crossing",   puzzle_probability,     "Stabilizer Rod",   0.20),
    ("Shadow Corridor",   puzzle_dark_corridor,   "Torch",            0.15),
]

# ================================================
# GAME LOOP
# ================================================

def play_game():
    print("=== Welcome to the Mathematical Universe ===")

    name = input("Character name: ") or "Traveler"
    attributes = choose_attributes()
    stats = create_stats()

    player = {
        "name": name,
        "attributes": attributes,
        "stats": stats,
        "inventory": [],
        "gold": STARTING_GOLD
    }

    print(f"\n{name}'s heroic titles: {attributes}")
    print("Stats:", stats)

    # Shop phase
    player["inventory"], player["gold"] = shop_interaction(player["inventory"], player["gold"])
    print("Final Inventory:", player["inventory"])

    print("\n--- Adventure Begins ---")
    passes = 0
    moves = 0
    MAX_MOVES = 10

    while moves < MAX_MOVES and passes < 3:
        cmd = input("\nPress Enter to move forward (or type 'status'): ").strip().lower()

        if cmd == "status":
            print("\n=== STATUS ===")
            print("Name:", player["name"])
            print("Attributes:", player["attributes"])
            print("Stats:", player["stats"])
            print("Inventory:", player["inventory"])
            print("Passes:", passes)
            print("Moves:", moves, "/", MAX_MOVES)
            continue

        moves += 1
        print(f"\n-- Move {moves}/{MAX_MOVES} --")

        # Choose event
        names = [e[0] for e in EVENTS]
        weights = [e[3] for e in EVENTS]
        idx = random.choices(range(len(EVENTS)), weights=weights, k=1)[0]

        event_name, puzzle_func, bypass_item, _ = EVENTS[idx]
        print(f"\nYou encounter: **{event_name}**")
        print(f"Bypass item for this event: {bypass_item}")

        # If player wants to bypass and has the item
        if bypass_item in player["inventory"]:
            bypass_choice = input(f"Use {bypass_item} to bypass? (y/n): ").strip().lower()
            if bypass_choice == "y":
                player["inventory"].remove(bypass_item)
                print(f"{bypass_item} breaks during use, but you bypass the challenge!")
                passes += 1
                # 5% item find chance
                if random.random() < 0.05:
                    found = random.choice(SHOP_ITEMS)
                    player["inventory"].append(found)
                    print(f"You find a {found} on the ground.")
                continue

        # Solve puzzle
        success = puzzle_func()

        if success:
            print("Success!")
            passes += 1
            if random.random() < 0.05:   # success find chance
                found = random.choice(SHOP_ITEMS)
                player["inventory"].append(found)
                print(f"You find a {found} nearby!")
        else:
            print("You failed the challenge.")
            if random.random() < 0.25:   # fail find chance
                found = random.choice(SHOP_ITEMS)
                player["inventory"].append(found)
                print(f"You stumble onto a {found} while recovering!")

    # End of game
    print("\n=== Adventure End ===")
    print(f"Events passed: {passes}")

    if passes >= 3:
        print("YOU WIN!")
    else:
        print("You did not pass enough events...")

    print("Final Inventory:", player["inventory"])


if __name__ == "__main__":
    random.seed()
    play_game()

import random

def find_high_score (values):
    high_score = 0

    for goal in range(1, 7):
        high_score = max(high_score, check_singles(values, goal))
    high_score = max(high_score, check_three_of_kind(values), check_four_of_kind(values), check_five_of_kind(values), check_full_house(values), check_straight(values))

    return high_score

# Add all occurences of goal value
def check_singles(dice, goal):
    score = 0

    # Type your code here.
    for die in dice:
        if die == goal:
            score += goal
    return score

# Check for three of a kind (score = 30)
def check_three_of_kind(dice):
    score = 0

    # Type your code here.
    for die in dice:
        if dice.count(die) >= 3:
            score = 30
    return score

# Check for four of a kind (score = 40)
def check_four_of_kind(dice):
    score = 0

    # Type your code here.
    for die in dice:
        if dice.count(die) >= 4:
            score = 40
    return score

# Check for five of a kind (score = 50)
def check_five_of_kind(dice):
    score = 0

    # Type your code here.
    for die in dice:
        if dice.count(die) >= 5:
            score = 50
    return score

# Check for full house (score = 35)
def check_full_house(dice):
    score = 0

    # Type your code here.
    for die in dice:
        if dice.count(die) == 3:
            for die2 in dice:
                if dice.count(die2) == 2:
                    score = 35
    return score

# Check for straight (score = 45)
def check_straight(dice):
    score = 0
    
    # Type your code here.
    if dice == [1, 2, 3, 4, 5] or dice == [2, 3, 4, 5, 6]:
        score = 45
    return score

def evaluate_score_and_inform_user(high_score):
    # Type your code here.
    if high_score > 0 and high_score < 30:
        print(f"You scored { high_score } points! Nice singles!")
    elif high_score == 30:
        print(f"You scored { high_score } points! The three of a kind!")
    elif high_score == 40:
        print(f"You scored { high_score } points! A four of a kind!")
    elif high_score == 50:
        print(f"You scored { high_score } points! A five of a kind!")
    elif high_score == 35:
        print(f"You scored { high_score } points! A full house!")
    elif high_score == 45:
        print(f"You scored { high_score } points! A straight!")
    else:
        print(f'This was your high score: { high_score }')

if __name__ == '__main__':  # Do not modify
    print("This is a dice game! Let's see what you rolled!")
    
    dice = [random.randint(1, 6) for _ in range(5)]
    print(f"You rolled: { dice }")
    high_score = 0

    # Place dice in ascending order
    dice.sort()

    # Find high score and output
    high_score = find_high_score(dice)

    evaluate_score_and_inform_user(high_score)
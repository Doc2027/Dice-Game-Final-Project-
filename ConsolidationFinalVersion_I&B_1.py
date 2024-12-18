from random import randint
import time # Importing a time module as a countdown timer

NUM_DICE = 3
DICE_SIDES = 6
MAX_SCORE = 50

def roll_dice():
    """three dice and return the results as a list"""
    return [randint(1, DICE_SIDES) for _ in range(NUM_DICE)]

def check_tuple_out(dice):
    """Check if all three dice have the same value"""
    return len(set(dice)) == 1

def fix_dice(dice):
    """Identify fixed and unfixed dice based on matching values"""
    fixed = [d for d in dice if dice.count(d) > 1]
    unfixed = [d for d in dice if dice.count(d) == 1]
    return fixed, unfixed

def player_turn(player_name):
    """Simulate a single player's turn"""
    print(f"\n{player_name}'s turn!")
    dice = roll_dice()
    print(f"Initial roll (as tuple): {tuple(dice)}")

    if check_tuple_out(dice):
        print("Tupled out! No points this turn.")
        return 0

    fixed, unfixed = fix_dice(dice)
    re_roll = True
    while re_roll:
        print(f"Fixed dice: {fixed}, Unfixed dice: {unfixed}")

        # Add countdown timer for player decision
        print("You have 10 seconds to decide whether to re-roll unfixed dice!")
        start_time = time.time()
        choice = ""

        while time.time() - start_time < 10:  # 10-second countdown
            choice = input("Re-roll unfixed dice? (yes/no): ").lower()
            if choice in ["yes", "no"]:
                break
            print("Invalid input! Please enter 'yes' or 'no'. Hurry up!")

        if not choice:  # Default if time runs out
            print("Time's up! No re-roll this time.")
            choice = "no"

        if choice != "yes":
            re_roll = False
        else:
            unfixed = [randint(1, DICE_SIDES) for _ in range(len(unfixed))]
            dice = fixed + unfixed
            print(f"New roll: {tuple(dice)}")
            if check_tuple_out(dice):
                print("Tupled out! No points this turn.")
                return 0
            fixed, unfixed = fix_dice(dice)

    score = sum(dice)
    print(f"{player_name} scores {score} points! Rolls {tuple(dice)}")
    return score

def print_scores(scores):
    """Print the current scores of all the players"""
    print("\nCurrent Scores:")
    for player, score in scores.items():
        print(f"{player}: {score} points")

"""Main game loop for managing player turns and determining the winner"""
players = []
num_players = 2
for i in range(num_players):
    while True:
        name = input(f"Enter name for Player {i + 1}: ").strip()
        if name:
            players.append(name)
            break
        print("Name cannot be empty. Please enter a valid name.")

scores = {player: 0 for player in players}
max_score = MAX_SCORE

while all(score < max_score for score in scores.values()):
    for player in players:
        print(f"\n{player}'s turn!")
        scores[player] += player_turn(player)
        print_scores(scores)

        if scores[player] >= max_score:
            print(f"{player} wins with {scores[player]} points!")
            break


"""Test functions for every feature"""

def test_roll_dice():
    """Test roll_dice function for correct output length and range."""
    result = roll_dice()
    assert len(result) == NUM_DICE, f"Expected {NUM_DICE} dice, but got {len(result)}."
    assert all(1 <= val <= DICE_SIDES for val in result), "One or more dice rolled out of range."
    print("test_roll_dice passed!")

def test_check_tuple_out():
    """Test check_tuple_out function for correct detection of all same values."""
    assert check_tuple_out([3, 3, 3]) == True, "Failed: Dice with the same values should return True."
    assert check_tuple_out([3, 2, 3]) == False, "Failed: Dice with different values should return False."
    print("test_check_tuple_out passed!")

def test_fix_dice():
    """Test fix_dice function to separate fixed and unfixed dice."""
    fixed, unfixed = fix_dice([3, 3, 4])
    assert fixed == [3, 3], f"Expected fixed dice [3, 3], but got {fixed}."
    assert unfixed == [4], f"Expected unfixed dice [4], but got {unfixed}."

    fixed, unfixed = fix_dice([1, 2, 3])
    assert fixed == [], "Expected no fixed dice when all are different."
    assert unfixed == [1, 2, 3], "Expected all dice as unfixed when no values match."
    print("test_fix_dice passed!")

if __name__ == "__main__":
    # Run all tests
    test_roll_dice()
    test_check_tuple_out()
    test_fix_dice()
    print("All tests passed successfully!")


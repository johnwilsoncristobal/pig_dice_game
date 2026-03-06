# PIG

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    num_players = input ("Enter the number of players (2-4): ")
    if num_players.isdigit():
        num_players = int(num_players)
        if 2 <= num_players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print ("Invalid, try again.")

max_score = 50
player_scores = [0 for x in range(num_players)]

print(player_scores)

while max(player_scores) < max_score:
    for player_index in range(num_players):
        print ("\nPlayer number", player_index + 1, "turn has just started!")
        print ("Your total score is:", player_scores[player_index], "\n")
        turn_score = 0


        while True:
            should_roll = input ("Would you like to roll again? (y)?: ")
            if should_roll.lower() != "y":
                break

            dice_value = roll()
            if dice_value == 1:
                print("You rolled a 1! Turn Done!")
                turn_score = 0
                break
            else:
                turn_score += dice_value
                print ("You rolled a:", dice_value)

            print ("Your score is:", turn_score)

        player_scores[player_index] += turn_score
        print ("Your total score is:", player_scores[player_index])


max_score_value = max(player_scores)
winning_index = player_scores.index(max_score_value)
print ("Player number", winning_index + 1, "is the winner with a score of:", max_score_value)
import time
import random

snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_die():
    return random.randint(1, 6)

def move_player(position, roll):
    new_position = position + roll
    if new_position > 100:
        return position  
    else:
        return new_position

def check_snakes_and_ladders(position):
    if position in snakes:
        new_position = snakes[position]
        print(f"Oops! Bitten by a snake from {position} to {new_position}")
        return new_position
    elif position in ladders:
        new_position = ladders[position]
        print(f"Yay! Climbed a ladder from {position} to {new_position}")
        return new_position
    else:
        return position

def play_game():
    num_players = int(input("Enter the number of players: "))
    player_positions = [0] * num_players
    player_turn = 0

    while True:
        input(f"Player {player_turn + 1}'s turn. Press Enter to roll the die...")
        roll = roll_die()
        print(f"Player {player_turn + 1} rolled a {roll}")
        
        initial_position = player_positions[player_turn]
        new_position = move_player(initial_position, roll)
        new_position = check_snakes_and_ladders(new_position)
        
        player_positions[player_turn] = new_position
        print(f"Player {player_turn + 1} moved from {initial_position} to {new_position}")

        if player_positions[player_turn] >= 100:
            print(f"Player {player_turn + 1} wins!")
            break
        
        player_turn = (player_turn + 1) % num_players

if(1):
    start_time = time.time()
    play_game()
    end_time = time.time()
    execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
    
    

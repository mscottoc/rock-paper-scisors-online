import random
random.seed()

import socket

print("RULES: rock beats scissors, scissors beats paper, paper beats rock.")
print("The rules are best out of three.")
print("If you tie after three rounds, the game will keep going until one of you win.")
usr_name = input("What is your username?\n> ")
p_one_score = 0
p_two_score = 0
turn = 0

while( turn < 3 or p_one_score == p_two_score):
    cpu_turn = random.randint(1,3)
    if cpu_turn == 1:
        cpu_turn = "rock"
    elif cpu_turn == 2:
        cpu_turn = "paper"
    elif cpu_turn == 3:
        cpu_turn = "scissors"
    else:
        print("woopsie!", cpu_turn)
        break

    input_valid = False
    while input_valid == False:
        local_turn = input("\nrock, paper, or scissors?\n> ")
        if local_turn != "rock" and  local_turn != "paper" and local_turn != "scissors":
            print("Input not valid! make sure to write the whole word lowercase.")
        else:
            input_valid = True
    
    print("They chose: " + cpu_turn)
    if local_turn == "rock":
        if cpu_turn == "paper":
            turn_win = False
            p_two_score += 1
        elif cpu_turn == "rock":
            turn_win = False
        elif cpu_turn == "scissors":
            turn_win = True
            p_one_score += 1
    elif local_turn == "paper":
        if cpu_turn == "scissors":
            turn_win = False
            p_two_score += 1
        elif cpu_turn == "paper":
            turn_win = False
        elif cpu_turn == "rock":
            turn_win = True
            p_one_score += 1
    elif local_turn ==  "scissors":
        if cpu_turn == "rock":
            turn_win = False
            p_two_score += 1
        elif cpu_turn == "scissors":
            turn_win = False
        elif cpu_turn == "paper":
            turn_win = True
            p_one_score += 1
    if turn_win:
        print("You win round", turn + 1)
    else:
        print("You lost round", turn + 1)
    turn += 1

    print("player one:", p_one_score)
    print("player two:", p_two_score)
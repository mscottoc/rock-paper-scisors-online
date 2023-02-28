import socket

HOST = '192.168.50.245' #NEEDS TO BE CHANGED FOR EACH HOST
PORT = 4207

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

print("RULES: rock beats scissors, scissors beats paper, paper beats rock.")
print("The rules are best out of three.")
print("If you tie after three rounds, the game will keep going until one of you win.")
usr_name = input("What is your username?\n> ")

continue_game = True
while continue_game:
    input_valid = False
    while input_valid == False:
        local_turn = input("\nrock, paper, or scissors?\n> ")
        if local_turn != "rock" and  local_turn != "paper" and local_turn != "scissors":
            print("Input not valid! make sure to write the whole word lowercase.")
        else:
            input_valid = True
    socket.send(local_turn.encode('utf-8'))
    print("They chose:", socket.recv(1024).decode('utf-8'))
    
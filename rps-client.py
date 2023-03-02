import socket

HOST = '192.168.50.245' #NEEDS TO BE CHANGED FOR EACH HOST
PORT = 4207

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

print("RULES: rock beats scissors, scissors beats paper, paper beats rock.")
print("The rules are best out of three.")
print("If you tie after three rounds, the game will keep going until one of you win.")
usr_name = input("What is your username?\n> ")
socket.send(usr_name.encode('utf-8'))

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
    local_score = int(socket.recv(1024).decode('utf-8'))
    remote_score = int(socket.recv(1024).decode('utf-8'))
    turn = int(socket.recv(1024).decode('utf-8'))
    print(f"Your Score: {local_score}\nTheir Score: {remote_score}\nTurn: {turn}")

    if turn >= 3 and local_score != remote_score:
        continue_game = False
print("Game Over")
if local_score > remote_score:
    print("you win!")
else:
    print("you lose :(")
print(f"You have {socket.recv(1024).decode('utf-8')} win(s) and {socket.recv(1024).decode('utf-8')} loss(es).")
    
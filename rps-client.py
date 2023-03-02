import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((input("input the host address\n> "), 4207))

print("RULES: rock beats scissors, scissors beats paper, paper beats rock.")
print("The rules are best out of three.")
print("If you tie after three rounds, the game will keep going until one of you win.")
usr_name = input("What is your username?\n> ")
server_socket.send(usr_name.encode('utf-8'))

continue_game = True
while continue_game:
    input_valid = False
    while input_valid == False:
        local_turn = input("\nrock, paper, or scissors?\n> ")
        if local_turn != "rock" and  local_turn != "paper" and local_turn != "scissors":
            print("Input not valid! make sure to write the whole word lowercase.")
        else:
            input_valid = True
    server_socket.send(local_turn.encode('utf-8'))
    print("They chose:", server_socket.recv(1024).decode('utf-8'))
    local_score = int(server_socket.recv(1024).decode('utf-8'))
    server_socket.send("local score received".encode('utf-8'))
    remote_score = int(server_socket.recv(1024).decode('utf-8'))
    server_socket.send("remote score received".encode('utf-8'))
    turn = int(server_socket.recv(1024).decode('utf-8'))
    server_socket.send("turn received".encode('utf-8'))
    print(f"Your Score: {local_score}\nTheir Score: {remote_score}\nTurn: {turn}")

    if turn >= 3 and local_score != remote_score:
        continue_game = False
print("Game Over")
if local_score > remote_score:
    print("you win!")
else:
    print("you lose :(")
print(f"You have {server_socket.recv(1024).decode('utf-8')} win(s) and {server_socket.recv(1024).decode('utf-8')} loss(es).")
    
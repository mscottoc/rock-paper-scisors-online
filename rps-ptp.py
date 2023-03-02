import socket
end_program = False

print("RULES: rock beats scissors, scissors beats paper, paper beats rock.")
print("The rules are best out of three.")
print("If you tie after three rounds, the game will keep going until one of you win.")
usr_name = input("What is your username?\n> ")
while not end_program:
    try:
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if socket.gethostbyname(socket.gethostname()) == '192.168.50.24': #tries different addresses so the same code can run on both machines
            remote_socket.connect(('192.168.50.245', 4207)) 
        else:
            remote_socket.connect(('192.168.50.24', 4207))
    except:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((socket.gethostname(), 4207))

        server.listen(5)
        remote_socket, address = server.accept()
    while not end_program:
        local_score = 0
        remote_score = 0
        turn = 0

        continue_game = True
        try:
            remote_socket.send(usr_name.encode('utf-8'))
            opnt_name = remote_socket.recv(1024).decode('utf-8')
        except:
            print("connection lost!")
            break
        print("\nNew Game")
        print(f"Your opponent is {opnt_name}")
        while continue_game:
            turn += 1
            input_valid = False
            while input_valid == False:
                local_turn = input("\nrock, paper, or scissors?\n> ")
                if local_turn != "rock" and  local_turn != "paper" and local_turn != "scissors":
                    print("Input not valid! make sure to write the whole word lowercase.")
                else:
                    input_valid = True
            remote_socket.send(local_turn.encode('utf-8'))
            remote_turn = remote_socket.recv(1024).decode('utf-8')
            print("They chose:",remote_turn)
            if local_turn == remote_turn:
                remote_score += 1
                local_score += 1
            elif local_turn == "rock":
                if remote_turn == "paper":
                    remote_score += 1
                elif remote_turn == "scissors":
                    local_score += 1
            elif local_turn == "paper":
                if remote_turn == "scissors":
                    remote_score += 1
                elif remote_turn == "rock":
                    local_score += 1
            elif local_turn ==  "scissors":
                if remote_turn == "rock":
                    remote_score += 1
                elif remote_turn == "paper":
                    local_score += 1
            print(f"Your Score: {local_score}\nTheir Score: {remote_score}\nTurn: {turn}")

            if turn >= 3 and local_score != remote_score:
                continue_game = False
        print("Game Over")
        if local_score > remote_score:
            print("you win!")
        else:
            print("you lose :(")
        if input("keep playing? y/n\n> ") == 'n':
            end_program = True
            break
            
import socket

HOST = '192.168.50.245' #NEEDS TO BE CHANGED FOR EACH HOST
PORT = 4207

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
random.seed()

while True:
    p_one_score = 0
    p_two_score = 0
    turn = 0

    client_socket, address = server.accept()
    print(f"Connected to {address}")

    continue_game = True

    while continue_game:
        cpu_turn = random.randint(1,3)
        if cpu_turn == 1:
            cpu_turn = "rock"
        elif cpu_turn == 2:
            cpu_turn = "paper"
        elif cpu_turn == 3:
            cpu_turn = "scissors"
        else:
            print("woopsie!", cpu_turn)
            assert(False)
        
        player_turn = client_socket.recv(1024).decode('utf-8')
        print(player_turn)
        client_socket.send(cpu_turn.encode('utf-8'))
        if player_turn == "rock":
            if cpu_turn == "paper":
                turn_win = False
                p_two_score += 1
            elif cpu_turn == "rock":
                turn_win = False
            elif cpu_turn == "scissors":
                turn_win = True
                p_one_score += 1
        elif player_turn == "paper":
            if cpu_turn == "scissors":
                turn_win = False
                p_two_score += 1
            elif cpu_turn == "paper":
                turn_win = False
            elif cpu_turn == "rock":
                turn_win = True
                p_one_score += 1
        elif player_turn ==  "scissors":
            if cpu_turn == "rock":
                turn_win = False
                p_two_score += 1
            elif cpu_turn == "scissors":
                turn_win = False
            elif cpu_turn == "paper":
                turn_win = True
                p_one_score += 1
    
import socket
import random

HOST = '10.244.13.236' #NEEDS TO BE CHANGED FOR EACH HOST
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
        turn += 1

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
        if player_turn == cpu_turn:
            p_two_score += 1
            p_one_score += 1
        elif player_turn == "rock":
            if cpu_turn == "paper":
                p_two_score += 1
            elif cpu_turn == "scissors":
                p_one_score += 1
        elif player_turn == "paper":
            if cpu_turn == "scissors":
                p_two_score += 1
            elif cpu_turn == "rock":
                p_one_score += 1
        elif player_turn ==  "scissors":
            if cpu_turn == "rock":
                p_two_score += 1
            elif cpu_turn == "paper":
                p_one_score += 1
        
        print(p_one_score,'|',p_two_score,'|', turn)
        client_socket.send(str(p_one_score).encode('utf-8'))
        print("player score sent")
        client_socket.send(str(p_two_score).encode('utf-8'))
        print("player score sent")
        client_socket.send(str(turn).encode('utf-8'))
        print("turn sent")
        if turn >= 3 and p_one_score != p_two_score:
            continue_game = False
            print("game end")


        
    
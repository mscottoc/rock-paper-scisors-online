import socket
import random
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 4207))

server.listen(5)
random.seed()

while True:
    p_one_score = 0
    p_two_score = 0
    turn = 0

    client_socket, address = server.accept()
    print(f"Connected to {address}")

    continue_game = True
    usr_name = client_socket.recv(1024).decode('utf-8').upper()
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
        print(f"Server chose {cpu_turn}")
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
        print(client_socket.recv(1024).decode('utf-8'))
        client_socket.send(str(p_two_score).encode('utf-8'))
        print("player score sent")
        print(client_socket.recv(1024).decode('utf-8'))
        client_socket.send(str(turn).encode('utf-8'))
        print("turn sent")
        print(client_socket.recv(1024).decode('utf-8'))
        if turn >= 3 and p_one_score != p_two_score:
            continue_game = False
            print("game end")
    
    try:
        f = open("score-sheet.json", 'r')
        score_sheet = json.loads(f.read())
        f.close
    except:
        score_sheet = {}
    if p_one_score > p_two_score:
        if score_sheet.get(usr_name) is None:
            new_score = {
                usr_name : {
                "loss" : 0,
                "win" : 1
                }
            }
            score_sheet.update(new_score)
        else:
            score_sheet[usr_name]["win"] += 1
    elif p_two_score > p_one_score:
        if score_sheet.get(usr_name) is None:
            new_score = {
                usr_name : {
                "loss" : 1,
                "win" : 0
                }
            }
            score_sheet.update(new_score)
        else:
            score_sheet[usr_name]["loss"] += 1
    print(score_sheet)
    f = open("score-sheet.json", 'w')
    f.write(json.dumps(score_sheet))
    f.close()
    client_socket.send(str(score_sheet[usr_name]["win"]).encode('utf-8'))
    client_socket.send(str(score_sheet[usr_name]["loss"]).encode('utf-8'))



        
    
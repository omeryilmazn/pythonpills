print(" ==ROCK,PAPER,SCISSORS BATTLE== ")

print(" ==ROCK,PAPER,SCISSORS BATTLE== ")
player1_score = 0
player2_score = 0
player_1 = input("Player1, Do your move R, P or S: ")
player_2 = input("Player2, Do your move R, P or S: ")

if player_1 == "R":
    if player_2 == "R":
        print("Two Rocks. Tie.")
    elif player_2 == "P":
        print("Player 2's paper wrapped Player 1's rock.")
        player2_score += 1
    elif player_2 == "S":
        print("Player 1's rock smashed Player 2's scissors.")
        player1_score = +1
    else:
        print("Invalid move from Player 2.")
elif player_1 == "S":
    if player_2 == "S":
        print("Two scissors. Tie.")
    elif player_2 == "R":
        print("Player 2's rock smashed Player 1's scissors.")
        player2_score += 1
    elif player_2 == "P":
        print("Player 1's scissors cut the paper of Player 2's.")
        player1_score = +1
    else:
        print("Invalid move from Player 2.")
elif player_1 == "P":
    if player_2 == "P":
        print("Two papers. Tie.")
    elif player_2 == "S":
        print("Player 2's scissors cut the paper of Player 1.")
        player2_score += 1
    elif player_2 == "R":
        print("Player 1's paper wrapped Player 2's rock.")
        player1_score = +1
else:
    print("Invalid move from Player 1.")

print(f"SCORE: Player1: {player1_score}, Player2: {player2_score}")

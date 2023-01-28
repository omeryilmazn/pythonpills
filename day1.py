print(" ==ROCK,PAPER,SCISSORS BATTLE== ")

player_1 = input("Do your move R, P or S: ")
player_2 = input("Do your move R, P or S: ")

if player_1 == "R":
    if player_2 == "R":
        print("Two Rocks. Tie.")
    elif player_2 == "P":
        print("Player 2's paper wrapped Player 1's rock.")
    elif player_2 == "S":
        print("Player 1's rock smashed Player 2's scissors.")
    else:
        print("Invalid move from Player 2.")
elif player_1 == "S":
    if player_2 == "S":
        print("Two scissors. Tie.")
    elif player_2 == "R":
        print("Player 2's rock smashed Player 1's scissors.")
    elif player_2 == "P":
        print("Player 1's scissors cut the paper of Player 2's.")
    else:
        print("Invalid move from Player 2.")
elif player_1 == "P":
    if player_2 == "P":
        print("Two papers. Tie.")
    elif player_2 == "S":
        print("Player 2's scissors cut the paper of Player 1.")
    elif player_2 == "R":
        print("Player 1's paper wrapped Player 2's rock.")
else:
    print("Invalid move from Player 1.")
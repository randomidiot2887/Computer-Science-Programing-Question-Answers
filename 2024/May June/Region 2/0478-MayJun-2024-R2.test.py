import random as r
import testmaterial as t #To see if the data is stored correctly in a stuable format
Grid = [[None] * 6] + [[None] + ["" for _ in range(5)] for _ in range(5)] #make 0 in both axis into placeholders
t.printcontents(Grid)
l = -10
#Hide X in the 5 by 5 grid from axis 1
while True:
    x, y = r.randint(1, 5), r.randint(1, 5) #Random X and Y cordinates
    if not(x == 1 and y == 1):

        Grid[x][y] = "X"
        break

print()
t.printcontents(Grid)

#Player starts at cordinates 1, 1
player_x = 1
player_y = 1
moves = 10 #player starts with 10 moves

while True:

    #Giving player guidence on how to play while asking for movement diarection
    bad_move = False
    while True:
        diarection_to_move = input(f"You can input Left, Right, Up or Down as L,R,U,D Respectively.\n You have {moves} Moves left.\nPlease enter your diarection\n: - ")
        if (diarection_to_move == "L") or (diarection_to_move == "R") or (diarection_to_move == "U") or (diarection_to_move == "D"):
            break
        else: print(">invalid input<\n")
    match diarection_to_move:
        case 'L':
            if ((player_x-1) > 0): player_x -= 1
            else: bad_move = True
        case 'R':
            if ((player_x+1) <= 5): player_x += 1
            else: bad_move = True
        case 'U':
            if ((player_y-1) > 0): player_y -= 1
            else: bad_move = True
        case 'D':
            if ((player_y+1) <= 5): player_y += 1
            else: bad_move = True
    if bad_move != True: moves -= 1
    else: print(">Invalid Move<")
    if Grid[player_x][player_y] == 'X': print("You win"); break
    if moves < 1: print("You loose"); break
    Grid[player_x][player_y] = 'P'
    t.printcontents(Grid)
    Grid[player_x][player_y] = ""
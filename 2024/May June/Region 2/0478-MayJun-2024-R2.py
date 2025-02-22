import random as r #requird for random number generation in python, has been referd as 'r' in the code.
Grid = [[None] * 6] + [[None] + ["" for _ in range(5)] for _ in range(5)] #make 0 in both axis into placeholders
#Player starts at cordinates 1, 1
player_x = 1
player_y = 1
#player starts with 10 moves
moves = 10 
#Hide X in the 5 by 5 grid from axis 1
while True:
    x, y = r.randint(1, 5), r.randint(1, 5) #Random X and Y cordinates whth a number between 1 and 5 inclusive.
    if not(x == 1 and y == 1):#If X is not in 1,1 [to avoid an instant win.]
        Grid[x][y] = "X"#Sets X
        break#Breaks out of loop
print("Welcome to FIND X\nMove around and find X in the 5 by 5 maze.") #User greeted
while True:#Main game loop
    #Giving player guidence on how to play while asking for movement diarection
    bad_move = False #Flag to detect an inavlid move
    while True:
        diarection_to_move = input(f"You can input Left, Right, Up or Down as L,R,U,D Respectively.\n You have {moves} Moves left.\nPlease enter your diarection\n: - ")
        if (diarection_to_move == "L") or (diarection_to_move == "R") or (diarection_to_move == "U") or (diarection_to_move == "D"):#validating input
            break
        else: print(">invalid input<\n")
    match diarection_to_move:
        case 'L':
            if ((player_x-1) > 0): player_x -= 1#Check if input is possible and executes it
            else: bad_move = True#A bad move has occured, flag set to true
        case 'R':
            if ((player_x+1) <= 5): player_x += 1#Check if input is possible and executes it
            else: bad_move = True#A bad move has occured, flag set to true
        case 'U':
            if ((player_y-1) > 0): player_y -= 1#Check if input is possible and executes it
            else: bad_move = True#A bad move has occured, flag set to true
        case 'D':
            if ((player_y+1) <= 5): player_y += 1#Check if input is possible and executes it
            else: bad_move = True#A bad move has occured, flag set to true
    if bad_move != True: moves -= 1#If bad flag is true and if not, decrementing moves by 1
    else: print(">Invalid Move<") #If move invalid, printing that
    if Grid[player_x][player_y] == 'X': print("You win"); break #Exiting if user won, with message
    if moves < 1: print("You loose"); break #Exiting when moves ran out and user lost with message
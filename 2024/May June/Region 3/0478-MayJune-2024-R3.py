Teams = ["" for _ in range(10)]
Results = [["" for _ in range(4)] for _ in range(10)]
Played = 0

ERRORMSG = "I"

#Inputting and validating thee number of games played by all teams with at most 16 games being played (No more then 16)
while True:
    Played = int(input(f"{ERRORMSG}nput the number of games played by each team\nMAX 16\n:- "))
    if Played <= 18 and Played > 0:
        break
    elif Played > 18:
        ERRORMSG = f"{Played} is more then 18 games. Again i"
    else:#MAking it deny negative or zero integers. they are invalid.
        ERRORMSG = "The number of games must be a positive integer. A negetive integer or zero is not sutable. Again i"

for team in range(10):#Getting names of teams, storing them in Teams list
    Teams[team] = input(f"Input name of team {team}\n: - ")

for team in range(10):
    while True:
        Results[team][3]
        #Getting number of wins, losses, drawn matches from user, and calculating points for each team
        Results[team][0] = int(input("Enter the number of games won\n: - ")); Results[team][3] += Results[team][0] * 3 
        Results[team][1] = int(input("Enter the number of drawn won\n: - ")); Results[team][3] += Results[team][1]
        Results[team][2] = int(input("Enter the number of lost won\n: - ")) #No points are awarded.
        if Results[team][0] + Results[team][1] + Results[team][2] == Played: break
        else: print("Please Reenter!")
#Sorting arrays Results and Teams in decending order of Results[team][4] (Points)
while True:
    swap = False
    for team in range(10-1):
        if Results[team][3] < Results[team+1]:
           #Now get ready for the mahoosive swap statement taller then Nuha Misses Child
           Results[team], Results[team+1], Teams[team], Teams[team+1], swap = Results[team+1], Results[team], Teams[team+1], Teams[team], True
    if swap != True:
        break
no_winning_teams = 0
most_points = Results[0][3]
for team in range(10):#FInds teams with most points and prints them with their name (winning)
    if Results[team][3] == most_points:
        no_winning_teams += 1
        print(f"Team {Teams[team]} has won with {Results[3]} points")
print(f"{no_winning_teams} teams have most points")



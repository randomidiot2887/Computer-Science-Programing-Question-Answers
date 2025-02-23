
import random as r
for i in range(100):
    Teams = ["" for _ in range(10)]
    Results = [[0 for _ in range(4)] for _ in range(10)]
    Played = 0

    ERRORMSG = "I"

    #Inputting and validating thee number of games played by all teams with at most 16 games being played (No more then 16)
    while True:
        Played = r.randint(-1, 20);(print(f"{ERRORMSG}nput the number of games played by each team\nMAX 16\n:- "))
        if Played <= 18 and Played > 0:
            break
        elif Played > 18:
            ERRORMSG = f"{Played} is more then 18 games. Again i"
        else:#MAking it deny negative or zero integers. they are invalid.
            ERRORMSG = "The number of games must be a positive integer. A negetive integer or zero is not sutable. Again i"

    for team in range(10):#Getting names of teams, storing them in Teams list
        Teams[team] = f"a{r.randint(0, 1000)}";print(f"Input name of team {team}\n: - ")

    for team in range(10):
        print(f"for team {Teams[team]}")
        while True:
            one = r.randint(0, 20)
            three = r.randint(0, 20)
            two = r.randint(0, 20)
            if (one + two + three) >= Played - 1 and (one + two + three) <= Played + 1:break

            Results[team][3]
            #Getting number of wins, losses, drawn matches from user, and calculating points for each team
            Results[team][0] = one;(print("Enter the number of games won\n: - ")); Results[team][3] += Results[team][0] * 3 
            Results[team][1] = two;(print("Enter the number of drawn won\n: - ")); Results[team][3] += Results[team][1]
            Results[team][2] = three;(print("Enter the number of lost won\n: - ")) #No points are awarded.
            if Results[team][0] + Results[team][1] + Results[team][2] == Played: break
            else: print("Please Reenter!")
    #Sorting arrays Results and Teams in decending order of Results[team][3] (Points)
    while True:
        swap = False
        for team in range(10-1):
            if Results[team][3] < Results[team+1][3]:
            #Now get ready for the mahoosive swap statement taller then Nuha Misses Child
                Results[team], Results[team+1], Teams[team], Teams[team+1], swap = Results[team+1], Results[team], Teams[team+1], Teams[team], True
        if swap != True:
            break
    no_winning_teams = 0
    most_points = Results[0][3]
    for team in range(10):#FInds teams with most points and prints them with their name (winning)
        if Results[team][3] == most_points:
            no_winning_teams += 1
            print(f"Team '{Teams[team]}' has won with {Results[team][3]} points")
    print(f"{no_winning_teams} teams have most points")

#the question itself
#----------------------------------------------------------------------------------------------------
# A one-dimensional (1D) array Teams[] contains the names of 10 football teams in a local league.
# A two-dimensional (2D) array Results[] stores, for each team, the total number of:
# • games won
# • games drawn
# • games lost
# • points.
# The position of any team’s data is the same in both arrays. For example the data in index 3 of
# Results[] belongs to the team in index 3 of Teams[]
# The array data will be used to find the current leader of the league.
# The variable Played stores the number of games played by each team. Each team plays the
# same number of games.
# Write a program that meets the following requirements:
# • allows the number of games played to be input and stored, with a maximum of 18 games
# • allows the names of the teams to be input and stored
# • allows the number of games won, drawn and lost to be input and stored for each team
# • validates the number of games played and the number of games won, drawn or lost against
# the number of games played
# • calculates and stores the number of points for each team using three points for a win and one
# point for a draw; there are no points for a loss
# • sorts the array Results[] into descending order of number of points, ensuring the
# corresponding parallel array Teams[] is kept in the same order
# • determines how many teams have the highest number of points
# • outputs the name(s) of the winning team(s) along with the number of points achieved.
# You must use pseudocode or program code and add comments to explain how your code works.
# You do not need to declare any arrays, variables or constants; you may assume that this has
# already been done.
# All inputs and outputs must contain suitable messages.
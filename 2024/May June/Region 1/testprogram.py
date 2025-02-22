import random
##This is a Unittest used to test if the official algorithm will work without user input

Clubs = ["" for _ in range(12)]
Clubs_temp = ["United", "Manchester", "Intestinepool", "UnUnited Arabian Emirates", "UnUnited", "Bancester", "BrainPool", "Kingdom of states", "BaldIves", "Basilonaldo", "FCC Academy", "Post Mortom Analasysic"]
Statistics = [[0 for _ in range(12)] for _ in range(3)]
Points = [0 for _ in range(12)]
Matches = 0


#Input the number of matches played in league
while True:
    no_matches = random.randint(10, 24)
    Matches = no_matches; print("For the teams, input the number of matches played during the league\n(Must NOT be greater then 22 matches)\n: - ")
    if Matches <= 22: break #Validates if Matches is less then or eaqual to 22.
    else: print("Too many matches. Must be an integer thats less then 23")#Error message

#Gets the names of all teams in the league (amount of teams is 12). Stores it in list Clubs
for team in range(12): Clubs[team] = Clubs_temp[team]; print(f"Input the name of team {team+1}\n: - ")
#Getting the number of wins, dawn matches, and losses per team and calculating the score.
for team in range(12):
    while True:
        while True:
            one = random.randint(1, Matches); two = random.randint(1,Matches); three = random.randint(1,Matches)
            if one + two + three == Matches: break
            if one+two+three == Matches - 1: break
        Statistics[0][team] = one; print(f"For team {Clubs[team]};\nInput the number of matches won\n: - "); Points[team] += 12 * Statistics[0][team]
        Statistics[1][team] = two; print("Input the number of matches drawn\n: - "); Points[team] += 5 * Statistics[1][team]
        Statistics[2][team] = three; print("Input the number of matches lost\n: - ")
        if ((Statistics[0][team] + Statistics[1][team] + Statistics[2][team]) != Matches):
            print(f"The number of wins, losses and drawn matches must add up to {Matches}\n>Invalid Value<\n Please Reenter")
        else: break

#Initialising largest and variable with a very small value
most_points = -999999
#Finding club with most points at first.
for club in range(12):
    if Points[club] > most_points: most_points = Points[club]

#Prints teams with most points, their wins and total points.
for team in range(12):
    if Points[team] >= most_points:
        print(f"Club {Clubs[team]} is a winner with;\n{Statistics[0][team]} wins; {Points[club]} points total\n")

print("\n\ntest succesful\nexiting")
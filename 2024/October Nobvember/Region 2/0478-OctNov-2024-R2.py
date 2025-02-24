#Please excuse the lack of commenting, ill do it later
Rooms = ["" for _ in range(20)]
Dimentions = [[0 for _ in range(20)] for _ in range(3)]
Number = 0 #Number of rooms
nu_rooms = [0 for _ in range(30)]
Total_Area = 0
Largest_Room = [-float("INF"), ""]
Smallest_Room = [float("INF"), ""]
while True:
    Number = int(input(f"Input the number of rooms\n:- "))
    if Number > 20:
        print("The amount of rooms enterd must be less than 20\nFor more rooms, use the premium config of the program") #A littlke joke
    elif Number < 3:
        print("Thats too less rooms. we want atleast 3 rooms to calculate for.")
    else: break
    print("Please Re-Enter the number of rooms for which data is to be inputted for")
for room in range(2):
    Rooms[room] = input(f"Input the name of room {room+1}\n:- ") #Room name
    Dimentions[0][room], Dimentions[1][room] = map(int, input("Input the length and width of the room\nseperated by commas\n: - ").split(","))#Room dimentions (length and width)
    print("Inputting data succesfully completed")
    Dimentions[2][room] = round((Dimentions[0][room] * Dimentions[1][room]), 2)
    Total_Area += Dimentions[2][room]
    if Smallest_Room[0] > Dimentions[2][room]: Smallest_Room[0], Smallest_Room[1] = Dimentions[2][room], Rooms[room]
    elif Largest_Room[0] < Dimentions[2][room]: Largest_Room[0], Largest_Room[1] = Dimentions[2][room], Rooms[room]
    print(f"STATS FOR {Rooms[room]} Room\nLength is {Dimentions[0][room]}m\nWidth is {Dimentions[1][room]}m\nArea is {Dimentions[2][room]}m^2")
print(f"Largest room is {Largest_Room[1]}\nSmallest room is {Smallest_Room[1]}\nAverage area of all rooms is {Total_Area/Number}m^2\nTotal area of property is {Total_Area}m^2")

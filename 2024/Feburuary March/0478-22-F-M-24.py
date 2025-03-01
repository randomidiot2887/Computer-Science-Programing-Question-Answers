StudentName = ["Aal", "Aakil", "Naveesh", "Yazdhan"]
ScreenTime = [[0 for _ in range(7)] for _ in range(4)]
ClassSize = 4
TotalScreenPerWeekPerStudent = [0 for _ in range(ClassSize)]
NumberOfDaysWithMoreThenThreeHundredMinutesOfScreenTimePerStudent = [0 for _ in range(ClassSize)]
WeekDays = ['Sunday', 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saterday'] #To display week day
StudentWithLowestScreenTime = [float("INF"), ""] #For storing the number of minutes spent with the name of the student witb least minutes of screentime
TotalScreenTimeForWholeClassInMinutesTobeUsedToFindAverageOfTheWholeClassInMinutes = 0
#Inpuuting time spent infront of screen for week
#Looping for every student
for student in range(ClassSize):
    print(f"Input the number of time infront of scren spent for student {StudentName[student]}")
    for day in range(7): #To loop 7 times for each day in a week.
        ScreenTime[student][day] = int(input(f"For {WeekDays[day]}\n(In minutes): - "))
        print(f"Time inputted for {WeekDays[day]} for student {StudentName[student]}.\nProcessing") #Confromation
        TotalScreenPerWeekPerStudent[student] += ScreenTime[student][day] #Totaling total screentime per student for whole week per student
        if ScreenTime[student][day] > 300: #Checking if student spent more then 300 minutes on screntime
            NumberOfDaysWithMoreThenThreeHundredMinutesOfScreenTimePerStudent[student] += 1 #Incrementing the days with more then 300 min screen
        print("checked for if student has more then 300 minutes of screen")
    if TotalScreenPerWeekPerStudent[student] < StudentWithLowestScreenTime[0]:#Finding student with least screentime
        StudentWithLowestScreenTime[0] = TotalScreenPerWeekPerStudent[student]#Recording the time
        StudentWithLowestScreenTime[1] = StudentName[student]#Recording the name
    print("Checked if the student has lwoest screntime")
    TotalScreenTimeForWholeClassInMinutesTobeUsedToFindAverageOfTheWholeClassInMinutes += TotalScreenPerWeekPerStudent[student] #totals screntime for whole class
    print("Total screntime totaled with this studnets data\n")
for student in range(ClassSize):#prints info per student
    print(f"ScreenTimeData for Student {StudentName[student]}\nStudent has spent {TotalScreenPerWeekPerStudent[student] // 60} hours and {TotalScreenPerWeekPerStudent[student] % 60}minutes on screen total\nStudent has {NumberOfDaysWithMoreThenThreeHundredMinutesOfScreenTimePerStudent[student]} days with more then 300 minutes of screen.")
print(f"Average ScreenTime for whole class is {round(TotalScreenTimeForWholeClassInMinutesTobeUsedToFindAverageOfTheWholeClassInMinutes / ClassSize, 2)} minutes\nStudent {StudentWithLowestScreenTime[1]} has spent the least amount of ScreenTime withn the whole ClassRoom. Congrats!") #Prints the class screentime average and the student with least screentime


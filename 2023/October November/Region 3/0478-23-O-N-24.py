import random
Temperatures = [[round(random.uniform(0, 100), 2) for _ in range(24)] for _ in range(7)]
MaxWeek = float("-INF")
MinWeek = float("INF")
AvWeek = 0
TWeek = 0
WeekDays = ['SunDay', 'MonDay', 'TuesDay', 'WednesDay', 'ThursDay', 'FriDay', 'SaterDay'] #Week days names
for day in range(7):
    MaxDay = float("-INF") # Maxmum temperature per day
    MinDay = float("INF") # Minmum temperature per day
    TDay = 0 #Total temperature for finding average
    AvDay = 0 #Average for day
    for hour in range(24):
        if Temperatures[day][hour] > MaxDay:#Finding highest temperature for day
            MaxDay = Temperatures[day][hour]
        elif Temperatures[day][hour] < MinDay:#Finding lowest temperature for day
            MinDay = Temperatures[day][hour]
        TDay += Temperatures[day][hour] #Finding total day temperature
    AvDay = TDay / 24 #Average temperature
    TWeek += TDay #Total week temperature
    if AvDay > MaxWeek:
        MaxWeek = AvDay
    elif AvDay < MinWeek:
        MinWeek = AvDay
    print(f'Data for {WeekDays[day]}\nMaximum temperature for day is {MaxDay}C\nMinimum temperature for day is {MinDay}C\nAverage temperature for day is {AvDay}C')
AvWeek  = (TWeek / 7) / 24#Finding average week temp
print(f'Maximum temperature for week is {MaxWeek}C\nMinimum temperature for week is {MinWeek}C\nAverage temperature for week is {AvWeek}C')
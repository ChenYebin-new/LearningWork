day = int(input())
count_day = day%5
if count_day <=3 and count_day != 0:
    print(f"Fishing in day {day}")
else:
    print(f"Drying in day {day}")
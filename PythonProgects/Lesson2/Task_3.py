month_number = int(input("Enter month number: "))

season = {1: "Winter", 2: "Winter", 3: "String", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer",
          9: "Fall", 10: "Fall", 11: "Fall", 12: "Winter"}

season_list = ["Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Fall", "Fall", "Fall",
               "Winter"]

while True:
    if month_number <= 0 or month_number > 12:
        month_number = int(input("Enter month number: "))
    else:
        print("Dictionary:")
        print(f"Month {month_number} is {season[month_number]}", end="\n\n")

        print("List:")
        print(f"Month {month_number} is {season_list[month_number - 1]}")
        break

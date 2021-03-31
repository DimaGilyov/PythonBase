a = float(input("Enter result in first day (km): "))
b = float(input("Enter goal (km): "))

day_number = 1
while True:
    print(f"{day_number} day: {a:.2f}")
    if a > b:
        break

    percent_result = (a * 10) / 100
    a += percent_result

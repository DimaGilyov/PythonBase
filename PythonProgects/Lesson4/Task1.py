from sys import argv

working_hours, hourly_rate, working_bonus = [float(el) for el in argv[1:]]
if working_hours >= 0 and hourly_rate >= 0 and working_bonus >= 0:
    payment_sum = (working_hours * hourly_rate) + working_bonus
    print(f"({working_hours} * {hourly_rate}) + {working_bonus} = {payment_sum}")
else:
    print("Arguments must be >= 0")

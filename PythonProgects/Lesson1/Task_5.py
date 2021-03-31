income = float(input("Enter income: "))
costs = float(input("Enter costs: "))

if income > costs:
    print("The company has worked in profit\n")

    profit = income - costs
    profitability = profit / income
    print(f"Profitability:{profitability}")

    employees_count = int(input("Enter employees count: "))
    profit_per_one_employee = profit / employees_count
    print(f"Profit per one employee: {profit_per_one_employee}")
else:
    print("The company hasn't worked in profit")

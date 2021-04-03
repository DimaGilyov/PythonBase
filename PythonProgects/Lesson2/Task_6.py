products_list = []
while True:
    print()
    command = input("Do you want to add product? (Y/N): ")

    if command.upper() == "Y":
        name = input("Enter product name (String): ")
        if name.isdigit():
            print(f"Incorrect product name: {name}")
            continue

        price = float(input("Enter product price (Number): "))
        if price <= 0:
            print(f"Incorrect price: {price}")
            continue

        count = int(input("Enter products count (Number): "))
        if count < 0:
            print(f"Products count can't be < 0: {count}")
            continue

        unit = input("Enter unit of measurement (String): ")
        if unit.isdigit():
            print(f"Incorrect unit of measurement: {unit}")
            continue

        number = len(products_list) + 1
        product = (number, {"Name": name, "price": price, "count": count, "unit": unit})
        products_list.append(product)
        print()

        specifications = {}
        specifications_keys = list(products_list[0][1].keys())
        for key in specifications_keys:
            values_list = []
            for element in products_list:
                values_list.append(element[1].get(key))

            specifications[key] = list(set(values_list))

        print(specifications)
    elif command.upper() == "N":
        print("Close program")
        break
    else:
        print("Unknown command!")
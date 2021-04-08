def print_user_data(first_name, last_name, year_birth, city, email, phone_number):
    print(f"First name: {first_name}, Last name: {last_name}, Year birth: {year_birth}, City: {city}, Email: {email},"
          f" Phone number: {phone_number}")


def is_correct_name(name):
    for element in list(name):
        if str(element).isdigit():
            return False
    return True


def is_correct_year(year):
    if str(year).isdigit():
        return 1930 < int(year) <= 2021
    return False


def is_correct_email(email):
    """
    Примитивная функция для проверки строки на email, в дальнейшем будем это делать через регулярки
    :param email:
    """
    if str(email).isdigit():
        return False
    else:
        email = str(email)
        return email.find("@") > -1 and email.count(".") > 0 and not email.endswith(".") and not email.startswith(".")


def is_correct_phone_number(phone_number):
    phone_number = str(phone_number)
    phone_number = phone_number[1:] if phone_number.startswith("+") else phone_number
    return phone_number.replace("-", "").isdigit() and (phone_number.startswith("8") or phone_number.startswith("7")) \
        and len(phone_number) == 11


while True:
    input_first_name = input("Enter first name: ")
    input_last_name = input("Enter last name: ")
    try:
        input_year_birth = int(input("Enter year birth: "))
    except ValueError:
        continue
    input_city = input("Enter city: ")
    input_email = input("Enter email: ")
    input_phone_number = input("Enter phone number: ")

    if not is_correct_name(input_first_name):
        print(f"Incorrect first name: {input_first_name}")
        continue
    elif not is_correct_name(input_last_name):
        print(f"Incorrect last name: {input_last_name}")
        continue
    elif not is_correct_year(input_year_birth):
        print(f"Incorrect year: {input_year_birth}")
        continue
    elif not is_correct_name(input_city):
        print(f"Incorrect city name: {input_city}")
        continue
    elif not is_correct_email(input_email):
        print(f"Incorrect email: {input_email}")
        continue
    elif not is_correct_phone_number(input_phone_number):
        print(f"Incorrect phone number: {input_phone_number}")
        continue
    else:
        print_user_data(first_name=input_first_name, last_name=input_last_name, city=input_city, email=input_email,
                        year_birth=input_year_birth, phone_number=input_phone_number)
        break

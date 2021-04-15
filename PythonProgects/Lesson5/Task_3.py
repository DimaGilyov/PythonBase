from functools import reduce


def get_salary(text):
    return float((str(text).split()[1]))


def get_employee_name(text):
    return str(text).split()[0]


def print_list(_list):
    for e in _list:
        print(e)
    print()


def get_average_salary(employees):
    salaries_list = [get_salary(employee) for employee in employees]
    # Решил так сказать закрепить лямбды и reduce, но лучше наверное через sum вычислять.
    return reduce(lambda a, b: a + b, salaries_list) / len(salaries_list)


try:
    with open("text_3.txt", "r", encoding="utf-8") as file_3:
        employees_list = file_3.readlines()

        employees_list_with_salary_less_20k = [get_employee_name(employee.strip()) for employee in employees_list
                                               if get_salary(employee) < 20000.0]
        print("Employees list with salary less 20k")
        print_list(employees_list_with_salary_less_20k)

        print("Average salary")
        print(f"{get_average_salary(employees_list)} $")
except IOError as error:
    print(error)

import json


def get_companies_and_profits(text):
    companies_info = [line.split() for line in text]
    companies_and_profits = {}
    for company in companies_info:
        # Финансы лучше перевести во float
        company_name, profit, losses = company[0], float(company[2]), float(company[3])
        companies_and_profits[company_name] = profit - losses

    return companies_and_profits


def get_average_profit(companies_and_profits):
    companies_and_profits = dict(companies_and_profits)
    profits = ([profit for profit in companies_and_profits.values() if profit > 0])
    return {"average_profit": sum(profits) / len(profits)}


def write_file(json_object):
    try:
        with open("text_7_1.json", "w", encoding="utf-8") as file_7_1:
            json.dump(json_object, file_7_1, ensure_ascii=False, indent=4)
    except IOError as error:
        print(error)


def start_program():
    try:
        text = [line.strip() for line in open("text_7.txt", "r", encoding="utf-8")]
        companies_and_profits = get_companies_and_profits(text)
        average_profit = get_average_profit(companies_and_profits)
        write_file([companies_and_profits, average_profit])
    except IOError as error:
        print(error)


start_program()

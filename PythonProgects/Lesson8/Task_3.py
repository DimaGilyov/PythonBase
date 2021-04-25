class NumberException(Exception):
    def __init__(self, text):
        self.text = text


numbers_list = []


def is_digit(input_text):
    input_text = str(input_text)
    if input_text.isdigit():
        return True
    try:
        float(input_text)
        return True
    except ValueError:
        return False


def check_value(input_text):
    if not is_digit(input_text):
        raise NumberException(f"Not a number: {input_text}")


def start():
    while True:
        # Будем просто вносить только по одному числу.
        input_text = input("Enter number (exit: 'stop'): ")
        if input_text.lower().strip() == "stop":
            break
        try:
            check_value(input_text)
            numbers_list.append(float(input_text))
        except NumberException as error:
            print(error)


start()
print(numbers_list)

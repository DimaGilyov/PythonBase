text = input("Enter a few words separated by a space: ")
words_list = text.split(" ")

for n, el in enumerate(words_list):
    el = el if len(el) <= 10 else el[:10:]
    print(f"{n + 1}: {el}")

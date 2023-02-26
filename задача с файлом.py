def enter_lines():
    num_lines = input("Введите количествово строк: ")
    while not num_lines.isdigit():
        num_lines = input("Неккоректный ввод. Введите количествово строк: ")
    return int(num_lines)


def read_last(lines, file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        amount_lines = len(text)
        start = amount_lines - lines
        for i in text[start:]:
            print(i)


article_file = "article.txt"
last_lines = enter_lines()
read_last(last_lines, article_file)

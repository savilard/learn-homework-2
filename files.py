def save_line_to_file(filepath: str, line: str) -> None:
    """Saves line to file."""
    with open(filepath, 'a', encoding='utf-8') as essay_content:
        essay_content.write(line)


def main() -> None:
    """Домашнее задание №2.

    Работа с файлами


    1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
    2. Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
    3. Подсчитайте количество слов в тексте
    4. Замените точки в тексте на восклицательные знаки
    5. Сохраните результат в файл referat2.txt
    """
    length_of_strings = 0
    number_of_words = 0
    with open('referat.txt', 'r', encoding='utf-8') as file_content:
        for line in file_content:
            length_of_strings += len(line)
            number_of_words += len(line.split(' '))
            save_line_to_file('referat2.txt', line.replace('.', '!'))


if __name__ == '__main__':
    main()

def save_file_content_to(filepath: str, file_content: str) -> None:
    """Saves content to file.

    @param filepath:  path to the saved file;
    @param file_content: information to be saved to file.
    """
    with open(filepath, 'w', encoding='utf-8') as file_object:
        file_object.write(file_content)


def main() -> None:
    """Домашнее задание №2.

    Работа с файлами


    1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
    2. Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
    3. Подсчитайте количество слов в тексте
    4. Замените точки в тексте на восклицательные знаки
    5. Сохраните результат в файл referat2.txt
    """
    with open('referat.txt', 'r', encoding='utf-8') as file_object:
        file_content = file_object.read()
        number_of_characters = len(file_content)
        number_of_words = len(file_content.split())
        save_file_content_to('referat2.txt', file_content.replace('.', '!'))

    print(f'Длина текста - {number_of_characters} символов')
    print(f'Количество слов - {number_of_words}')


if __name__ == '__main__':
    main()

import csv
from typing import Dict, List


def save_users_to_csv_file(users: List[Dict[str, str]]) -> None:
    """Saves users data to csv file."""
    with open('export.csv', 'w', encoding='utf-8') as csv_file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(csv_file, fields, delimiter=';')
        writer.writeheader()
        for user in users:
            writer.writerow(user)


def main():
    """Домашнее задание №2.

    Работа csv

    1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
       В списке нужно создать не менее 4-х словарей
    2. Запишите содержимое списка словарей в файл в формате csv

    """
    users = [
        {'name': 'Алекс', 'age': '25', 'job': 'Инструктор по серфингу'},
        {'name': 'Катерина', 'age': '34', 'job': 'Библиотекарь'},
        {'name': 'Иван', 'age': '19', 'job': 'Студент'},
        {'name': 'Пётр', 'age': '29', 'job': 'Фитнес тренер'},
        {'name': 'Елена', 'age': '40', 'job': 'Бухгалтер'},
    ]

    save_users_to_csv_file(users)


if __name__ == '__main__':
    main()

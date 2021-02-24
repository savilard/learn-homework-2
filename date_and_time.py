from datetime import datetime, timedelta
from typing import Optional


def calculate_date_days_ago(number_of_days_ago: int) -> Optional[datetime]:
    """Calculates a date that was a specified number of days ago."""
    if isinstance(number_of_days_ago, int):
        return datetime.today() - timedelta(days=number_of_days_ago)


def convert_datetime_to_str(date: datetime) -> Optional[str]:
    """Converts datetime to string."""
    if isinstance(date, datetime):
        return date.strftime('%d.%m.%Y')


def print_days() -> None:
    """Prints the dates to the console: yesterday, today, 30 days ago."""
    print('Сегодня - {0}'.format(convert_datetime_to_str(datetime.today())))
    print('Вчера - {0}'.format(convert_datetime_to_str(calculate_date_days_ago(number_of_days_ago=1))))
    print('30 дней назад - {0}'.format(convert_datetime_to_str(calculate_date_days_ago(number_of_days_ago=30))))


def convert_string_to_datetime(date_string):
    """Converts string to datetime."""
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')


if __name__ == '__main__':
    print_days()
    print(convert_string_to_datetime('01/01/20 12:10:03.234567'))

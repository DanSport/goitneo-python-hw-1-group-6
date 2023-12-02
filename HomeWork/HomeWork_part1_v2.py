from collections import defaultdict
from datetime import datetime
import createlist


def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        birthday_weekday = birthday_this_year.strftime("%A")

        if 0 <= delta_days <= 7:
            if birthday_this_year.weekday() >= 5:
                birthday_weekday = "Monday"

            birthdays_per_week[birthday_weekday].append(name)

    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


if __name__ == "__main__":
    get_birthdays_per_week(createlist.generate_random_users(40))

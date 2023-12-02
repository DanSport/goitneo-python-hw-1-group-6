from datetime import datetime, timedelta
import random
import string

def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

def generate_random_users(count):
    users = []
    start_date = datetime(2005, 12, 1)
    end_date = datetime(2005, 12, 31)

    for _ in range(count):
        random_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
        random_surname = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
        random_birthday = generate_random_date(start_date, end_date)
        full_name = f"{random_name} {random_surname}"
        user = {"name": full_name, "birthday": random_birthday}
        users.append(user)

    return users



from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    current_day_of_week = datetime.now().weekday()
    days_until_monday = (7 - current_day_of_week) % 7
    start_of_week = datetime.now() - timedelta(days=days_until_monday)
    days_of_week = [start_of_week + timedelta(days=i) for i in range(7)]
    birthdays_per_week = {day.strftime('%A'): [] for day in days_of_week}

    for user in users:
        user_birthday = user['birthday']
        user_name = user['name']

        if start_of_week <= user_birthday < (start_of_week + timedelta(days=7)):
            day_of_birthday = user_birthday.strftime('%A')
            birthdays_per_week[day_of_birthday].append(user_name)

    for day, users in birthdays_per_week.items():
        if users:
            print(f"{day}: {', '.join(users)}")

users = [
    {'name': 'Marek', 'birthday': datetime(2024, 1, 6)},
    {'name': 'Kamil', 'birthday': datetime(2024, 1, 8)},
    {'name': 'Dawid', 'birthday': datetime(2024, 1, 10)},
    {'name': 'Jan', 'birthday': datetime(2024, 1, 10)},
]

get_birthdays_per_week(users)

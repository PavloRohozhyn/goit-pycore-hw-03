""" get datetime and timedelta from datetime """
from datetime import datetime, timedelta

users_list = [
    {"name": "John Doe", "birthday": "1985.04.29"},
    {"name": "Jane Smith", "birthday": "1990.04.27"},
    {"name": "Jane Smith1", "birthday": "1990.04.12"},
    {"name": "Jane Smith2", "birthday": "1990.04.23"},
    {"name": "Jane Smith3", "birthday": "1990.04.15"},
    {"name": "Jane Smith4", "birthday": "1990.04.28"}
]

def get_upcoming_birthdays(users: dict) -> dict:
    """ get birthdays list """
    result = []
    today = datetime.today().date()
    for item in users:
        name = item['name']
        birthday = item['birthday']
        # get datatime object from str
        b_obj = datetime.strptime(birthday, "%Y.%m.%d").date()
        # get day of year (birthday) - 122
        day_of_year = b_obj.timetuple().tm_yday
        # get day of year (today) - 119
        day_of_year_current = today.timetuple().tm_yday
        # its one week
        one_week = day_of_year_current+7

        # get date witch 
        if day_of_year >= day_of_year_current and one_week >= day_of_year:
            modified_birthday = b_obj.replace(year = today.year)
            # check if weekend
            if modified_birthday.weekday() == 5 or modified_birthday.weekday() == 6:
                # modified to next monday
                delta = (6 - modified_birthday.weekday()+1) % 6
                modified_birthday = modified_birthday + timedelta(days=delta)
            result.append({'name': name, 'congratulation_date': modified_birthday})

    return result


upcoming_birthdays = get_upcoming_birthdays(users_list)
print("Список привітань на цьому тижні:", upcoming_birthdays)

# result
# {'name': 'John Doe', 'congratulation_date': datetime.date(2024, 4, 29), 'old': datetime.date(1985, 4, 29)}, 
# {'name': 'Jane Smith', 'congratulation_date': datetime.date(2024, 4, 29), 'old': datetime.date(1990, 4, 27)}, 
# {'name': 'Jane Smith2', 'congratulation_date': datetime.date(2024, 4, 23), 'old': datetime.date(1990, 4, 23)}, 
# {'name': 'Jane Smith4', 'congratulation_date': datetime.date(2024, 4, 29), 'old': datetime.date(1990, 4, 28)}
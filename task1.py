""" import datetime from datetime module """
from datetime import datetime
import sys

def get_days_from_today(date: str)-> int | ValueError:
    """Function return amount of days from the entered date"""

    try:
        # converting entered data(string) to datetime object
        enter_data = datetime.strptime(date, '%Y-%m-%d')
        # calculate the difference of days
        res = datetime.now() - enter_data
        return res.days

    # handling an exception when user have a wrong entered date
    except ValueError:

        print("Opps! date must have next format YYYY-MM-DD, please run again with the correct date")
        # terminate script
        sys.exit()


def day_or_days(target: int) -> str:
    if abs(target) == 1:
        return 'day'
    else:
        return 'days'

# Gets entered date from user
date = input('Please, enter a date, the date should have the next format YYYY-MM-DD (for example 2021-10-09): ')
# Calculate of result
total = get_days_from_today(date)
end = day_or_days(total)
# deriving the result
print(f'Amount of days from {date} to date of today : {total} {end}')

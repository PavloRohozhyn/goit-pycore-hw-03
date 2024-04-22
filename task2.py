""" import random sys module """
import random
import sys

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """ random function"""
    
    # min must be more then 0
    if not 1 <= min <= 1000:
        raise ValueError("min must be more then 0")
    # max must be less then 1000
    if not 1 <= max <= 1000:
        raise ValueError("max must be less then 1000")
    # max must be more then min
    if max < min or max == min:
        raise ValueError("max must be more then min or not equils min")
    # quntity must be more then 0 and more then max or equils max
    if quantity <= 0 and quantity >= max:
        raise ValueError("quntity must be more then 0 and more then max or equils max")
    set_of_random_element = []
    while(True):
        # add element into list
        set_of_random_element.append(random.randint(min,max))
        # remove duplicates 
        result = set(set_of_random_element)
        # check amount of elements
        if(len(result) == quantity):
            # cast to list
            result = list(result)
            # sort
            result.sort()
            return result


# predefine params
min = 10
max = 10
quantity = 9


# GO
try:

    lottery_numbers = get_numbers_ticket(min, max, quantity)
    print("Ваші лотерейні числа:", lottery_numbers)
except ValueError as exc:
    print(f'Something went wrong, {exc}')
    sys.exit(0)

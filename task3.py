""" import regex module """
import re


def normalize_phone(num: str) -> str:
    """ sanizate telephone numer """

    # get all numers
    raw = re.findall(r'\d+', num)
    raw_tel_numer = ''.join(raw)
    return add_prefix(raw_tel_numer)



def add_prefix(s: str) -> str:
    """ add prefix to telephone numer """

    # mask for case when numer starts from 38
    mask_38 = '38'
    prefix_38 = '+'
    # mask for case when numer starts from 0
    mask_0 = '0'
    prefix_0 = '+38'
    # check masks
    if s.startswith(mask_38):
        return ''.join([prefix_38, s])
    elif s.startswith(mask_0):
        return ''.join([prefix_0,s])
    else:
        # retunr without changes
        return s

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:\n", sanitized_numbers)

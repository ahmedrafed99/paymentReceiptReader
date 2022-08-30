import re


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def detectNumber(string: str):
    value = '\d*(\.|,)\d+|\d+'
    pattern = re.compile(value)
    result = re.search(pattern, string)

    if result:
        number = result.group()
        return number
    else:
        raise Exception("No number found in the following string :\n" + string)


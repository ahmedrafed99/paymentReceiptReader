import re

import nltk
from nltk import TreebankWordDetokenizer


def extract_lines_containing(string:str, text_file:str):
    lines = open(text_file, "r").readlines()
    matches = []
    for line in lines:
        if re.search(string, line):
            matches.append(line)

    return matches

def extract_TVA_percentage(candidates:[str]):
    value = '(\d+((.)\d+)?\s*?%)'
    pattern = re.compile(('TVA.' + value), re.IGNORECASE)
    for candidate in candidates:
        result = re.search(pattern, candidate)
        if result:
            TVA_value = re.search(value, result.group())
            print(TVA_value.group())


def extract_TVA_price(candidates:[str]):

    value = '(TVA 20,00%*\d+(.)\d+(?!%))'
    pattern = re.compile(value, re.IGNORECASE)

    for candidate in candidates:
        print("i am a candidate line in the text, i have the word TVA:\n"+candidate)
        result = re.search(pattern, candidate)
        if result:
            TVA_value = re.search(value, result.group())
            print("found a match!\n" + TVA_value.group() + "\n")


def extract_siren(string: str) -> str:

    if "SIREN".casefold() in string.casefold():
        string = string.replace(" ", "")
        value = '([0-9]{9})'
        pattern = re.compile(value, re.IGNORECASE)
        siren_number = re.search(pattern, string).group()
        print("SIREN : " + siren_number)
    else:
        raise Exception("the word 'SIREN' does not exist in the following string:\n" + string)
    return siren_number

def extract_siret(string:str) -> str:

    if "SIRET".casefold() in string.casefold():
        string = string.replace(" ", "")
        value = '([0-9]{14})'
        pattern = re.compile(value, re.IGNORECASE)
        siret_number = re.search(pattern, string).group()
        print("SIRET : " + siret_number)
    else:
        raise Exception("the word 'SIRET' does not exist in the following string:\n" + string)

    return siret_number

#only works for French phone number formats
def extract_phone_number(string:str):

    string = string.replace(" ", "")
    value = '((\+|00)33|0)[1-9][0-9]{8}'
    pattern = re.compile(value, re.IGNORECASE)
    result = re.search(pattern, string)
    if result:
        phone_number = result.group()
        print("phone number : " + phone_number)
        return phone_number

    raise Exception("No phone number found in the following string that matches the French phone number format :\n" + string)



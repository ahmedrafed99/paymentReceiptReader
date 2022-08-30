import re

import nltk
from nltk import TreebankWordDetokenizer

import maths


def extract_lines_containing(string:str, text_file:str):
    lines = open(text_file, "r").readlines()
    matches = []
    for line in lines:
        if re.search(string, line):
            matches.append(line)

    return matches

def extract_VAT_percentage(string):

    if "TVA".casefold() in string.casefold():
        words = nltk.word_tokenize(string)
        print(words)

        percent_index = words.index("%")
        if percent_index:
            i = percent_index
        else:
            raise Exception("the character '%' does not exist in the following string and therefore the vat percentage does most likely not exist :\n -> " + string)
        while i>0:
            vat_percentage = maths.detectNumber(words[i-1])
            if vat_percentage:
                print("the vat percentage is : " + vat_percentage + "%")
                return vat_percentage
            else:
                i -= 1
        raise Exception("No vat percentage found in the following string :\n " + string)

    raise Exception("The VAT percentage is likely not to be found in the following string as the word 'VAT' does not exist either :\n" + string)



def extract_VAT_price(string:str) -> str:

    if "TVA".casefold() in string.casefold():
        words = nltk.word_tokenize(string)
        print(words)

        percent_index = words.index("%")
        i = percent_index

        while len(words) > i+1:
            vat_price = maths.detectNumber(words[i+1])
            if vat_price:
                print("the vat price is : " + vat_price)
                return vat_price
            else:
                i += 1
        raise Exception("No vat price is found in the following string :\n " + string)

    raise Exception("The VAT price is likely not to be found in the following string as the word 'VAT' does not exist either :\n" + string)


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



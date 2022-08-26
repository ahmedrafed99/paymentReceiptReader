import re


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


    # for candidate in candidates:
    #     words = nltk.word_tokenize(candidate)
    #     results = []
    #     try:
    #         currency = re.search(currency_character, candidate, re.IGNORECASE)
    #         TVA = re.search("T.*V.*A", candidate, re.IGNORECASE)
    #         number = re.search("€?\s+\d+\s+€ | €\s+\d+\s+€?", candidate, re.IGNORECASE)
    #
    #         print(currency)
    #         print(TVA)
    #         print(number)
    #
    #         if currency and TVA and number:
    #             results.append(currency)
    #             results.append(TVA)
    #             results.append(number)
    #
    #             #print(results)
    #             return results
    #
    #     except ValueError:
    #         print('at least one element was not found')
    #         return []

        # if(currency_index != None and 'TVA' in words):
        #
        #
        #     if currency_index == len(words)-1:
        #         if maths.isfloat(words[currency_index-1]):


    #   result = re.search(pattern, candidate)
    #   if result:
    #     print(result.group())



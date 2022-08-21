import re

import nltk
from nltk import word_tokenize, TreebankWordDetokenizer
from nltk.corpus import stopwords

#nltk.download()

def extract_line_contains(data: str) -> str:
    return ""

def remove_unwanted_characters(text: str) -> str:
    cleanTxt = text.replace("_", "")
    cleanTxt = cleanTxt.replace("-", "")
    cleanTxt = cleanTxt.replace(".", "")
    cleanTxt = cleanTxt.replace(";", "")


    return cleanTxt

def process_text(text: str) -> str:
    cleaned_text = remove_unwanted_characters(text)
    filtered_text = remove_stopwords(cleaned_text, 'french')
    #correct_spell(cleaned_text)

    return filtered_text

def remove_stopwords(text: str, language: str):
    stop_words = set(stopwords.words(language))

    #regex will search for all words including \n which is needed to preserve the new lines in the detokenizer in line 36
    word_tokens = re.findall(r'\S+|\n', text)
    filtered_words =[]
    for word in word_tokens:
        if word not in stop_words or word.__eq__('\n'):
            filtered_words.append(word)

    filtered_text = TreebankWordDetokenizer().detokenize(filtered_words)
    return filtered_text






# def check_spell(text: str):
#     words = word_tokenize(text)
#     return misspelled


def correct_spell(text: str):
    return text



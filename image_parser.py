import re

import imutils
from PIL import Image
from numpy import unicode
from pytesseract import image_to_osd, Output
import cv2
from pytesseract import image_to_string
import text_processor
from sys import platform, version_info
import json


def process(imageFilename):
    image = correct_rotation(imageFilename)
    cv2.imwrite("test3.jpeg", image)
    (height, width) = image.shape[:2]
    resizedImage = cv2.resize(image, (width*4, height*4))
    grayImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
    blackWhiteImage = cv2.threshold(grayImage, 230, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite("test_output.jpeg", blackWhiteImage)

    return blackWhiteImage


def to_string(imageFilename, language:str, text_file: str):
    blackWhiteImage = process(imageFilename)
    txt = image_to_string(blackWhiteImage, lang=language)
    cleanTxt = text_processor.process_text(txt)
    cleanTxt_file = open(text_file, "w")
    cleanTxt_file.write(cleanTxt)
    return text_file




def get_orientation_data(imageFilename):
    result = image_to_osd(imageFilename, output_type=Output.DICT)
    return result

def correct_rotation(imageFilename):
    orientation_data = get_orientation_data(imageFilename)
    if orientation_data['orientation'] != 0:
        return imutils.rotate_bound((cv2.imread(imageFilename)), angle=orientation_data['rotate'])
    else:
        return cv2.imread(imageFilename)


def is_rotated(imageFilename):
    return get_orientation_data(imageFilename)['orientation'] != 0

def get_orientation(imageFilename):
    return get_orientation_data(imageFilename['orientation'])

def get_correction_angle(imageFilename):
    return get_orientation_data(imageFilename)['rotate']

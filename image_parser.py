import math
from scipy import ndimage
import imutils
import numpy as np
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
    #blackWhiteImage = process(imageFilename)
    txt = image_to_string(imageFilename, lang=language)
    cleanTxt = text_processor.process_text(txt)
    cleanTxt_file = open(text_file, "w")
    cleanTxt_file.write(cleanTxt)
    print(cleanTxt)
    return text_file




def correct_rotation(filename):
    img_before = cv2.imread(filename)

    img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

    angles = []

    for [[x1, y1, x2, y2]] in lines:
        cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        angles.append(angle)

    height, width = img_before.shape[:2]

    # get the center coordinates of the image to create the 2D rotation matrix

    center = (width / 2, height / 2)
    # using cv2.getRotationMatrix2D() to get the rotation matrix

    median_angle = np.median(angles)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=median_angle, scale=1)

    # rotate the image using cv2.warpAffine

    rotated_image = cv2.warpAffine(src=img_before, M=rotate_matrix, dsize=(width, height))

    # img_rotated = ndimage.rotate(img_before, median_angle)
    cv2.imwrite('rotated.jpg', rotated_image)
    print(median_angle)
    return rotated_image

# def get_rotation_angle(imageFilename):
#     result = cv2.HoughLinesP(cv2.imread(imageFilename))
#     print(result)
#     return result
#
# def correct_rotation(imageFilename):
#     orientation_data = get_rotation_angle(imageFilename)
#     if orientation_data['orientation'] != 0:
#         return imutils.rotate_bound((cv2.imread(imageFilename)), angle=orientation_data['rotate'])
#     else:
#         return cv2.imread(imageFilename)


# def is_rotated(imageFilename):
#     return get_orientation_data(imageFilename)['orientation'] != 0
#
# def get_orientation(imageFilename):
#     return get_orientation_data(imageFilename['orientation'])
#
# def get_correction_angle(imageFilename):
#     return get_orientation_data(imageFilename)['rotate']

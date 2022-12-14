import cv2
from fastapi import FastAPI

import data_extractor
import image_parser
from pytesseract import image_to_string


app = FastAPI()

#text_file = image_parser.to_string("test2.jpeg", 'fra', 'cleantxt.txt')
#matched_lines = data_extractor.extract_lines_containing("TVA", text_file)
#data_extractor.extract_TVA_percentage(matched_lines)

print(data_extractor.extract_VAT_percentage("0,25 0.625 TVA A 20,00%  5,25€"))
#data_extractor.extract_TVA_price(matched_lines)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

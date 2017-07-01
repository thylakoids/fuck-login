# coding=utf-8
#https://github.com/tesseract-ocr
from PIL import Image
import pytesseract
print pytesseract.image_to_string(Image.open('3434.png'),lang='chi_sim')


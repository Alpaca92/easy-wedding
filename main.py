import os

from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

root_dir = "C:/Users/admin/Downloads/test"
list = os.listdir(f"{root_dir}")
number_files = len(list)

for i in range(number_files):
  file = f"{root_dir}/test_{i + 1}.jpg"
  img = Image.open(file)
  text = image_to_string(img, lang='kor')
  
  print(text)


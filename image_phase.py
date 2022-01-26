import os

from PIL import Image
from pytesseract import image_to_string

image_path = 'images/'
input_path = 'inputs/'


def rename_files():

    i = 1
    for filename in os.listdir(image_path):
        dst = "image" + str(i) + ".png"
        src = image_path + filename
        dst = image_path + dst

        os.rename(src, dst)
        i += 1


def count_files():

    i = 0
    for filename in os.listdir(image_path):
        i += 1
    print(f"Total Number of images: {i}")


def convert_images_to_text():

    initial_text = ""
    for filename in os.listdir(image_path):
        src = image_path + filename
        img = Image.open(src)
        text = image_to_string(img, lang='eng')
        initial_text += text

    with open(f"{input_path}scannedquestion.txt", mode='w') as file:
        file.write(initial_text)
    print(
        f'Successful: Questions(image) -> Questions(text)\nLocation: {input_path}scannedquestion.txt')

from PIL import Image

from pytesseract import image_to_string

path = 'images/'
img = Image.open(f"{path}image_file.png")
text = image_to_string(img, lang='eng')

with open('scannedquestion.txt', mode='w') as file:
    file.write(text)

fhandle = open('scannedquestion_modified.txt')
content = fhandle.read()

print(content)
seperated = content.split('\n')

for i in seperated:
    print('------')
    print(i)


from PIL import Image

import pytesseract

data = pytesseract.image_to_string(Image.open('/home/ncs/Downloads/test2.JPEG'))


print(data)
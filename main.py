from converter.ascii_converter import ASCIIConverter
from PIL import Image


original_image_name = 'mises'

image = Image.open(f'./{original_image_name}.jpg')

converter = ASCIIConverter()
new_image = converter.convert_to_ascii(image, f'./{original_image_name}.txt')

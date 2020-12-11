from converter.ascii_converter import ASCIIConverter
from converter.image_saver import ASCIIImageSaver
from PIL import Image


original_image_name = 'knife'

image = Image.open(f'./examples/{original_image_name}.jpg')

converter = ASCIIConverter()
new_image = converter.convert_to_ascii(image)

saver = ASCIIImageSaver()
saver.save_image(new_image, f'./examples/{original_image_name}.txt')

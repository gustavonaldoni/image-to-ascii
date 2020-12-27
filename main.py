from converter.ascii_converter import ASCIIConverter
from converter.image_saver import ASCIIImageSaver
from converter.image_resizer import ImageResizer
from PIL import Image



image = Image.open('examples/snake.png')

converter = ASCIIConverter()
resizer = ImageResizer()
resized_image = resizer.resize_image(image)
new_image = converter.convert_to_ascii(resized_image)

saver = ASCIIImageSaver()
saver.save_image(new_image, 'snake.txt')

from converter.ascii_converter import ASCIIConverter
from converter.image_saver import ASCIIImageSaver
from converter.image_resizer import ImageResizer
from PIL import Image
import sys

default_image_file = 'examples/snake.png'
if len(sys.argv)==1:
  image_file=default_image_file
elif len(sys.argv)==2:
  image_file = sys.argv[1]
  image_width = 100
elif len(sys.argv)>2:
  image_file = sys.argv[1]
  image_width = int(sys.argv[2])
  
image = Image.open(image_file)

resizer = ImageResizer()
resized_image = resizer.resize_image(image,image_width)

converter = ASCIIConverter()
new_image = converter.convert_to_ascii(resized_image)

saver = ASCIIImageSaver()
saver.save_image(new_image, 'snake.txt')

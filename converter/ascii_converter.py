import PIL.Image
from converter.grayscale_converter import GrayscaleConverter
from converter.image_saver import ASCIIImageSaver
from converter.image_resizer import ImageResizer
from confirmation_messages.success_messages import SuccessMessages

class ASCIIConverter(GrayscaleConverter, ASCIIImageSaver, ImageResizer):

    def __init__(self):
        self.success_messages = SuccessMessages()
    
    ASCII_CHARACTERS = '@#$%?*+;:,.'

    def get_ascii_characters(self, image):
        try:
            pixels = image.getdata()
            characters = ''.join([self.ASCII_CHARACTERS[pixel // 25] for pixel in pixels])
            self.success_messages.show_success_message('ASCII characters gotten')

        except Exception as e:
            pass

        return characters

    def format_ascii_characters(self, ascii_characters, new_width=100):
        try:
            formatted = '\n'.join(ascii_characters[i:(i + new_width)] for i in range(0, len(ascii_characters), new_width))
            self.success_messages.show_success_message('ASCII characters successfully formatted')
        except Exception as e:
            pass

        return formatted

    def convert_to_ascii(self, image, path, new_width=None):
        if new_width is None:
            original_width, original_height = self.get_width_and_height(image)
            new_width = round(original_width * 2)

        resized_image = self.resize_image(image, new_width)
        grayscale_image = self.convert_to_grayscale(resized_image)
        ascii_characters = self.get_ascii_characters(grayscale_image)
        formatted_text = self.format_ascii_characters(ascii_characters, new_width)

        self.save_image(formatted_text, path)

        return formatted_text

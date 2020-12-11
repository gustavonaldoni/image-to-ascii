import PIL.Image
from converter.grayscale_converter import GrayscaleConverter
from converter.image_resizer import ImageResizer
from confirmation_messages.success_messages import SuccessMessages
from confirmation_messages.error_messages import ErrorMessages


class ASCIIConverter(GrayscaleConverter, ImageResizer):

    def __init__(self):
        self.success_messages = SuccessMessages()
        self.error_messages = ErrorMessages()
    
    ASCII_CHARACTERS = '@#$%?*+;:,.'

    def get_ascii_characters(self, image):
        try:
            pixels = image.getdata()
            characters = ''.join([self.ASCII_CHARACTERS[pixel // 25] for pixel in pixels])
            self.success_messages.show_success_message('ASCII characters gotten')

        except Exception as e:
            self.error_messages.show_error_message('getting ASCII characters', e)

        return characters

    def format_ascii_characters(self, ascii_characters, new_width=100):
        try:
            formatted = '\n'.join(ascii_characters[i:(i + new_width)] for i in range(0, len(ascii_characters), new_width))
            self.success_messages.show_success_message('ASCII characters successfully formatted')
        
        except Exception as e:
            self.error_messages.show_error_message('formatting ASCII characters', e)

        return formatted

    def convert_to_ascii(self, image, new_width=200):
        resized_image = self.resize_image(image, new_width)
        grayscale_image = self.convert_to_grayscale(resized_image)
        ascii_characters = self.get_ascii_characters(grayscale_image)
        formatted_text = self.format_ascii_characters(ascii_characters, new_width)

        return formatted_text

import PIL.Image
from converter.grayscale_converter import GrayscaleConverter
from converter.image_saver import ASCIIImageSaver


class ASCIIConverter(GrayscaleConverter, ASCIIImageSaver):

    ASCII_CHARACTERS = '@#$%?*+;:,.'

    def resize_image(self, image, new_width=100):
        image = image.copy()

        width, height = image.size
        aspect_ratio = height / width

        new_height = round(width * aspect_ratio)

        resized_image = image.resize((new_width, new_height))

        return resized_image

    def get_ascii_characters(self, image):
        pixels = image.getdata()
        characters = ''.join([self.ASCII_CHARACTERS[pixel // 25] for pixel in pixels])

        return characters

    def format_ascii_characters(self, ascii_characters, new_width=100):
        formatted = '\n'.join(ascii_characters[i:(i + new_width)] for i in range(0, len(ascii_characters), new_width))

        return formatted

    def convert_to_ascii(self, image, path, new_width=100):
        resized_image = self.resize_image(image, new_width)
        grayscale_image = self.convert_to_grayscale(resized_image)

        ascii_characters = self.get_ascii_characters(grayscale_image)
        formatted_text = self.format_ascii_characters(ascii_characters, new_width)

        self.save_image(formatted_text, path)

        return formatted_text
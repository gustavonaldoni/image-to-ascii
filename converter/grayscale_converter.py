from PIL import Image


class GrayscaleConverter:

    def convert_to_grayscale(self, image):
        image = image.copy()
        converted_image = image.convert(mode='L')

        return converted_image
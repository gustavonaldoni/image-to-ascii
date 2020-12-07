from PIL import Image

class ImageResizer:

    def get_width_and_height(self, image):
        width, height = image.size

        return (width, height)

    def resize_image(self, image, new_width=100):
            image = image.copy()

            width, height = self.get_width_and_height(image)
            aspect_ratio = height / width

            new_height = round(width * aspect_ratio)

            resized_image = image.resize((new_width, new_height))

            return resized_image
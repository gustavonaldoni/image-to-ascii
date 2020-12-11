from PIL import Image
from confirmation_messages.success_messages import SuccessMessages
from confirmation_messages.error_messages import ErrorMessages


class ImageResizer:

    def __init__(self):
        self.success_messages = SuccessMessages()
        self.error_messages = ErrorMessages()

    def get_width_and_height(self, image):
        width, height = image.size

        return (width, height)

    def resize_image(self, image, new_width=100):
            image = image.copy()

            width, height = self.get_width_and_height(image)
            aspect_ratio = height / width

            new_height = round(new_width * aspect_ratio * 0.45)

            try:
                resized_image = image.resize((new_width, new_height))
                self.success_messages.show_success_message(f'Image resized from {width}x{height} px to {new_width}x{new_height} px')
                
            except Exception as e:
                self.error_messages.show_error_message('resizing image', e)

            return resized_image
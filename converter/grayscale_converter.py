from PIL import Image
from confirmation_messages.success_messages import SuccessMessages
from confirmation_messages.error_messages import ErrorMessages


class GrayscaleConverter:

    def __init__(self):
        self.success_messages = SuccessMessages()
        self.error_messages = ErrorMessages()

    def convert_to_grayscale(self, image):
        image = image.copy()

        try:
            converted_image = image.convert(mode='L')
            self.success_messages.show_success_message('Image converted to grayscale')
            
        except Exception as e:
            self.error_messages.show_error_message('converting image to grayscale', e)

        return converted_image
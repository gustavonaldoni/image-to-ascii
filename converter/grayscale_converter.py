from PIL import Image
from confirmation_messages.success_messages import SuccessMessages


class GrayscaleConverter:

    def __init__(self):
        self.success_messages = SuccessMessages()

    def convert_to_grayscale(self, image):
        image = image.copy()

        try:
            converted_image = image.convert(mode='L')
            self.success_messages.show_success_message('Image converted to grayscale')
            
        except Exception as e:
            pass

        return converted_image
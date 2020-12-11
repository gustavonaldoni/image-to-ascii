from confirmation_messages.success_messages import SuccessMessages
from confirmation_messages.error_messages import ErrorMessages

class ASCIIImageSaver:

    def __init__(self):
        self.success_messages = SuccessMessages()
        self.error_messages = ErrorMessages()
    
    def save_image(self, text, path):
        try:
            with open(path, 'w') as file:
                file.write(text)
            self.success_messages.show_success_message(f"Imaged saved on path: '{path}'")

        except Exception as e:
            self.error_messages.show_error_message('saving ASCII image', e)
            
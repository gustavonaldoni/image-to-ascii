from confirmation_messages.success_messages import SuccessMessages


class ASCIIImageSaver:

    def __init__(self):
        self.success_messages = SuccessMessages()
    
    def save_image(self, text, path):
        try:
            with open(path, 'w') as file:
                file.write(text)
            self.success_messages.show_success_message(f"Imaged saved on path: '{path}'")

        except Exception as e:
            pass
            
from confirmation_messages.success_messages import SuccessMessages
from confirmation_messages.error_messages import ErrorMessages

class ASCIIImageSaver:
    """
    The ASCIIImageSaver object allows you to save your new ASCII images easily


    Attributes
    ----------

    success_messages : SuccessMessages
        Object that contains the success messages templates

    error_messages : ErrorMessages
        Object that contains the error messages templates

    """

    def __init__(self):
        self.success_messages = SuccessMessages()
        self.error_messages = ErrorMessages()
    
    def save_image(self, text, path):
        """
        Save the ASCII text into a .txt file at a given path


        Parameters
        ----------

        text : str
            The ASCII text to put on the .txt file

        
        Returns
        -------

        None

        """
        try:
            with open(path, 'w') as file:
                file.write(text)
            self.success_messages.show_success_message(f"Imaged saved on path: '{path}'")

        except Exception as e:
            self.error_messages.show_error_message('saving ASCII image', e)
            
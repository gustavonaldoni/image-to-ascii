from PIL import Image
from confirmation_messages.success_messages import SuccessMessages
from confirmation_messages.error_messages import ErrorMessages


class GrayscaleConverter:
    """
    The GrayscaleConverter object allows you to convert
    a image to a grayscale version easily


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

    def convert_to_grayscale(self, image):
        """
        Convert a given image to a grayscale version


        Parameters
        ----------

        image : PIL Image Object
            The image to be converted to grayscale

        
        Returns
        -------

        converted_image : PIL Image Object
            The image already converted to grayscale

        """
        image = image.copy()

        try:
            converted_image = image.convert(mode='L')
            self.success_messages.show_success_message('Image converted to grayscale')
            
        except Exception as e:
            self.error_messages.show_error_message('converting image to grayscale', e)

        return converted_image
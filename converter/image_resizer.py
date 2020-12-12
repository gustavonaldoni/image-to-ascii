from PIL import Image
from confirmation_messages.success_messages import SuccessMessages
from confirmation_messages.error_messages import ErrorMessages


class ImageResizer:
    """
    The ImageResizer object allows you to resize an image easily


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

    def get_width_and_height(self, image):
        """
        Catch the width and height of a given image


        Parameters
        ----------

        image : PIL Image Object
            The image to get the width and height

        
        Returns
        -------

        tuple
            A tuple containing the width and height of the image, respectively

        """
        width, height = image.size

        return (width, height)

    def resize_image(self, image, new_width=100):
        """
        Resize a image, without changing it,
        and following the aspect ratio
        

        Parameters
        ----------

        image : PIL Image Object
            The image to be resized

        new_width : int
            The width of the new image


        Returns
        -------

        resized_image : PIL Image Object
            The new resized image

        """
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
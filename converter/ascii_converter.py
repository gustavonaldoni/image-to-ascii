import PIL.Image
from converter.grayscale_converter import GrayscaleConverter
from converter.image_resizer import ImageResizer
from confirmation_messages.success_messages import SuccessMessages
from confirmation_messages.error_messages import ErrorMessages


class ASCIIConverter(GrayscaleConverter, ImageResizer):
    """
    The ASCIIConverter object allows you to 
    simple convert an image to a ASCII text


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
    
    ASCII_CHARACTERS = '@#$%?*+;:,.'

    def __get_ascii_characters(self, image):
        """
        Convert each pixel from the image to a ASCII character


        Parameters
        ----------

        image : PIL Image Object
            Image used to capture the ASCII characters


        Returns
        -------
            characters : str
                A string containing all ASCII characters from the image

        """
        try:
            pixels = image.getdata()
            characters = ''.join([self.ASCII_CHARACTERS[pixel // 25] for pixel in pixels])
            self.success_messages.show_success_message('ASCII characters gotten')

        except Exception as e:
            self.error_messages.show_error_message('getting ASCII characters', e)

        return characters

    def __format_ascii_characters(self, ascii_characters, new_width=200):
        """
        Format the ASCII characters to make them form a 'image'


        Parameters
        ----------

        ascii_characters : str
            The ASCII characters to be formatted

        new_width : int
            The width of the new image
            Has the default value of 200


        Returns 
        -------

        formatted : str
            A formatted string containing the text of the new ASCII image

        """
        try:
            formatted = '\n'.join(ascii_characters[i:(i + new_width)] for i in range(0, len(ascii_characters), new_width))
            self.success_messages.show_success_message('ASCII characters successfully formatted')
        
        except Exception as e:
            self.error_messages.show_error_message('formatting ASCII characters', e)

        return formatted

    def convert_to_ascii(self, image, new_width=200):
        """
        Converts a image to a ASCII version


        Parameters
        ----------

        image : PIL Image Object
            The image you want to convert to ASCII

        new_width : int
            The width of the new ASCII image

        
        Returns
        -------

        formatted_text : str
            The new ASCII image already formatted

        """
        resized_image = self.resize_image(image, new_width)
        grayscale_image = self.convert_to_grayscale(resized_image)
        ascii_characters = self.__get_ascii_characters(grayscale_image)
        formatted_text = self.__format_ascii_characters(ascii_characters, new_width)

        return formatted_text

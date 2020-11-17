import pytesseract as tes
import web_ocr.settings as settings
import os
def retrive_text(gray_image):
    """
    :param : gray_image processed gray image
    :return: text from image
    """

    result = tes.image_to_string(gray_image, lang='deu')
    return result


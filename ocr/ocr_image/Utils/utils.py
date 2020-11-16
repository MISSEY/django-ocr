import os
from  ocr.ocr_image.Config import config
from ocr.ocr_image.Utils.logger import get_logger


def create_directory(uiid):
    """
    Create a ouput directory for processed images
    :return:
    """

    path = os.path.join(config.image_data["save_path"] ,uiid)

    try:
        os.makedirs(path)

    except OSError:
        # print ("Creation of the directory %s failed" )
        i = 1

    else:
        logger = get_logger("Create_directory")
        logger.debug("Successfully created the directory %s" % path)
    return path
from .Config import config
from .Utils import utils
from .OCR import ocr
from .Preprocessing import image_processing
import cv2
import numpy as np
from uuid import uuid4
import shutil
import ctypes

import multiprocessing as mp

def process(shared,image):
    print(shared.value)
    uuid = shared.value.decode('utf-8')
    gray_pre = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_pre = cv2.threshold(gray_pre, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray_pre = cv2.medianBlur(gray_pre, 3)
    gray_pre = cv2.GaussianBlur(gray_pre, (5, 5), 0)
    edged = cv2.Canny(gray_pre, 10, 50)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    rectangle_box = None
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            rectangle_box = approx
            break

    path = utils.create_directory(uuid)
    pts = np.array(rectangle_box.reshape(4, 2))
    cropped_image = image_processing.image_crop_and_transfrom(image,pts)
    file_name = uuid + ".jpg"
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    text = ocr.retrive_text(gray)
    if(len(text) >=40):
        text_file = open(str(path) + "\\" + uuid + ".txt", "w")
        text_file.writelines(text)
        text_file.close()
        cv2.imwrite(str(path) + "\\" + file_name, cropped_image)
    else:
        text = ocr.retrive_text(gray_pre)
        text_ = ocr.retrive_text(image)
        if(len(text)>=40 and len(text_)>=40):
            text_file = open(str(path) + "\\" + uuid + ".txt", "w")
            text_file.writelines(text)
            text_file.close()

            text_file = open(str(path) + "\\" + uuid + "(2).txt", "w")
            text_file.writelines(text_)
            text_file.close()

            cv2.imwrite(str(path) + "\\" + file_name, image)
        else:
            shutil.rmtree(path)


def main(image):
    uuiid = str(uuid4())
    shared_channel_state = mp.Array(ctypes.c_char, len(uuiid))
    shared_channel_state.value = str(uuiid).encode('utf-8')
    print(shared_channel_state)
    ocr_worker = mp.Process(target=process, args=(shared_channel_state,image,))
    ocr_worker.start()
    return uuiid


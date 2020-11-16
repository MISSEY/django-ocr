import cv2
import numpy as np
import imutils

def get_rectangular_points(pts):
    """

    :param pts: points of rectangle after finding counters
    :return: return set of rectangular coordinates
    """
    ## variable for storing points of rectangle
    rect = np.zeros((4, 2), dtype="float32")

    ## Sum for first point is minimum and 4th point is maximum, diagonals
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    ## difference for 2nd point is minimum and 3rd point is maximum, so another diagonal
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def image_crop_and_transfrom(image,pts):
    """

    :param image: original image
    :param pts: points detected after the rectangle, contours
    :return:  return cropped image
    """
    rect = get_rectangular_points(pts)
    (tl, tr, br, bl) = rect

    ## cropping
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped


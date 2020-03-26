import numpy as np
import cv2


def create_opencv_image(
    image_as_bytearray: bytearray, width: int = 25, height: int = 25
) -> np.matrix:
    """
        Given an image, converts it into a workable opencv2 object
        for easy numerical parsing.
    """
    img_array = np.asarray(image_as_bytearray, dtype=np.uint8)
    image_bgr = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

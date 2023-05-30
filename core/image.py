from typing import Generator

import cv2
import numpy as np


def _get_pixel(pixel: str):
    if pixel == "0":
        return 0

    if pixel == "1":
        return 255

    return 128


def generate_image_from_frame(
    width: int, height: int, frame_gen: Generator[str, None, str]
):
    for frame in frame_gen:
        if len(frame) < width * height:
            rem = (width * height) - len(frame)
            frame += "".join(["2"] * rem)

        numbers = [_get_pixel(f) for f in frame]
        numbers_py = np.array(numbers, dtype=np.uint8).reshape(width, height)

        yield numbers_py

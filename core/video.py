from typing import Generator

import cv2
import numpy as np


def generate_video_from_image(
    width: int,
    height: int,
    frame_rate: int,
    image_gen: Generator[np.array, None, np.array],
):
    frameSize = (width, height)
    out = cv2.VideoWriter(
        "./data/output_video.avi",
        cv2.VideoWriter_fourcc(*"DIVX"),
        frame_rate,
        frameSize,
        0,
    )

    for image in image_gen:
        out.write(image)

    out.release()

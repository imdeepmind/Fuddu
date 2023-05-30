from core.read import read_large_file
from core.binary import get_binary
from core.frame import generate_frames
from core.image import generate_image_from_frame
from core.video import generate_video_from_image

file_name = "./data/text.txt"


read_gen = read_large_file(file_name)
binary_gen = get_binary(read_gen)
frame_gen = generate_frames(500, 500, binary_gen)
image_gen = generate_image_from_frame(500, 500, frame_gen)


generate_video_from_image(500, 500, 24, image_gen)


# import cv2
# import numpy as np


# frameSize = (500, 500)

# out = cv2.VideoWriter(
#     "output_video.avi", cv2.VideoWriter_fourcc(*"DIVX"), 60, frameSize
# )

# for i in range(0, 255):
#     img = np.ones((500, 500, 3), dtype=np.uint8) * i
#     out.write(img)

# out.release()

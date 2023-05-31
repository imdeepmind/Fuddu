import cv2
import numpy as np


class TextToVideo:
    def __init__(
        self,
        width: int,
        height: int,
        frame_rate: int,
        path_to_text: str,
        path_to_video_output: str,
    ) -> None:
        self._width = width
        self._height = height
        self._frame_rate = frame_rate
        self._path_to_text = path_to_text
        self._path_to_video_output = path_to_video_output

    def _text_to_ascii(self):
        with open(self._path_to_text, mode="r", buffering=10000, encoding="ascii") as f:
            for line in f:
                yield [ord(x) for x in line]

    def _ascii_to_frame(self):
        size = self._width * self._height
        carry = []

        for binary in self._text_to_ascii():
            n = len(binary) + len(carry)

            if size > n:
                carry += binary
                continue
            else:
                # TODO: Fix the frame and carry size
                frame = carry + binary[: size - len(carry)]
                carry = binary[size - len(carry) :]

                yield frame

        yield carry

    def _frame_to_video(self):
        frameSize = (self._width, self._height)
        out = cv2.VideoWriter(
            self._path_to_video_output,
            cv2.VideoWriter_fourcc(*"DIVX"),
            self._frame_rate,
            frameSize,
            0,
        )

        for frame in self._ascii_to_frame():
            if len(frame) < self._width * self._height:
                rem = (self._width * self._height) - len(frame)
                frame += [255] * rem

            numbers_py = np.array(frame, dtype=np.uint8).reshape(
                self._width, self._height
            )

            out.write(numbers_py)


t = TextToVideo(100, 100, 1, "./data/sample.txt", "./data/video.avi")
t._frame_to_video()

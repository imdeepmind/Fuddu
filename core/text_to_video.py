import cv2
import numpy as np
from ._cli import progress_bar_inf


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

        self._buffering_size = 1024 * 1024 * 100
        self._encoding_type = "ascii"

    def _text_to_ascii(self):
        with open(
            self._path_to_text,
            mode="r",
            buffering=self._buffering_size,
            encoding=self._encoding_type,
        ) as f:
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
                frame = carry + binary[: size - len(carry)]
                carry = binary[size - len(carry) :]

                yield frame

        yield carry

    def convert(self):
        frameSize = (self._width, self._height)
        out = cv2.VideoWriter(
            self._path_to_video_output,
            cv2.VideoWriter_fourcc(*"DIVX"),
            self._frame_rate,
            frameSize,
            0,
        )

        with progress_bar_inf as p:
            for frame in p.track(self._ascii_to_frame(), description="Converting"):
                if len(frame) < self._width * self._height:
                    rem = (self._width * self._height) - len(frame)
                    frame += [255] * rem

                numbers_py = np.array(frame, dtype=np.uint8).reshape(self._width, self._height)

                out.write(numbers_py)

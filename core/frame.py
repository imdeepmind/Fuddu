from typing import Generator

def generate_frames(width: int, height: int, binary_gen: Generator[str, None, str]):
    size = width * height
    carry = ""


    for binary in binary_gen:
        n = len(binary) + len(carry)

        if size > n:
            carry += binary
            continue
        else:
            # TODO: Fix the frame and carry size
            frame = carry + binary[:size-len(carry)]
            carry = binary[size-len(carry)-1:]

            yield frame

    yield carry
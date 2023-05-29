from typing import Generator

def get_binary(read_gen: Generator[str, None, str]) -> str:
    """Convert the ASCII text to binary representation

    Args:
        read_gen (Generator): Generator function that reads the target file

    Yields:
        str: Binary Representation
    """
    for line in read_gen:
        yield ''.join(format(ord(x), 'b') for x in line)
def read_large_file(path: str):
    """Read large files with buffer size of 10000. Only supports ASCII text.

    Args:
        path (str): Path of the file to read

    Yields:
        str: Returns each line in the text file
    """
    with open(path, mode="r", buffering=10000, encoding="ascii") as f:
        for line in f:
            yield line

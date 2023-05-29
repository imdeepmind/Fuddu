from core.read import read_large_file
from core.binary import get_binary
from core.frame import generate_frames

file_name = "./data/text.txt"

read_gen = read_large_file(file_name)
binary_gen = get_binary(read_gen)
frame_gen = generate_frames(100, 100, binary_gen)


len_b = 0
len_f = 0

for b in get_binary(read_large_file(file_name)):
    len_b += len(b)

for f in frame_gen:
    len_f += len(f)

print(len_b, len_f)
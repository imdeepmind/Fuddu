from rich.prompt import Prompt
from rich.console import Console

from core import get_arg, TextToVideo, print, print_json

console = Console()
console.print(
    "[blue]Welcome to Fuddu: A CLI application for converting text to video or video to text."
)
console.print("[blue]You're in the text to video module.")

console.rule("[bold red]Please provide some details needed for the conversion")

width = Prompt.ask(
    "Please enter the width for the video", default=100, show_default=True
)
height = Prompt.ask(
    "Please enter the height for the video", default=100, show_default=True
)
frame_rate = Prompt.ask(
    "Please enter the frame rate for the video", default=60, show_default=True
)

path_to_text = Prompt.ask("Please enter the path to the text file")
path_to_video_output = Prompt.ask("Please enter the path to the output video file")


console.log("Started converting the text to the video")

ttv = TextToVideo(
    width=int(width),
    height=int(height),
    frame_rate=int(frame_rate),
    path_to_text=path_to_text,
    path_to_video_output=path_to_video_output,
)

ttv.convert()

console.log(
    f"Converted the video to text, please check the output path {path_to_video_output} for the video."
)

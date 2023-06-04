import argparse
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
    SpinnerColumn,
)
from rich.console import Console
from rich_argparse import RichHelpFormatter

progress_bar_inf = Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    MofNCompleteColumn(),
    TextColumn("•"),
    TimeElapsedColumn(),
)

console = Console()


def print(text: str):
    console.log(text)


def print_json(text):
    console.print_json(data=text)


def get_arg():
    parser = argparse.ArgumentParser(formatter_class=RichHelpFormatter)
    parser.add_argument(
        "--width",
        help="Provide the width for the generated video",
        required=True,
        type=int,
    )

    parser.add_argument(
        "--height",
        help="Provide the height for the generated video",
        required=True,
        type=int,
    )

    parser.add_argument(
        "--frame_rate",
        help="Provide the frame rate for the generated video",
        required=True,
        type=int,
    )

    parser.add_argument(
        "--input",
        help="Provide the input path for the text to be converted",
        required=True,
    )

    parser.add_argument(
        "--output",
        help="Provide the output path for the generated video",
        required=True,
    )

    values = parser.parse_args()

    return {
        "width": values.width,
        "height": values.height,
        "frame_rate": values.frame_rate,
        "path_to_text": values.input,
        "path_to_video_output": values.output,
    }


__all__ = ["print", "progress_bar_inf", "get_arg"]

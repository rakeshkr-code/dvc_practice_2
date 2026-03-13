"""
Read and print the contents of a text file.
Run the command: `python main.py <path_to_your_file.txt>`
"""

import argparse
from pathlib import Path

def read_txt_file(file_path: Path) -> str:
    """Read and return the contents of a text file."""
    with file_path.open("r", encoding="utf-8") as f:
        return f.read()


def validate_txt_file(path_str: str) -> Path:
    """Validate that the given path exists and is a .txt file."""
    path = Path(path_str)

    if not path.exists():
        raise FileNotFoundError(f"File does not exist: {path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("Input file must have a .txt extension")

    return path


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Read and print a text file.")
    parser.add_argument(
        "file_path",
        type=str,
        # default="data/myfile.txt",
        help="Path to the text file to read",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        txt_path = validate_txt_file(args.file_path)
        content = read_txt_file(txt_path)
        print(content)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
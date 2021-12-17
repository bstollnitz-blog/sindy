"""Data proccessing step."""

import argparse
import logging
from pathlib import Path

from common import DATA_DIR, get_absolute_dir
from utils_video import track_object


def main() -> None:
    logging.info("Processing data.")
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_dir", dest="data_dir", default=DATA_DIR)
    args = parser.parse_args()
    data_dir = get_absolute_dir(args.data_dir)

    input_file_name = "damped_oscillator_900.mp4"
    input_file_path = str(Path(data_dir, input_file_name))
    bbox = (269, 433, 378, 464)
    output_file_name = "damped_oscillator_900_tracked.avi"
    output_file_path = str(Path(get_absolute_dir(DATA_DIR), output_file_name))
    centers = track_object(input_file_path, bbox, output_file_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

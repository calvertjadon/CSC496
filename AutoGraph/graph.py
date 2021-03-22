import os
import argparse
from pprint import pprint
from graph import load_configurations


parser = argparse.ArgumentParser()
parser.add_argument(
    "-d",
    "--directory",
    help="Folder containing benchmark data",
)

args = parser.parse_args()

directory_abs: str = os.path.abspath(args.directory)
configs = load_configurations(directory_abs)

# pprint(configs)

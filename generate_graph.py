#!/usr/bin/python3

import os
import shutil
import subprocess
import sys

try:
    ROOT_DIR = os.getcwd()
    WORKING_DIR = sys.argv[1]
except IndexError:
    # no dir provided
    sys.exit("Error: a directory must be provided")

os.chdir(WORKING_DIR)

# constants
FRAMES_FOLDER_PATH = os.path.join(os.getcwd(), "frames")

# delete old csv files
try:
    shutil.rmtree(FRAMES_FOLDER_PATH)
except FileNotFoundError:
    pass
os.mkdir(FRAMES_FOLDER_PATH)

# get all hwinfo64 csv files
output = subprocess.check_output(
    ["find", ".", "-name", "HWiNFO64.CSV"]
)

# clean up output and filter out blanks
files = list(filter(
    lambda x: x != "",
    [
        path.replace("./", "")
        for path in output.decode().splitlines()
    ]
))

# extract headers (folder names) from file paths
headers = [
    path.split("/")[0]
    for path in files
]

# map headers to file path
files_dict = dict(zip(headers, files))

# sort headers
headers = sorted(headers)

# use awk to extract fps column and write it to frames/<header>.csv
for i in range(len(headers)):
    full_path = os.path.join(os.getcwd(), files_dict[headers[i]])

    output = subprocess.check_output(
        ["awk", "-F", ",", '{print $188}', full_path]
    )

    lines = output.decode().splitlines()
    lines[0] = headers[i]

    with open(os.path.join(FRAMES_FOLDER_PATH, f"{headers[i]}.csv"), "w") as f:
        f.writelines("\n".join(lines))

# merge columns into graph_me.csv
with open(os.path.join(FRAMES_FOLDER_PATH, "graph_me.csv"), "w") as f:
    args = ["paste", "-d", ","]
    args.extend(
        [os.path.join(FRAMES_FOLDER_PATH, f"{header}.csv")
         for header in headers]
    )

    output = subprocess.check_output(args).decode()
    f.writelines(output)

# generate png plot based off graph_me.csv
subprocess.call(["gnuplot", "-c", os.path.join(ROOT_DIR, "gnu.plot")])

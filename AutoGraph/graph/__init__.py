import os

from pprint import pprint
from datetime import datetime

from graph.Benchmark import Benchmark
from graph.Configuration import Configuration

"""
Write a script in the language of your choice to extract the benchmarks from these folders and graph them by game and GPU.
So for example Borderlands 3 is tested at 3 different resolutions on both GPUs.
The output of your program should generate an image for each Game and in the image is a graph of the frame rate.
Ideally the graph would show the average framerate and show what the 1% and .1% lows were overall.

The graph should be clear to the end-user what it is a graph of (which game, what cpu), and you should include a label such as "More is better" or "Less is better."
"""


def __get_subdirs(abs_path: str) -> list[str]:
    return next(os.walk(abs_path))[1]


def load_configurations(abs_path: str) -> list[Configuration]:
    configs: list[Configuration] = []

    processors = __get_subdirs(abs_path)
    for cpu in processors:
        cpu_path = os.path.join(abs_path, cpu)

        graphics_cards = __get_subdirs(cpu_path)
        for gpu in graphics_cards:
            gpu_path = os.path.join(cpu_path, gpu)

            benchmarks = {}
            benchmark_path = os.path.join(gpu_path, "Benchmark.txt")
            with open(benchmark_path, "r") as f:
                # 10-03-2021, 12:30:09
                # first 20 chars

                # line = f.readline()

                # lines = list(filter(lambda line: line != "\n", f.readlines()))
                lines = list(filter(lambda line: line != "",
                                    [line.strip() for line in f.readlines()]
                                    ))

                STEP = 6
                for i in range(0, len(lines), STEP):
                    # header
                    # print(lines[i])

                    dt = datetime.strptime(
                        lines[i][:20],
                        "%d-%m-%Y, %H:%M:%S"
                    ).strftime("%m/%d/%Y")

                    game = lines[i].split(
                        " "
                    )[2].replace(".exe", "")
                    print(game, dt)

                    # data
                    for j in range(i+1, i + STEP):
                        print(lines[j])

                # for line in f.readlines():
                #     try:
                #

                #         bnckmrk["game"] = line.split(
                #             " "
                #         )[2].replace(".exe", "")

                #         bnckmrk["timestamp"] = dt

                #         while

                #     except ValueError:
                #         pass

    return configs

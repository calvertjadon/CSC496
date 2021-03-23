import csv
import matplotlib.pyplot as plt
from pprint import pprint
import pandas as pd
from collections import Counter
import numpy as np
import os
import shutil


def plot_avg_fps_graph(game: str, cpu: str, graphics: str, benchmark: dict[str, dict[str, dict[str, float]]]):

    graphics_cards = list(benchmark.keys())

    gpi1_data = benchmark["Reference 6700XT"]

    plt.style.use("fivethirtyeight")

    x = np.arange(3)

    # print(x)

    BAR_WIDTH = 0.2
    PADDING = .01

    plt.xkcd()

    fig, ax = plt.subplots()

    rects = []

    resolutions = []

    for gpu in graphics_cards:
        resolutions = sorted(benchmark[gpu].keys())
        y_pos = (x-BAR_WIDTH*graphics_cards.index(gpu) +
                 BAR_WIDTH*(len(graphics_cards)-1)/2)

        rects.append(
            ax.barh(
                y_pos,
                [
                    benchmark[gpu][resolution]["Average framerate"]
                    for resolution in resolutions
                ],
                BAR_WIDTH,
                label=gpu
            )
        )

    ax.set_ylabel("Resolutions")
    ax.set_xlabel("Average FPS")
    ax.set_title(
        f"Graphics: {graphics} | CPU: {cpu} | Higher is better",
        fontdict={
            "size": 8,
            "horizontalalignment": "left"
        },
        loc='left'
    )
    ax.set_yticks(x)
    ax.set_yticklabels([f"{r}p" for r in resolutions])
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            width = rect.get_width()
            ax.annotate(
                f"{width}",
                xy=(
                    width/2,
                    rect.get_y(),
                ),
                xytext=(0, 8),
                textcoords="offset points",
                ha="center",
                va="center"
            )

    for rect in rects:
        autolabel(rect)

    plt.suptitle(f"{game} Benchmark", fontdict={
        "size": 12, "horizontalalignment": "left"})
    fig.tight_layout()

    IMAGES_FOLDER = os.path.join(
        os.getcwd(),
        "images"
    )

    plt.savefig(
        fname=os.path.join(
            IMAGES_FOLDER,
            f"{game}_{graphics}.png"
        )
    )

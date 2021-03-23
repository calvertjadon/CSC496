import csv
import matplotlib.pyplot as plt
from pprint import pprint
import pandas as pd
from collections import Counter
import numpy as np


horizon_stock = {
    'Reference 6700XT': {
        '1080': {
            '0.1% low framerate': 78.4,
            '1% low framerate': 86.0,
            'Average framerate': 116.9,
            'Maximum framerate': 151.9,
            'Minimum framerate': 85.7
        },
        '1440': {
            '0.1% low framerate': 69.2,
            '1% low framerate': 72.9,
            'Average framerate': 94.7,
            'Maximum framerate': 132.9,
            'Minimum framerate': 72.9
        },
        '4K': {
            '0.1% low framerate': 39.2,
            '1% low framerate': 40.4,
            'Average framerate': 49.3,
            'Maximum framerate': 61.1,
            'Minimum framerate': 40.1
        }
    },
    'Sapphire 6700XT': {
        '1080': {
            '0.1% low framerate': 77.3,
            '1% low framerate': 83.6,
            'Average framerate': 113.5,
            'Maximum framerate': 148.1,
            'Minimum framerate': 83.7
        },
        '1440': {
            '0.1% low framerate': 67.7,
            '1% low framerate': 71.3,
            'Average framerate': 92.5,
            'Maximum framerate': 112.7,
            'Minimum framerate': 71.1
        },
        '4k': {
            '0.1% low framerate': 38.1,
            '1% low framerate': 40.7,
            'Average framerate': 49.5,
            'Maximum framerate': 61.7,
            'Minimum framerate': 40.7
        }
    }
}

reference = horizon_stock["Reference 6700XT"]
sapphire = horizon_stock["Sapphire 6700XT"]

reference_avgs = [
    resolution["Average framerate"]
    for resolution in reference.values()
]
sapphire_avgs = [
    resolution["Average framerate"]
    for resolution in sapphire.values()
]

resolutions = list(reference.keys())
print(resolutions)

# PLOTTING
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
# https://stackoverflow.com/questions/15201386/how-to-plot-multiple-horizontal-bars-in-one-chart-with-matplotlib
plt.style.use("fivethirtyeight")

x = np.arange(len(resolutions))

print(x)

BAR_WIDTH = 0.2
PADDING = .01

# plt.xkcd()

fig, ax = plt.subplots()
rects1 = ax.barh(x - BAR_WIDTH/2 - PADDING, reference_avgs,
                 BAR_WIDTH, label="Reference")
rects2 = ax.barh(x + BAR_WIDTH/2 + PADDING, sapphire_avgs,
                 BAR_WIDTH, label="Sapphire")

ax.set_ylabel("Resolutions")
ax.set_xlabel("Average FPS")
ax.set_title(
    "Graphics: stock | CPU: 5950x | Higher is better",
    fontdict={
        "size": 8,
        "horizontalalignment": "left"
    },
    loc='left'
)
ax.set_yticks(x)
ax.set_yticklabels(resolutions)
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


autolabel(rects1)
autolabel(rects2)

plt.suptitle("HorizonZeroDawn Benchmark", fontdict={
    "size": 12, "horizontalalignment": "left"})
fig.tight_layout()

plt.savefig(fname="plot.png")
# plt.show()

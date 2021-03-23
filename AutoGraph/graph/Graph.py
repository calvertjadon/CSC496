from matplotlib import pyplot as plt
import numpy as np
import os


class Graph():
    def __init__(self, game: str, cpu: str, graphics_settings: str, graphics_cards: list[str], resolutions: list[str], benchmark_data: dict[str, dict[str, float]], key: str) -> None:
        # STYLING
        plt.style.use("fivethirtyeight")

        self.BAR_WIDTH = 0.2
        self.BAR_PADDING = 0.01

        self.X_LABEL = "Average FPS"
        self.Y_LABEL = "Resolutions"

        # CONFIGURATION
        self.game = game
        self.graphics_settings = graphics_settings
        self.cpu = cpu

        self.resolutions = resolutions
        self.graphics_cards = graphics_cards
        self.benchmark_data = benchmark_data
        self.key = key

        self.IMAGES_FOLDER_PATH = os.path.join(
            os.getcwd(),
            "images"
        )

    def plot(self):
        figure, axis = plt.subplots()

        # define our y range
        y = np.arange(len(self.resolutions))

        # create our bars
        rects = []
        for gpu in self.graphics_cards:
            y_pos = (
                y-self.BAR_WIDTH*self.graphics_cards.index(gpu) +
                self.BAR_WIDTH*(len(self.graphics_cards)-1)/2
            )
            rects.append(
                axis.barh(
                    y_pos,
                    [
                        self.benchmark_data[gpu][resolution][self.key]
                        for resolution in self.resolutions
                    ],
                    self.BAR_WIDTH,
                    label=gpu
                )
            )

        # label everything
        axis.set_ylabel(self.Y_LABEL)
        axis.set_xlabel(self.X_LABEL)
        axis.set_title(
            f"Graphics: {self.graphics_settings} | CPU: {self.cpu} | Higher is better",
            fontdict={
                "size": 8,
                "horizontalalignment": "left"
            },
            loc='left'
        )
        plt.suptitle(f"{self.game} Benchmark", fontdict={
            "size": 12, "horizontalalignment": "left"})

        for rect in rects:
            self.__autolabel(axis, rect)

        axis.set_yticks(y)
        axis.set_yticklabels([f"{r}p" for r in self.resolutions])
        axis.legend()

        # adjust layout
        figure.tight_layout()

        # save to file
        plt.savefig(
            fname=os.path.join(
                self.IMAGES_FOLDER_PATH,
                f"{self.game}_{self.graphics_settings}.png"
            )
        )

    @staticmethod
    def __autolabel(axis, rects):
        for rect in rects:
            width = rect.get_width()
            axis.annotate(
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

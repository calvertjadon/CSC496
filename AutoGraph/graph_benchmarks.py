from graph.Graph import Graph
from graph import load_benchmark_data
import os
import shutil


IMAGES_FOLDER = os.path.join(
    os.getcwd(),
    "images"
)

try:
    shutil.rmtree(IMAGES_FOLDER)
except FileNotFoundError:
    pass
os.mkdir(IMAGES_FOLDER)

data = load_benchmark_data()

configurations = list(data.keys())
for config in configurations:
    cpu, game, graphics = config
    graphics_cards = list(data[config].keys())
    benchmark_data = data[config]

    # sys.exit()

    resolutions = set()
    for gpu in graphics_cards:
        for r in benchmark_data[gpu].keys():
            resolutions.add(r)

    avg_fps = Graph(
        game=game,
        cpu=cpu,
        graphics_settings=graphics,
        graphics_cards=graphics_cards,
        resolutions=sorted(resolutions),
        benchmark_data=benchmark_data,
        key="Average framerate"
    )

    avg_fps.plot()

import os

"""
Write a script in the language of your choice to extract the benchmarks from these folders and graph them by game and GPU.
So for example Borderlands 3 is tested at 3 different resolutions on both GPUs.
The output of your program should generate an image for each Game and in the image is a graph of the frame rate.
Ideally the graph would show the average framerate and show what the 1% and .1% lows were overall.

The graph should be clear to the end-user what it is a graph of (which game, what cpu), and you should include a label such as "More is better" or "Less is better."
"""


def __get_subdirs(abs_path: str) -> list[str]:
    return next(os.walk(abs_path))[1]


def load_benchmark_data() -> dict[str, dict[str, dict[str, dict[str, dict[str, float]]]]]:

    abs_path = os.getcwd()
    FOLDERS_TO_IGNORE = ["graph", "__pycache__",
                         "matplotlib_examples", ".vscode", "images"]

    # cpus
    processors = list(filter(
        lambda f: f not in FOLDERS_TO_IGNORE,
        __get_subdirs(abs_path)
    ))

    # gpus
    configs = []
    for cpu in processors:
        cpu_folder_path = os.path.join(
            abs_path,
            cpu
        )

        gpus = __get_subdirs(cpu_folder_path)
        configs.extend([
            (cpu, gpu) for gpu in gpus
        ])

    # print(configs)

    BENCHMARK_FILE_NAME = "Benchmark.txt"

    benchmarks = {}
    resolutions = set()
    resolution_mappings = {
        "HD": (1280, 720),
        "FHD": (1920, 1080),
        "QHD": (2560, 1440),
        "UHD": (3840, 2160),
        "4K": (3840, 2160),
        "8K": (7680, 4320)
    }

    # read benchmark file for each configuration
    for cpu, gpu in configs:
        benchmark_file_path = os.path.join(
            abs_path,
            cpu,
            gpu,
            BENCHMARK_FILE_NAME
        )
        # print(benchmark_file_path)

        with open(benchmark_file_path, "r") as f:
            # remove empty lines
            lines = list(
                filter(
                    lambda line: line != "",
                    [line.strip() for line in f.readlines()]
                )
            )

            STEP = 6  # header row every n rows, n-1 data rows follow
            for i in range(0, len(lines), STEP):
                # extract data from header
                game = lines[i]\
                    .split(" ")[2]\
                    .strip()\
                    .replace(".exe", "")

                resolution, graphics = lines[i].split()[-2:]

                mapping = resolution_mappings.get(resolution.upper())
                if mapping:
                    resolution = f"{mapping[1]}"

                resolutions.add(resolution)

                benchmarks.setdefault((cpu, game, graphics), {})
                benchmarks[(cpu, game, graphics)].setdefault(gpu, {})
                benchmarks[(cpu, game, graphics)][gpu].setdefault(
                    resolution, {})

                # benchmark data
                for j in range(i+1, i + STEP):
                    sensor, data = [s.strip() for s in lines[j].split(":")]
                    benchmarks[(cpu, game, graphics)
                               ][gpu][resolution][sensor] = float(
                        data.split()[0]
                    )

    return benchmarks

"""
Benchmark results:
AMD Ryzen 9 5950X 16-Core Processor             (16 Gb) / AMD Radeon RX 6700 XT
average FPS = 61.8
min FPS = 43.3
max FPS = 72.9
1% low FPS = 53.7
0.1% low FPS = 44.2
averageCpuTimeMs = 4.14
averageGpuTime: WholeFrame (ms) = 15.87
averageGpuTime: DepthPass (ms) = 1.71
averageGpuTime: OpaquePass (ms) = 5.02
averageGpuTime: PrplDepthPass (ms) = 0.00
averageGpuTime: BlendedPass (ms) = 0.56
averageGpuTime: Shadows (ms) = 1.33
averageGpuTime: LightProbes (ms) = 1.57
averageGpuTime: SimpleViews (ms) = 0.22
averageGpuTime: Lighting (ms) = 2.10
averageGpuTime: UpdateHistory (ms) = 0.72
averageGpuTime: PostEffects (ms) = 0.21
"""


from graph.Configuration import Configuration


class Benchmark:
    def __init__(self, data: dict[str, str], config: Configuration) -> None:
        self.config = config
        self.data = data

    @staticmethod
    def from_file(abs_path: str, config: Configuration) -> "Benchmark":
        data = {}

        with open(abs_path, "r") as f:
            next(f)  # skip first line
            cpu, gpu = next(f).split("             ")
            # cpu, gpu = f.readline().split("\t")

            for line in f.readlines():
                sensor, value = line.split(" = ")
                data[sensor] = value

        return Benchmark(data, config)

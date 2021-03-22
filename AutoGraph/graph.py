import os
import argparse
from pprint import pprint
from graph import load_configurations


parser = argparse.ArgumentParser()
parser.add_argument(
    "-d",
    "--directory",
    help="Folder containing benchmark data",
    default="."
)

args = parser.parse_args()

directory_abs: str = os.path.abspath(args.directory)
configs = load_configurations(directory_abs)

# pprint(configs)

"""
('SOTTR', '5950x', 'stock'): {'Reference 6700XT': {'1080': {'0.1% low framerate': 42.7,
                                                             '1% low framerate': 110.6,
                                                             'Average framerate': 175.4,
                                                             'Maximum framerate': 311.2,
                                                             'Minimum framerate': 121.7},
                                                    '1440': {'0.1% low framerate': 44.7,
                                                             '1% low framerate': 99.9,
                                                             'Average framerate': 131.0,
                                                             'Maximum framerate': 211.1,
                                                             'Minimum framerate': 102.1},
                                                    '4k': {'0.1% low framerate': 44.0,
                                                           '1% low framerate': 61.6,
                                                           'Average framerate': 74.2,
                                                           'Maximum framerate': 111.5,
                                                           'Minimum framerate': 61.5}},
                               'Sapphire 6700XT': {'1080': {'0.1% low framerate': 44.6,
                                                            '1% low framerate': 117.6,
                                                            'Average framerate': 180.6,
                                                            'Maximum framerate': 314.4,
                                                            'Minimum framerate': 124.6},
                                                   '1440': {'0.1% low framerate': 45.8,
                                                            '1% low framerate': 102.3,
                                                            'Average framerate': 133.0,
                                                            'Maximum framerate': 212.5,
                                                            'Minimum framerate': 103.5},
                                                   '4K': {'0.1% low framerate': 43.9,
                                                          '1% low framerate': 62.8,
                                                          'Average framerate': 75.6,
                                                          'Maximum framerate': 113.5,
                                                          'Minimum framerate': 62.6}}}}
"""

# for config in configs.keys():
#     pprint(configs[config])

# game, cpu, graphics = config
# for gpu in configs[config].keys():
#     for resolution in configs[config][gpu].keys():
#         avg_fps = configs[config][gpu][resolution]
#         print([game, graphics, resolution, gpu, avg_fps])


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

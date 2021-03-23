# CSC496 Semester Project - Spring 2021


## Games Benchmarked

### [Tomb Raider (2013)](https://tombraider.fandom.com/wiki/Tomb_Raider_(2013_Game))

This game was chosen for two reasons.  The first being that I already owned it and the second being its built-in benchmarking ability, specifically the ability to provide a configuration file.  Being an older game, I expected it to run well, even on my lower-end graphics card.

Additional sensor data was recording using HWiNFO64 and MSI Afterburner.

 | Date       | Settings                                                               | Notes                                    |
 | ---------- | ---------------------------------------------------------------------- | ---------------------------------------- |
 | 02-16-2021 | [benchmark.ini](./Tomb%20Raider/02_16_2021/benchmark003/benchmark.ini) | Windows Power Mode: **High performance** |
 | 02-16-2021 | [benchmark.ini](./Tomb%20Raider/02_16_2021/benchmark002/benchmark.ini) | Windows Power Mode: **High performance** |
 | 02-16-2021 | [benchmark.ini](./Tomb%20Raider/02_16_2021/benchmark001/benchmark.ini) | Windows Power Mode: **Power saver**      |
 | 02-08-2021 | [benchmark.ini](./Tomb%20Raider/02_08_2021/benchmark001/benchmark.ini) | Windows Power Mode: **High performance** |

### [BioShock Infinite](https://2k.com/en-US/game/bioshock-infinite/)

This game was chosen for similar reasons to Tomb Raider in that I already owned this game and it has a built in benchmark.  I thought it would be interesting to compare two games from the same era and see how far I can push my hardware.

Additional sensor data was recording using HWiNFO64 and MSI Afterburner.

 | Date       | Settings                                                                                               | Notes                                    |
 | ---------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
 | 02-16-2021 | [CustomBenchmarkOptions.ini](./BioShock%20Infinite/02_16_2021/benchmark003/CustomBenchmarkOptions.ini) | Windows Power Mode: **High performance** |
 | 02-16-2021 | [CustomBenchmarkOptions.ini](./BioShock%20Infinite/02_16_2021/benchmark002/CustomBenchmarkOptions.ini) | Windows Power Mode: **High performance** |
 | 02-16-2021 | [CustomBenchmarkOptions.ini](./BioShock%20Infinite/02_16_2021/benchmark001/CustomBenchmarkOptions.ini) | Windows Power Mode: **Power saver**      |
 | 02-08-2021 | [settings.txt](/BioShock%20Infinite/02_08_2021/settings.txt)                                           | Windows Power Mode: **High performance** |

## Observations

### 02-18-2021

![Line Graph TR](./Tomb%20Raider/02_18_2021/plot.png)
![Line Graph BS](./BioShock%20Infinite/02_18_2021/plot.png)

Repeated benchmarks from 02-16-2021 with same settings.  I realized when graphing that the original data was not very consistent and in order to improve consistency, I am now starting and stopping the data logging using specific visual landmarks in each game.

gnuplot file used to generate these graphs can be found [here](./gnu.plot).

A [temporary Python script](#generate-graph-python-script) was used to manipulate the data into a graphable form using: [find](https://en.wikipedia.org/wiki/Find_(Unix)), [awk](https://en.wikipedia.org/wiki/AWK), and [paste](https://en.wikipedia.org/wiki/Paste_(Unix)).

### 02-16-2021

Three benchmarks were run for each games.  The first benchmark was run at 1080p under the Power saver setting in Windows, the second was run at 1080p with the High performance power setting, and the third was run at 720p with the High performance setting.

Tomb raider saw a 2.38% increase in average FPS at 1080p when using the High performance power plan over the Power saver plan.  Decreasing the resolution from 1080p to 720p led to a 49.52% increase in average FPS.

BioShock Infinite saw a 63.56% increase in average FPS at 1080p when using the High performance power plan over the Power saver plan.  Decreasing the resolution from 1080p to 720p led to a 2.60% increase in average FPS.

These two games seem to be optimized quite differently, as their reactions to the change in settings was opposite.  Tomb raider was not affected much by the power plan, but was heavily impacted by the change in resolution.  BioShock on the other hand was heavily affected by the power plan, but no so much the resolution change.

### 02-08-2021

The Tomb Raider benchmark is actually quite short and I opted to not run it in a loop.  In the beginning of the benchmark, the FPS is at its lowest and the CPU is at its hottest.  After a few seconds, the CPU temperature goes down and the FPS goes up and stabilizes.

BioShock showed similar results, however the benchmark is much longer.  It is divided up into multiple "scenes" and each scene is about as long as the entire Tomb Raider benchmark.  In the first scene, we see similar FPS fluctuation to what we saw in the first part of the Tomb Raider benchmark.  After the first scene, the FPS stabilizes quite a bit and the CPU temperature drops to around 50 degrees Celsius.

It seems to me like my CPU cooler takes a few seconds to kick in and during that time, the performance is temporarily limited.  After the cooler starts up, however, performance is slightly increased.

## Module 9 AutoGraph Script (Python)

### Prerequisites

- Python 3.9.0+
- pipenv

### Setup

`cd` into the `AutoGraph` folder and run `$ pipenv install`.  This will create a virtual python environment (venv) and install the necessary dependencies.

### Usage

Once the venv has been created, run `$ pipenv run python graph_benchmarks.py`.  The resulting graphs will be placed in `AutoGraph/images`.

## Cinebench Benchmarking Script (AutoHotKey)

[autohotkey/run_cinebench.ahk](./autohotkey/run_cinebench.ahk) is an AutoHotKey script that invokes both a single-core and multi-score Cinebench run.  Upon launching the script, you will be prompted to locate the Cinebench install directory.  Once the directory has been located, the benchmarks will begin.  The benchmark results are stored in `$CinebenchDir\output.txt`.

## Benchmark Output-Testing Script (Powershell)

[autohotkey/check_results.ps1](./autohotkey/check_results.ps1) is a PowerShell script that will make sure that the output of the AutoHotKey Cinebench script is in the correct format.  To run the script, run the following in a PowerShell terminal:

```PowerShell
> .\check_results.ps1 -FilePath path\to\output.txt
```

## Generate Graph Script (Python)

`$ ./generate_graph.py <folder containing benchmark folders>`

* Looks through the specified folder for `HWiNFO64.CSV` files and plots the FPS columns

Example usage:

Assume `folder1` contains two benchmark folders (`benchmark001`, `benchmark002`), each containing a file called `HWiNFO64.CSV`

If we call `$ ./generate_graph.py folder1`, an `plot.png` will be created inside the folder

On the graph, the legend title for each line will be the name of the folder `HWiNFO64.CSV` was found in (`benchmark001`, `benchmark002`)

## Computer Specifications

* CPU: [AMD Ryzen 5 3600](https://www.amd.com/en/products/cpu/amd-ryzen-5-3600)
* Motherboard: [ASRock Fatal1ty B450 Gaming-ITX/ac](https://www.asrock.com/mb/AMD/Fatal1ty%20B450%20Gaming-ITXac/)
* Memory: [G.SKILL TridentZ 32GB CL16 DDR4 @ 3200 MHz](https://www.gskill.com/product/165/168/1536218236/F4-3200C16D-32GTZKWTrident-ZDDR4-3200MHz-CL16-18-18-38-1.35V32GB-(2x16GB))
* GPU: [Saphire RX 570 Nitro+ 4GB](https://www.sapphiretech.com/en/consumer/nitro-rx-570-4g-g5-oc)
* Storage: [Intel 660p 1TB M.2 SSD](https://www.intel.com/content/www/us/en/products/memory-storage/solid-state-drives/consumer-ssds/6-series/ssd-660p-series/660p-series-1-tb-m-2-80mm-3d2.html)
* Case: [NZXT H1](https://www.nzxt.com/products/h1-matte-white)
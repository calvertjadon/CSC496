# CSC496 Semester Project - Spring 2021

## Games Benchmarked

### [Tomb Raider (2013)](https://tombraider.fandom.com/wiki/Tomb_Raider_(2013_Game))

This game was chosen for two reasons.  The first being that I already owned it and the second being its built-in benchmarking ability, specifically the ability to provide a configuration file.  Being an older game, I expected it to run well, even on my lower-end graphics card.

Additional sensor data was recording using HWiNFO64 and MSI Afterburner.

Settings used in benchmark can be found [here](./Tomb%20Raider/benchmark.ini).

### [BioShock Infinite](https://2k.com/en-US/game/bioshock-infinite/)

This game was chosen for similar reasons to Tomb Raider in that I already owned this game and it has a built in benchmark.  I thought it would be interesting to compare two games from the same era and see how far I can push my hardware.

Additional sensor data was recording using HWiNFO64 and MSI Afterburner.

Settings used:
* Quality: UltraDX11_DDOF
* Aspect ratio: 16:9
* Resolution: 1920x1080

### Observations

The Tomb Raider benchmark is actually quite short and I opted to not run it in a loop.  In the beginning of the benchmark, the FPS is at its lowest and the CPU is at its hottest.  After a few seconds, the CPU temperature goes down and the FPS goes up and stabilizes.

BioShock showed similar results, however the benchmark is much longer.  It is divided up into multiple "scenes" and each scene is about as long as the entire Tomb Raider benchmark.  In the first scene, we see similar FPS fluctuation to what we saw in the first part of the Tomb Raider benchmark.  After the first scene, the FPS stabilizes quite a bit and the CPU temperature drops to around 50 degrees Celsius.

It seems to me like my CPU cooler takes a few seconds to kick in and during that time, the performance is temporarily limited.  After the cooler starts up, however, performance is slightly increased.

## Computer Specifications

* CPU: [AMD Ryzen 5 3600](https://www.amd.com/en/products/cpu/amd-ryzen-5-3600)
* Motherboard: [ASRock Fatal1ty B450 Gaming-ITX/ac](https://www.asrock.com/mb/AMD/Fatal1ty%20B450%20Gaming-ITXac/)
* Memory: [G.SKILL TridentZ 32GB CL16 DDR4 @ 3200 MHz](https://www.gskill.com/product/165/168/1536218236/F4-3200C16D-32GTZKWTrident-ZDDR4-3200MHz-CL16-18-18-38-1.35V32GB-(2x16GB))
* GPU: [Saphire RX 570 Nitro+ 4GB](https://www.sapphiretech.com/en/consumer/nitro-rx-570-4g-g5-oc)
* Storage: [Intel 660p 1TB M.2 SSD](https://www.intel.com/content/www/us/en/products/memory-storage/solid-state-drives/consumer-ssds/6-series/ssd-660p-series/660p-series-1-tb-m-2-80mm-3d2.html)
* Case: [NZXT H1](https://www.nzxt.com/products/h1-matte-white)
# Chippy-8
Chippy-8 is a simple CHIP-8 emulator written in Python. It implements instructions based on the [1997 Cogwood's Technical Reference](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM) specification and uses [PyGame](https://www.pygame.org/docs/) to handle both rendering (binding to SDL) and Keyboard Input. This project was created as a assignment for my programming course at [Matfyz Charles University](https://www.mff.cuni.cz/en) and is not intended for production.

## [Wiki](https://github.com/GasimoCodes/Chippy-8/wiki) 

![2024-02-0918-06-31-ezgif com-video-to-gif-converter](https://github.com/GasimoCodes/Chippy-8/assets/22917863/667d38bb-e925-42dc-846b-3a5824ebb2f9)
![2024-02-0918-11-32-ezgif com-video-to-gif-converter(1)](https://github.com/GasimoCodes/Chippy-8/assets/22917863/30404a55-ccfb-42a6-93de-ea13f2cb38fd)
![2024-02-0918-14-38-ezgif com-video-to-gif-converter](https://github.com/GasimoCodes/Chippy-8/assets/22917863/bf8260a0-1271-49cc-8dbb-ee09dc7ff701)


## Getting Started
### Installation

1. Clone the repository: `git clone https://github.com/GasimoCodes/Chippy-8.git`
2. Download dependencies using: `pip install numpy` or `conda install numpy`

### Emulating
1. Run `PyChip8.py` to run the emulation. It will also generate an config.json file (if not already present).
2. To run a different ROM, make sure the rom is placed in `Roms/`, then edit config.json's `RomName` property with the file name of the new ROM.

## Configuration
Config file config.json is generated automatically upon first launch of the application and contains following fields:

|Parameter  | Description |
|--|--|
| EmulatorDelay  | Time which the emulator sleeps for between CPU cycles (Default 1) |
| ResolutionX | Simulated screen width in pixels of the Chip8 monitor. Do not change if you want to keep the rendering intact. (Default 64)
| ResolutionY | Simulated screen height in pixels of the Chip8 monitor. Do not change if you want to keep the rendering intact. (Default 32) |
| ScalingFactor | Use this to increase the emulator window size (Default 20)
| Debug | True forces the CPU to dump its current OPCODE into console every cycle. (Default false)
| RomName | Name of the rom file located under Roms/ to execute. (Default pong.ch8)


## To-Do's
- Implement sound (**Fx18 - LD ST, Vx**)
- Implement pause (used by **Fx0A - LD Vx, K**)
- Fix PyGame's speed fluctuations with different ScalingFactors.

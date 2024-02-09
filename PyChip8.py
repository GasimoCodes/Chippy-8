import pygame, sys;
from pygame.locals import *;
import Renderer as Rend;
import Input;
import CPU as HW;
import Settings;

# Load settings and init all components
data = Settings.loadSettings();
speed = data["EmulatorDelay"];
rend : Rend.Renderer = Rend.Renderer(data["ResolutionX"], data["ResolutionY"], data["ScalingFactor"]);
keyboard = Input.Keyboard();
ROM : Input.ROM = Input.ROM("Roms/" + data["RomName"]);
CPU : HW.CPU = HW.CPU(rend, keyboard);

CPU.LoadSprites();
CPU.LoadROM(ROM.data);


# Set CPU to debug mode based on config
CPU.debug = data["Debug"];


# Main loop
run = True
while run:
    pygame.time.delay(speed)
    
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            run = False
            
    CPU.Tick();

pygame.quit()





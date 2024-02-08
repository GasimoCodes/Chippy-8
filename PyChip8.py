import pygame, sys;
from pygame.locals import *;

import Renderer as Rend;
import Input;
import CPU as HW;

speed = 1;
rend : Rend.Renderer = Rend.Renderer();
keyboard = Input.Keyboard();
ROM : Input.ROM = Input.ROM("Roms/key_test.ch8");
CPU : HW.CPU = HW.CPU(rend, keyboard);

CPU.LoadSprites();
CPU.LoadROM(ROM.data);

run = True
while run:
    pygame.time.delay(speed)
    
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            run = False
            

    CPU.Tick();

        
pygame.quit()






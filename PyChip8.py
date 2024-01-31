import pygame, sys;
from pygame.locals import *;

import Renderer as Rend;
import Input;
import CPU as HW;


rend : Rend.Renderer = Rend.Renderer();
keyboard = Input.Keyboard();
ROM : Input.ROM = Input.ROM("Roms/Test1.ch8");
CPU : HW.CPU = HW.CPU(rend, keyboard);
a = 0;

CPU.LoadSprites();
CPU.LoadROM(ROM.data);

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

    rend.setPixel(a, a);
    rend.redraw();
    print(a);

        
pygame.quit()






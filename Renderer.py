import pygame, sys;
from pygame.locals import *;

class Renderer:

    
    def __init__(self):
        self.sw, self.sh = 64, 32
        self.scaling_factor = 20
        pygame.init()

        self.black = Color(0, 0, 0)
        self.white = Color(255, 255, 255)        

        self.win = pygame.display.set_mode((self.sw * self.scaling_factor, self.sh * self.scaling_factor))
        self.screen = pygame.Surface((self.sw, self.sh))
        
        pygame.display.set_caption("Chippy8");
        # Set pygame icon as blank
        pygame.display.set_icon(pygame.Surface((1, 1)));
        pass
    

    def redraw(self):
        """Redraws the screen by resizing from the chip8 buffer"""
        
        self.win.blit(pygame.transform.scale(self.screen, self.win.get_rect().size), (0, 0))
        pygame.display.update();
    

    def clear(self):
        """Clears the screen by setting all pixels to black"""
        self.screen.fill(self.black);
        pass


    
    def setPixel(self, x: int, y: int) -> bool:
        """XOR's an pixel at a given x,y position. Returns true if a pixel got 'erased'."""        

        if (x > self.sw):
            x -= self.sw;
        elif (x < 0):
            x += self.sw;


        if (y > self.sh):
            y -= self.sh;
        elif (y < 0):
            y += self.sh;
    
        if self.screen.get_at((x, y)) == self.white:
            self.screen.set_at((x, y), self.black);
            return True;
        
        self.screen.set_at((x, y), self.white);    
        return False;
    

pass





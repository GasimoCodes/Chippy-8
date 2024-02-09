import pygame, sys;
from pygame.locals import *;

class Renderer:
    """Handles rendering pixels on the screen the CHIP-8 way"""
    
    def __init__(self, sw, sh, scaling):
        """Initializes the renderer with a given resolution and scaling factor"""
        self.sw, self.sh = sw, sh
        self.scaling_factor = scaling
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
        # Setting lower or higher scaling causes slowdowns, seems like a pygame issue. TODO: Investigate
        self.win.blit(pygame.transform.scale(self.screen, self.win.get_rect().size), (0, 0))
        pygame.display.update();
    

    def clear(self):
        """Clears the screen by setting all pixels to black"""
        self.screen.fill(self.black);
        pass

    
    def setPixel(self, x: int, y: int) -> bool:
        """XOR's an pixel at a given x,y position. Returns true if a pixel got 'erased'."""        

        # WRAP X VALUE AROUND IF IT GOES OUT OF BOUNDS
        x = x % self.sw;
        y = y % self.sh;
                
        if self.screen.get_at((x, y)) == self.white:
            self.screen.set_at((x, y), self.black);
            return True;
        
        self.screen.set_at((x, y), self.white);    
        return False;
    
pass





import pygame, sys;
from pygame.locals import *;
import numpy;

class Keyboard(object):
    """Represents the Chip8 keyboard. Handles mapping."""
    
    def __init__(self):

        # Map pygame keys to chip8 HEX values
        self.keymap = {
            0x1: K_1,
            0x2: K_2,
            0x3: K_3,
            0xC: K_4,
            0x4: K_q,
            0x5: K_w,
            0x6: K_e,
            0xD: K_r,
            0x7: K_a,
            0x8: K_s,
            0x9: K_d,
            0xE: K_f,
            0xA: K_z,
            0x0: K_x,
            0xB: K_c,
            0xF: K_v
        }
        
        pass
    
    def isKeyDown(self, key: numpy.uint8) -> bool:
        """Returns true if the key is down"""
        return pygame.key.get_pressed()[self.keymap[key]];


    pass


class ROM(object):
    """Represents a chip8 ROM"""
    
    def __init__(self, path: str):
        self.path = path;
        self.data = [];
        self.load();
        pass
    
    
    def load(self):
        """Loads the ROM into memory"""
        with open(self.path, "rb") as f:
            byte = f.read(1);
            while byte:
                # Convert byte to int and append to data
                self.data.append(int.from_bytes(byte, byteorder='big', signed=False));
                byte = f.read(1);
                pass
            pass
        pass
    pass



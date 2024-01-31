import pygame, sys;
from pygame.locals import *;

class Keyboard(object):
    
    
    def __init__(self):

        # Map pygame keys to chip8 HEX values
        self.keymap = {
            K_1: 0x1,
            K_2: 0x2,
            K_3: 0x3,
            K_4: 0xC,
            K_q: 0x4,
            K_w: 0x5,
            K_e: 0x6,
            K_r: 0xD,
            K_a: 0x7,
            K_s: 0x8,
            K_d: 0x9,
            K_f: 0xE,
            K_z: 0xA,
            K_x: 0x0,
            K_c: 0xB,
            K_v: 0xF
        }
        
        pass
    
    def isKeyDown(self, key: int) -> bool:
        """Returns true if the key is down"""
        return pygame.key.get_pressed()[key];


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
                self.data.append(byte);
                byte = f.read(1);
                pass
            pass
        pass
    pass



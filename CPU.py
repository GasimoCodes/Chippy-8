from ast import Num
import Renderer as Rend;
import Input;
import Executer;
import numpy;

class CPU(object):

    def __init__(self, renderer : Rend.Renderer, keyboard : Input.Keyboard):
        # EXT
        self.renderer = renderer;
        self.keyboard = keyboard;
        self.executer = Executer.Executer(self);
        
        # MEM (in bytes) using numpy uint8 array
        self.memory = numpy.zeros(4096, dtype=numpy.uint8);
        self.registers = numpy.zeros(16, dtype=numpy.uint8);
        
        # STACC
        self.stack = [0] * 16;
        self.stackPointer = 0;
        
        # PC
        self.programCounter = 0x200;
        self.indexRegister = 0;
        
        # TIMERS
        self.delayTimer = 0;
        
        self.paused = False;
        pass


    def LoadSprites(self):
        """Loads the 'sprite font' into memory"""
        
        # Praised be Cowgod.
        self.sprites = [
        0xF0, 0x90, 0x90, 0x90, 0xF0, # 0
        0x20, 0x60, 0x20, 0x20, 0x70, # 1
        0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2
        0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3
        0x90, 0x90, 0xF0, 0x10, 0x10, # 4
        0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5
        0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6
        0xF0, 0x10, 0x20, 0x40, 0x40, # 7
        0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8
        0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9
        0xF0, 0x90, 0xF0, 0x90, 0x90, # A
        0xE0, 0x90, 0xE0, 0x90, 0xE0, # B
        0xF0, 0x80, 0x80, 0x80, 0xF0, # C
        0xE0, 0x90, 0x90, 0x90, 0xE0, # D
        0xF0, 0x80, 0xF0, 0x80, 0xF0, # E
        0xF0, 0x80, 0xF0, 0x80, 0x80  # F
        ];

        # Copy sprites into interpreter memory starting at 0x000
        self.memory[0:80] = self.sprites;
    
    def LoadROM(self, ROM):
        """Loads the ROM into memory"""

        print(ROM);
        

        # At 0x200, like lord intended.
        self.memory[(0x200) : (int(0x200) + len(ROM))] = ROM;
        pass


    def Tick(self):
        """Executes a single cycle"""
        # To-do: Implement a way to control how many instructions are executed/tick.

        # Fetch opcode. Each instruction is 2 bytes long. Shift the first byte left by 8 bits, 
        # then OR it with the second byte and voila.
        opcode = (self.memory[self.programCounter] << 8) | self.memory[self.programCounter + 1];

                
        self.executer.Execute(opcode);
        self.updateTimers();
        self.renderer.redraw();
    
        pass


    def updateTimers(self):
        """Updates the delay timer"""
        if (self.delayTimer > 0):
            self.delayTimer -= 1;

        pass






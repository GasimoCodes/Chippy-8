import numpy;
import random;

class Executer(object):

    def __init__(self, cpu):
        self.cpu = cpu;
        pass

    def Execute(self, opcode):
        """Executes an opcode"""
        
        # Only way to do this in an performant and readable way in python is 
        # a monster of a Match().
        # MAY LORD HAVE MERCY ON US.

        #print("Executing: " + hex(opcode));
        self.cpu.programCounter += 2;

        # Commonly used OPCODE parts shorthands:
        # nibble 2
        x = (opcode & 0x0F00) >> 8;
        # nibble 3
        y = (opcode & 0x00F0) >> 4;
        


        # Based on nibble 1
        match (opcode & 0xF000):
            case 0x0000:
                match (opcode):
                    case 0x00E0:
                        # CLEAR SCREEN
                        self.cpu.renderer.clear();
                        pass
                    case 0x00EE:
                        # RETURN FROM SUBROUTINE
                        self.cpu.programCounter = self.cpu.stack.pop();
                        pass
                pass;
            
            case 0x1000:
                # JUMP TO ADDRESS
                self.cpu.programCounter = opcode & 0x0FFF;
                pass;
            case 0x2000:
                # CALL SUBROUTINE
                self.cpu.stack.append(self.cpu.programCounter);
                self.cpu.programCounter = opcode & 0x0FFF;
                pass;
            case 0x3000:
                # SKIP NEXT INSTRUCTION IF VX == NN
                if self.cpu.registers[x] == (opcode & 0x00FF):
                    self.cpu.programCounter += 2;
                pass;
            case 0x4000:
                # SKIP NEXT INSTRUCTION IF VX != NN
                if self.cpu.registers[x] != (opcode & 0x00FF):  
                    self.cpu.programCounter += 2;
                pass;
            case 0x5000:
                # SKIP NEXT INSTRUCTION IF VX == VY
                if self.cpu.registers[x] == self.cpu.registers[y]:
                    self.cpu.programCounter += 2;
                pass;
            case 0x6000:
                # LOAD VX TO NN
                self.cpu.registers[x] = (opcode & 0x00FF);
                pass;
            case 0x7000:
                # ADD NN TO VX
                self.cpu.registers[x] += (opcode & 0x00FF);
                pass;
            case 0x8000:
                # MATCH LAST NIBBLE
                match (opcode & 0xF):
                    case 0x0:
                        # LOAD VY INTO VX
                        self.cpu.registers[x] = self.cpu.registers[y];
                        pass;
                    case 0x1:
                        # OR VY INTO VX
                        self.cpu.registers[x] |= self.cpu.registers[y];
                        pass;
                    case 0x2:
                        # AND VY INTO VX
                        self.cpu.registers[x] &= self.cpu.registers[y];
                        pass;
                    case 0x3:
                        # XOR VY INTO VX
                        self.cpu.registers[x] ^= self.cpu.registers[y];
                        pass;
                    case 0x4:
                        # ADD VY TO VX

                        # If this doesnt work then numpy did not overflow properly.
                        result = int(self.cpu.registers[x]) + int(self.cpu.registers[y]);
                        self.cpu.registers[x] = numpy.uint8(result);
                        
                        # Set carry flag
                        if result > 255:
                            self.cpu.registers[0xF] = 1;
                        else:
                            self.cpu.registers[0xF] = 0;    
                        
                        pass;
                    case 0x5:
                        # SUBTRACT VY FROM VX
                        # TODO: FIX
                        
                        isNotBorrow = 0;
                        if numpy.uint8(self.cpu.registers[x]) >= numpy.uint8(self.cpu.registers[y]):
                            isNotBorrow = 1;
                        
                        self.cpu.registers[x] = numpy.uint8(numpy.uint8(self.cpu.registers[x]) - numpy.uint8(self.cpu.registers[y]));
                        self.cpu.registers[0xF] = isNotBorrow;

                        pass;
                    case 0x6:
                        # SHIFT VX RIGHT
                        flag = self.cpu.registers[x] & 0x1;
                        self.cpu.registers[x] >>= 1;
                        self.cpu.registers[0xF] = flag;
                        pass;
                    case 0x7:
                        # SUBTRACT VX FROM VY
                        borrow = 0;                        

                        if self.cpu.registers[y] >= self.cpu.registers[x]:
                            borrow = 1;
                        
                        self.cpu.registers[x] = self.cpu.registers[y] - self.cpu.registers[x];
                        
                        self.cpu.registers[0xF] = borrow;                        
                        
                        pass;
                    case 0xE:
                        # SHIFT VX LEFT
                        # TODO: FIX CARRY FLAG if broken
                        borrow = (self.cpu.registers[x]) >> 7;                        
                        self.cpu.registers[x] = (self.cpu.registers[x] << 1);
                        self.cpu.registers[0xF] = borrow;
                        pass;
                pass

            case 0x9000:
                # SKIP NEXT INSTRUCTION IF VX != VY
                if self.cpu.registers[x] != self.cpu.registers[y]:
                        self.cpu.programCounter += 2;
                pass;
            case 0xA000:
                # LOAD I WITH ADDRESS
                self.cpu.indexRegister = opcode & 0x0FFF;
                pass;
            case 0xB000:
                # JUMP TO ADDRESS + V0
                self.cpu.programCounter = (opcode & 0x0FFF) + self.cpu.registers[0];
                pass;
            case 0xC000:
                # LOAD VX WITH RANDOM NUMBER AND NN
                self.cpu.registers[x] = random.randint(0, 255) & (opcode & 0x00FF);
                pass;
            case 0xD000:
                # DRAW SPRITE
                self.DrawSprite(x, y, opcode);
                pass;
            case 0xE000:
                match (opcode & 0xFF):
                    case 0x9E:
                        # SKIP NEXT INSTRUCTION IF KEY VX IS PRESSED
                        if self.cpu.keyboard.isKeyDown(self.cpu.registers[x]):
                            self.cpu.programCounter += 2;
                        pass;
                    case 0xA1:
                        # SKIP NEXT INSTRUCTION IF KEY VX IS NOT PRESSED
                        if not self.cpu.keyboard.isKeyDown(self.cpu.registers[x]):
                            self.cpu.programCounter += 2;                    
                        pass;
                pass;
            
            case 0xF000:
                match (opcode & 0xFF):
                    case 0x07:
                        # LOAD VX WITH DELAY TIMER
                        self.cpu.registers[x] = self.cpu.delayTimer;
                        pass;
                    case 0x0A:
                        # WAIT FOR KEY PRESS AND LOAD VX
                        # TODO: Implement this
                        raise Exception("NOT IMPLEMENTED: " + opcode);
                        pass;
                    case 0x15:
                        # LOAD DELAY TIMER WITH VX
                        self.cpu.delayTimer = self.cpu.registers[x];  
                        pass;
                    case 0x18:
                        # TODO: Implement sound timer
                        pass;
                    case 0x1E:
                        # ADD VX TO I
                        self.cpu.indexRegister += self.cpu.registers[x];
                        pass;
                    case 0x29:
                        # LOAD I WITH SPRITE LOCATION FOR VX
                        self.cpu.indexRegister = self.cpu.registers[x] * 5;
                        pass;
                    case 0x33:
                        # STORE DIGITS 100,10,1 OF VX IN I
                        
                        # 100s digit
                        self.cpu.memory[self.cpu.indexRegister] = self.cpu.registers[x] // 100;
                        # 10s digit
                        self.cpu.memory[self.cpu.indexRegister + 1] = (self.cpu.registers[x] // 10) % 10;
                        # 1s digit
                        self.cpu.memory[self.cpu.indexRegister + 2] = self.cpu.registers[x] % 10;
                        
                        pass;
                    case 0x55:
                        # STORE V0 TO VX IN MEMORY STARTING AT I
                        
                        for i in range(x + 1):
                            self.cpu.memory[self.cpu.indexRegister + i] = self.cpu.registers[i];
                        
                        pass;
                    case 0x65:
                        # LOAD V0 TO VX FROM MEMORY STARTING AT I
                        for i in range(x + 1):
                            self.cpu.registers[i] = self.cpu.memory[self.cpu.indexRegister + i];

                        pass;
                
                pass;

            case _:
                raise Exception("NO OP: " + opcode);
                

        
        pass


    def DrawSprite(self, x,y, opcode):
        """Draws a sprite"""

        width = 8;
        height = (opcode & 0xF);
        self.cpu.registers[0xF] = 0;

        for row in range(height): 
            # Lets hope this copies and not modifies the original.
            sprite = self.cpu.memory[self.cpu.indexRegister + row];

            for col in range(width):
                # If the pixel is white, draw it (Or undraw it).
                if ((sprite & 0x80) > 0):
                    # If pixel was erased (returns 1), set VF to 1
                    if (self.cpu.renderer.setPixel(self.cpu.registers[x] + col, self.cpu.registers[y] + row) == 1):
                        self.cpu.registers[0xF] = 1;

                # Shift the sprite left to get the next pixel.
                sprite <<= 1;

        pass














    pass





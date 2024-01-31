class Executer(object):

    def __init__(self, cpu):
        self.cpu = cpu;
        pass

    def Execute(self, opcode):
        """Executes an opcode"""
        
        # Only way to do this in an performant and readable way in python is 
        # a monster of a Match().
        # MAY LORD HAVE MERCY ON US.

        print("Executing: " + hex(opcode));
        self.cpu.programCounter += 2;

        # Commonly used OPCODE parts shorthands:
        # Take bottom nibble
        x = (opcode & 0x0F00) >> 8;
        # Take top nibble
        y = (opcode & 0x0F00) >> 8;
        

                

        
        pass


















    pass





import pygame, sys;
from pygame.locals import *;





pygame.init();
DISPLAYSURF = pygame.display.set_mode((400, 300));
pygame.display.set_caption('CHIP-8');

a = 0;
print(sys.getsizeof(a));

while True: # main game loop

    a += 1;

    DISPLAYSURF.set_at((a, a), Color(255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
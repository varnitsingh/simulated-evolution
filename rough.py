import pygame
pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
pygame.display.set_caption("this")
run = True
clock=pygame.time.Clock()
win = pygame.display.set_mode((600,600))
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(textsurface,(0,0))
    pygame.display.update()
    pygame.quit()
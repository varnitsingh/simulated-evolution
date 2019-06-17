from creature import *
pygame.display.set_caption("Simulated Evolution")

#####   Main loop ######
def main():
    global food_count
    global run
    global maxCreatures
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        tempCountLifeCycle = 1
        keys = pygame.key.get_pressed()#for starting the fooking program
        while (tempCountLifeCycle <= max_life_cycle) and keys[pygame.K_SPACE] :  #decides life cycles
            print(maxCreatures)
            win.fill(black)
            tempCountLifeCycle += 1    #updating loop
            tempCountCreatures = 0
            creatureInitialPosCount = 0
            CreatureObject = []
            distributeFood(food_count)
            keyForCreature = pygame.key.get_pressed()
            creatureIncreased=0
            while tempCountCreatures < maxCreatures and keyForCreature[pygame.K_SPACE]:
                #### assign creatures initial  position  ####
                if creatureInitialPosCount < 10:
                    CreatureObject.append(creature(0-1,9-creatureInitialPosCount))   #will assign value from (0,9) to (0,0)
                elif creatureInitialPosCount < 20:
                    CreatureObject.append(creature(-10+creatureInitialPosCount,0-1))   #will assign value from (1,0) to (9,0)
                elif creatureInitialPosCount < 30:
                    CreatureObject.append(creature(9+1,-20+creatureInitialPosCount))  #will assign value from (9,1) to (9,9)
                elif creatureInitialPosCount < 40:
                    CreatureObject.append(creature(39-creatureInitialPosCount,9+1))
                elif creatureInitialPosCount == 40:
                        creatureInitialPosCount = -1
                CreatureObject[tempCountCreatures].assign(creatureInitialPosCount)
                creatureInitialPosCount += 1
                #### assignment over   ####
                redrawGameWindow()
                CreatureObject[tempCountCreatures].calculateDrawCreature()                      #draws the initial pos of the creatures
                CreatureObject[tempCountCreatures].moveCreature()
                creatureIncreased += CreatureObject[tempCountCreatures].reproduction
                tempCountCreatures += 1  # updating loop
            maxCreatures += creatureIncreased
            drawGraph(tempCountLifeCycle)
            pygame.display.update()

    pygame.quit()
main()
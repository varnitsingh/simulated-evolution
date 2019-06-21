from creature import *
pygame.display.set_caption("Simulated Evolution")

#####   Main loop ######
def main():
    global food_count
    global run
    global maxCreatures
    global countLifeForGraph
    global average
    global max_life_cycle
    global maxMoveCount
    while run:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        tempCountLifeCycle = 1
        count = 1
        keys = pygame.key.get_pressed()#for starting the program
        drawDefaultScreen()
        while (keys[pygame.K_DOWN]) and count==1:
            win.fill(black)
            pygame.draw.circle(win,red,(100 + 5,100 + 5),6)
            message("Food Eaten by creature",120,100,white)
            pygame.draw.rect(win,blue,(70+ 5,120+ 5,40,40))
            message("Virtual depiction of Creature",120,135,white)
            pygame.display.update()
            count = 0
        while (tempCountLifeCycle <= max_life_cycle) and (keys[pygame.K_SPACE]):
            #decides life cycles
            win.fill(black,(0,0,600,600))
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
                CreatureObject[tempCountCreatures].assign(creatureInitialPosCount)
                if creatureInitialPosCount == 39:
                    creatureInitialPosCount = -1
                creatureInitialPosCount += 1
                #### assignment over   ####
                redrawGameWindow()
                CreatureObject[tempCountCreatures].calculateDrawCreature()                      #draws the initial pos of the creatures
                CreatureObject[tempCountCreatures].moveCreature()
                creatureIncreased += CreatureObject[tempCountCreatures].reproduction
                tempCountCreatures += 1  # updating loop
                ### creature count loop over ###
            maxCreatures += creatureIncreased
            countLifeForGraph+=1
            drawGraph(countLifeForGraph,maxCreatures)
            average=(average+maxCreatures)/2
            averagestr = "Average No of Creatures = " + str(average)
            creaturestr = "Creatues in this cycle = " + str(maxCreatures)
            win.fill(black,(700,100,500,100))
            message(averagestr,700,100,red)
            message(creaturestr,700,130,red)
            pygame.display.update()
            ###  life cycle loop over   ###
        pygame.display.update()
    pygame.quit()
    ###  run loop over   ###
##### End of MAIN loop  ######
main()
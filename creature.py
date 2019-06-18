from functions import *
class creature:
    def __init__(self,x,y):
        self.xInitial=x
        self.yInitial=y
        self.food_eaten=0
        self.move_count= 1
        self.vel = 0.1
        self.xCur = x
        self.yCur = y
        self.xNex = x
        self.yNex = y
        self.reproduction=0
        self.color = blue

    def assign(self,initialPosCount):
        if initialPosCount < 10 :
            self.xCur = 0
        elif initialPosCount < 20:
            self.yCur = 0
        elif initialPosCount < 30:
            self.xCur=9
        elif initialPosCount < 40:
            self.yCur=9
        self.xNex=self.xCur
        self.yNex=self.yCur

    def drawCreatures(self):
        drawLandscape()
        drawFood()
        pygame.draw.rect(win, self.color, (self.xCur * 50 + 50 + 5, self.yCur * 50 + 50 + 5, 40, 40))

    def calculateDrawCreature(self,flag=-1):      #asking for flag. If flag =1, move the creature
        if flag == -1:
            redrawGameWindow()
            pygame.draw.rect(win,self.color,(self.xInitial*50 + 50 + 5,self.yInitial*50 + 50 + 5,40,40))
        elif flag == 0:
            while self.xCur >= self.xNex:
                self.xCur -= self.vel
                self.drawCreatures()
        elif flag == 1:
            while self.yCur >= self.yNex:
                self.yCur -= self.vel
                self.drawCreatures()
        elif flag == 2:
            while self.yCur <= self.yNex:
                self.yCur += self.vel
                self.drawCreatures()
        elif flag == 3:
            while self.xCur <= self.xNex:
                self.xCur += self.vel
                self.drawCreatures()
        self.xCur=self.xNex
        self.yCur=self.yNex
        pygame.display.update()


    def moveCreature(self):
        global maxMoveCount
        while(self.move_count < maxMoveCount):
            direction = random.randint(0,3)
            if direction == 0 and self.xCur > 0:
                self.xNex -= 1
                self.move_count += 1  # updating current loop
                self.calculateDrawCreature(direction)
            elif direction == 1 and self.yCur > 0:
                self.yNex -= 1
                self.move_count += 1  # updating current loop
                self.calculateDrawCreature(direction)
            elif direction == 2 and self.yCur < 9:
                self.yNex += 1
                self.move_count += 1  # updating current loop
                self.calculateDrawCreature(direction)
            elif direction == 3 and self.xCur < 9:
                self.xNex += 1
                self.move_count += 1  # updating current loop
                self.calculateDrawCreature(direction)
            if landscape_area[self.xNex][self.yNex] == 1:      #checking if the creature landed on food
                self.food_eaten += 1
                landscape_area[self.xNex][self.yNex] = 0
            if self.food_eaten == 2:
                self.move_count=maxMoveCount
        drawLandscape()
        drawFood()
        if self.food_eaten == 0:        #deciding whether the creature reproduced or not
            self.reproduction = -1
        elif self.food_eaten >= 2:
            self.reproduction = 1
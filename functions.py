from gl_variable import *

def distributeFood(foodAmount):
    foodDistributed = 0
    for i in range (10):
        for j in range (10):
            landscape_area[i][j]=0
    while foodDistributed < foodAmount:
        x=random.randint(0,9)
        y=random.randint(0,9)
        if (landscape_area[x][y] == 0):
            landscape_area[x][y] = 1
            foodDistributed +=1

def drawFood():
    for i in range(10):
        for j in range (10):
            if landscape_area[i][j] == 1:
                pygame.draw.circle(win,red,((i*50)+50+25,(j*50)+50+25),6)


def drawLandscape():
    pygame.draw.rect(win,white,(50,50,500,500))


def redrawGameWindow():
    drawLandscape()
    drawFood()
    pygame.display.update()

def drawGraph(tempLifeCycle):
    pygame.draw.line(win,green,(700,500),(1100,500))
    pygame.draw.line(win,green,(700,500),(700,300))
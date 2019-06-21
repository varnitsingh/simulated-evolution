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

def message(text,x,y,color):
    screenText = font.render(text,True,color)
    win.blit(screenText,(x,y))

def drawGraph(xgraph,ygraph):
    global countLifeForGraph
    global maxCreatures
    global previousYpos
    global previousXpos
    pygame.draw.line(win,green,(700,500),(1150,500))
    pygame.draw.line(win,green,(700,500),(700,250))
    message("Life Cycle ---->",850,550,white)
    message("Number of Creatures ^",650,200,white)
    i=800
    while i<=1100:
        pygame.draw.line(win,green,(i,490),(i,510))
        value = (i-700)/4
        value=int(value)
        message(str(value),i-10,520,green)
        i+=100
    i=300
    while i<=450:
        pygame.draw.line(win,green,(690,i),(710,i))
        value = (500-i)/5
        value = int(value)
        message(str(value),660,i-10,green)
        i+=50
    pygame.draw.line(win,green,(previousXpos,previousYpos),((xgraph*4)+700,500-(ygraph*5)))
    previousXpos = (xgraph*4)+700
    previousYpos = 500-(ygraph*5)

def drawDefaultScreen():
    message("Space - Run simulation            Down Arrow Key - Instructions",300,620,white)
    i=0
    while (i<=15):
        pygame.draw.line(win, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(0,620 + i),(295,620 + i))
        pygame.draw.line(win, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (905, 620 + i),(1200, 620 + i))
        pygame.draw.line(win, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (529, 620 + i),(595 , 620 + i))
        i+= 3
    i=0
    while i<=10:
        pygame.draw.line(win,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(0,641 + i),(1200,641 + i))
        i+=3
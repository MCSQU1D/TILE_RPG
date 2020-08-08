# import the pygame module, so you can use it
import pygame
from time import sleep
import random
import os
from multiprocessing import Process

os.system('clear')


display_width = 720
display_height = 720
global island
island = 0
global mx
global my
mx = 0
my = 0
buttonsDict = {}





# initialize the pygame module
pygame.init()

running = True

# load and set the logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("RPG - Work in progress")


### SREEN AND CLOCK ###
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

### SCENES ###


Map_Work_1 = pygame.image.load("Map_Work_1.png")
Map_Park = pygame.image.load("Map_Park.png")
Map_Work_2 = pygame.image.load("Map_Work_2.png")
Map_Food = pygame.image.load("Map_Food.png")
Map_Home = pygame.image.load("Map_Home.png")
Map_Bank = pygame.image.load("Map_Bank.png")
Map_Uni = pygame.image.load("Map_Uni.png")
Map_Shop_1 = pygame.image.load("Map_Shop_1.png")
Map_Shop_2 = pygame.image.load("Map_Shop_2.png")


#Start
#Opening
#Map1
#Map2
#Map3
#Map4
#Map5
#Map6
#Map7
#Map8
#map9
#End








###   VARIABLES   START  ###


ButtonLocationPrintHolder = "placeholder"
scene = "Start"
playerx = 360
playery = 360
current_map = 0
global maps
maps = ["Start", "Map_Work_1", "Map_Park", "Map_Work_2", "Map_Food", "Map_Home", "Map_Bank", "Map_Uni", "Map_Shop_1", "Map_Shop_2"]


global player_speed
player_speed = 4
inventory = []

global can_up
global can_down
global can_left
global can_right
can_up = True
can_down = True
can_left = True
can_right = True


global health
global Time_Actual
global Days
global stamina
global max_stamina

health = 100
time = "0:00"
Time_Actual = 0
Days = 0
stamina = 0
max_stamina = 100





# all positions: lower are subtracted 4, upper are added 4 to compensate for player size
obstacle_finder = [
[1, 1, 1, 1]
]

Map_Work_1_Obstacles = [
[1, 1, 1, 1]
]

Map_Park_Obstacles = [
[1, 1, 1, 1]
]

Map_Work_2_Obstacles = [
[1, 1, 1, 1]
]

Map_Food_Obstacles = [
[1, 1, 1, 1]
]

Map_Home_Obstacles = [
[472, 460, 724, 724],
[244, 480, 412, 724],
[244, 480, 412, 724],
[84, 600, 412, 724],
[-4, 248, 308, 264],
[300, 236, 324, 264],
[396, 236, 420, 264],
[412, 248, 724, 264]
]

Map_Bank_Obstacles = [
[-4, 248, 248, 264],
[248, -4, 264, 248],
[240, 240, 264, 264],
[-4, 460, 256, 724],
[492, 12, 724, 708]
]

Map_Uni_Obstacles = [
[1, 1, 1, 1]
]

Map_Shop_1_Obstacles = [
[1, 1, 1, 1]
]

Map_Shop_2_Obstacles = [
[1, 1, 1, 1]
]


###   VARIABLES   END   ###










###   PRINTING   START   ###

def PrintMap_Work_1_Below():
    screen.fill((255,255,255))  # (R, G, B)
    screen.blit(Map_Work_1, (0, 0))

def PrintMap_Park_Below():
    screen.fill((255,255,255))  # (R, G, B)
    screen.blit(Map_Park, (0, 0))

def PrintMap_Work_2_Below():
    screen.fill((255,255,255))  # (R, G, B)
    screen.blit(Map_Work_2, (0, 0))

def PrintMap_Food_Below():
    screen.fill((255,255,255))  # (R, G, B)
    screen.blit(Map_Food, (0, 0))

def PrintMap_Home_Below():
    screen.fill((255,255,255))  # (R, G, B)
    screen.blit(Map_Home, (0, 0))

def PrintMap_Bank_Below():
    screen.fill((255,255,255))  # (R, G, B)
    screen.blit(Map_Bank, (0, 0))

def PrintMap_Uni_Below():
    screen.fill((255,255,255))  # (R, G, B)
    screen.blit(Map_Uni, (0, 0))

def PrintMap_Shop_1_Below():
    screen.fill((255,255,255))  # (R, G, B)
    screen.blit(Map_Shop_1, (0, 0))

def PrintMap_Shop_2_Below():
    screen.fill((255,255,255))  # (R, G, B)
    screen.blit(Map_Shop_2, (0, 0))





def PrintMap_Work_1_Above():
    screen.fill((255,255,255))  # (R, G, B)
    #screen.blit(Map_Work_1, (0, 0))

def PrintMap_Park_Above():
    screen.fill((255,255,255))  # (R, G, B)
    #screen.blit(Map_Park, (0, 0))

def PrintMap_Work_2_Above():
    screen.fill((255,255,255))  # (R, G, B)
    #screen.blit(Map_Work_2, (0, 0))

def PrintMap_Food_Above():
    screen.fill((255,255,255))  # (R, G, B)
    #screen.blit(Map_Food, (0, 0))

def PrintMap_Home_Above():
    screen.fill((255,255,255))  # (R, G, B)
    #screen.blit(Map_Home, (0, 0))

def PrintMap_Bank_Above():
    screen.fill((255,255,255))  # (R, G, B)
    #screen.blit(Map_Bank, (0, 0))

def PrintMap_Uni_Above():
    screen.fill((255,255,255))  # (R, G, B)
    #screen.blit(Map_Uni, (0, 0))

def PrintMap_Shop_1_Above():
    screen.fill((255,255,255))  # (R, G, B)
    #screen.blit(Map_Shop_1, (0, 0))

def PrintMap_Shop_2_Above():
    screen.fill((255,255,255))  # (R, G, B)
    #screen.blit(Map_Shop_2, (0, 0))





def PrintStart():
    screen.fill((205,0,0))  # (R, G, B)
    text = "RPG"
    font = pygame.font.Font('RUSKOF.ttf', 400) #Font size
    LineHolder = text
    text = font.render(text, True, (255, 217, 0)) #Font colour
    linewidth = text.get_width()
    textRect = text.get_rect()
    textRect.center = ((display_width/2), 150)
    screen.blit(text, textRect)
    text2 = "game by SAM MCKID, developed with PYTHON and PYGAME"
    font = pygame.font.Font('RUSKOF.ttf', 20) #Font size
    LineHolder = text2
    text2 = font.render(text2, True, (0, 0, 0)) #Font colour
    linewidth = text2.get_width()
    textRect = text2.get_rect()
    textRect.center = ((display_width/2), 735)
    screen.blit(text2, textRect)






def PrintStartButtons(buttontext1, buttontext2, buttontext3):
    global buttonsDict


    #buttonsDict = {(X, -X, Y, -Y) : operation/number}
    buttonsDict = {
        (214, 506, 400, 480) : "button1",
        (213, 506, 500, 580) : "button2",
        (239, 482, 600, 690) : "button3",
    }


    font = pygame.font.Font('RUSKOF.ttf', 160) #Font size
    LineHolder = buttontext1
    buttontext1 = font.render(buttontext1, True, (255, 217, 0)) #Font colour
    linewidth = buttontext1.get_width()
    textRect = buttontext1.get_rect()
    textRect.center = ((display_width/2), 440)
    screen.blit(buttontext1, textRect)

    font = pygame.font.Font('RUSKOF.ttf', 160) #Font size
    LineHolder = buttontext2
    buttontext2 = font.render(buttontext2, True, (255, 217, 0)) #Font colour
    linewidth = buttontext2.get_width()
    textRect = buttontext2.get_rect()
    textRect.center = ((display_width/2), 540)
    screen.blit(buttontext2, textRect)

    font = pygame.font.Font('RUSKOF.ttf', 160) #Font size
    LineHolder = buttontext3
    buttontext3 = font.render(buttontext3, True, (255, 217, 0)) #Font colour
    linewidth = buttontext2.get_width()
    textRect = buttontext3.get_rect()
    textRect.center = ((display_width/2), 640)
    screen.blit(buttontext3, textRect)


def PrintStats(health, time, stamina):
    font = pygame.font.Font('RUSKOF.ttf', 30) #Font size
    health = "Health: " + str(health)
    time = "Time: " + str(time)
    stamina = round(stamina, 1)
    stamina = "Stamina: " + str(stamina)


    health = font.render(health, True, (255, 0, 0)) #Font colour
    linewidth = health.get_width()
    textRect = health.get_rect()
    textRect.center = ((display_width/2), 30)
    screen.blit(health, textRect)


    time = font.render(time, True, (255, 255, 255)) #Font colour
    linewidth = time.get_width()
    textRect = time.get_rect()
    textRect.center = ((display_width/2)+200, 30)
    screen.blit(time, textRect)


    stamina = font.render(stamina, True, (3, 157, 252)) #Font colour
    linewidth = stamina.get_width()
    textRect = stamina.get_rect()
    textRect.center = ((display_width/2)-200, 30)
    screen.blit(stamina, textRect)



def PrintPlayer(x, y):
    s = pygame.Surface((16,16)) # Size of Shadow
    s.set_alpha(180) # Alpha of Shadow
    s.fill((115,55,0)) # Color of Shadow
    screen.blit(s, ((x-4), (y-4))) # Position of Shadow
    SkateBoard(x, y)
    pygame.draw.rect(screen, (230, 110, 1), (x-8, y-8, 16, 16)) # Location, location, size, size


def SkateBoard(x_coord, y_coord):
    global playerx
    global playery
    global stamina
    playerx = x_coord
    playery = y_coord
    key = pygame.key.get_pressed()

    if (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]) and "skakeboard" in inventory:

        CheckObstactles()
        Movement(playerx, playery)
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            pygame.draw.rect(screen, (3, 252, 11), (playerx-20, playery-4, 24, 8))
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            pygame.draw.rect(screen, (3, 252, 11), (playerx-4, playery-4, 24, 8))
        elif key[pygame.K_UP] or key[pygame.K_w]:
            pygame.draw.rect(screen, (3, 252, 11), (playerx-4, playery-4, 8, 24))
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            pygame.draw.rect(screen, (3, 252, 11), (playerx-4, playery-20, 8, 24))

    elif (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]) and "skakeboard" not in inventory and stamina > 1:
        CheckObstactles()
        Movement(playerx, playery)
        stamina -= 1
        stamina = round(stamina, 1)




def CheckObstactles():
    global can_up
    global can_down
    global can_left
    global can_right

    can_up = True
    can_down = True
    can_left = True
    can_right = True

    obstacle_finder = [[1,1,1,1]]
    if scene == "Map_Work_1":
        obstacle_finder = Map_Work_1_Obstacles
    if scene == "Map_Park":
        obstacle_finder = Map_Park_Obstacles
    if scene == "Map_Work_2":
        obstacle_finder = Map_Work_2_Obstacles
    if scene == "Map_Food":
        obstacle_finder = Map_Food_Obstacles
    if scene == "Map_Home":
        obstacle_finder = Map_Home_Obstacles
    if scene == "Map_Bank":
        obstacle_finder = Map_Bank_Obstacles
    if scene == "Map_Uni":
        obstacle_finder = Map_Uni_Obstacles
    if scene == "Map_Shop_1":
        obstacle_finder = Map_Shop_1_Obstacles
    if scene == "Map_Shop_2":
        obstacle_finder = Map_Shop_2_Obstacles


    for i in obstacle_finder:
        #print(i)
        #print("next")
        obstacle_xlow = i[0]
        obstacle_ylow = i[1]
        obstacle_xhigh = i[2]
        obstacle_yhigh = i[3]
        if (playerx + 4) == obstacle_xlow and playery >= obstacle_ylow and playery <= obstacle_yhigh:
            can_right = False
            print('rightobstance')
        if (playerx - 4) == obstacle_xhigh and playery >= obstacle_ylow and playery <= obstacle_yhigh:
            can_left = False
            print('leftobstance')
        if (playery + 4) == obstacle_ylow and playerx >= obstacle_xlow and playerx <= obstacle_xhigh:
            can_down = False
            print('downobstance')
        if (playery - 4) == obstacle_yhigh and playerx >= obstacle_xlow and playerx <= obstacle_xhigh:
            can_up = False
            print('upobstance')




def Movement(x_coord, y_coord):
    global movement_checker
    global playerx
    global playery
    playerx = x_coord
    playery = y_coord

    player_speed = 4
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] or key[pygame.K_w]:
        if can_up == True:
            playery -= player_speed

    if key[pygame.K_DOWN] or key[pygame.K_s]:
        if can_down == True:
            playery += player_speed

    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        if can_right == True:
            playerx += player_speed

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        if can_left == True:
            playerx -= player_speed

    if playerx != x_coord or playery != y_coord:
        movement_checker = True











###   PRINTING   END   ###


# main loop
while running == True:
    movement_checker = False




    mx, my = pygame.mouse.get_pos()
    #print("X: " + str(mx) + ", Y: " + str(my))

    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
        # prints everything going on
        #print(event)
    for ButtonLocations in buttonsDict:
        xlimithigh = ButtonLocations[0]
        xlimitlow = ButtonLocations[1]
        ylimithigh = ButtonLocations[2]
        ylimitlow = ButtonLocations[3]

        if mx > xlimithigh and mx < xlimitlow and my > ylimithigh and my < ylimitlow:
            ButtonLocationFinder = buttonsDict[ButtonLocations]


    if event.type == pygame.MOUSEBUTTONDOWN:       #From Alexander Henry Photios
        #print("x: " + str(mx) + "  y: " + str(my))
        for ButtonLocations in buttonsDict:
            xlimithigh = ButtonLocations[0]
            xlimitlow = ButtonLocations[1]
            ylimithigh = ButtonLocations[2]
            ylimitlow = ButtonLocations[3]

            if mx > xlimithigh and mx < xlimitlow and my > ylimithigh and my < ylimitlow:
                ButtonLocationPrintHolder = buttonsDict[ButtonLocations]
                #print(ButtonLocationPrintHolder)






#Movement between map
    if playerx >= 704:
        playerx = 0
        if current_map != 9 and current_map != 6 and current_map != 3:
            current_map += 1
    if playerx <= -4:
        playerx = 700
        if current_map != 1 and current_map != 4 and current_map != 7:
            current_map -= 1
    if playery >= 704:
        playery = 0
        if current_map != 7 and current_map != 8 and current_map != 9:
            current_map += 3
    if playery <= -4:
        playery = 700
        if current_map != 1 and current_map != 2 and current_map != 3:
            current_map -= 3
    scene = maps[current_map]




    if scene == "Start":
        PrintStart()


        PrintStartButtons("PLAY", "LOAD", "QUIT")
        if ButtonLocationPrintHolder == "button1":
            something = "happens"
            scene = "Map_Home"
            current_map = 5
            ButtonLocationPrintHolder = "holder"
        if ButtonLocationPrintHolder == "button2":
            something = "happens"
            #scene = "Load_Screen"
            ButtonLocationPrintHolder = "holder"
        if ButtonLocationPrintHolder == "button3":
            running = False
            ButtonLocationPrintHolder = "holder"

    if scene != "Start":
        Current_Scene_Finder = str(scene) + ".png"
        Current_Scene = pygame.image.load(Current_Scene_Finder)
        screen.blit(Current_Scene, (0, 0))


    if scene != "Start":
        CheckObstactles()
        Movement(playerx, playery)
        PrintPlayer(playerx,playery)
        Current_Scene_Above_Finder = str(scene) + "_Above.png"
        Current_Scene_Above = pygame.image.load(Current_Scene_Above_Finder)
        screen.blit(Current_Scene_Above, (0, 0))
        PrintStats(health, time, stamina)




    #print("Current: " + str(current_map))
    #print("Map: " + str(maps[current_map]))
    #print("x: " + str(playerx))
    #print("y: " + str(playery))
    """
    if Time_Actual >= 96:
        Time_Actual = 0
        Days += 1
    Time_Actual_holder = Time_Actual
    if "." in str(Time_Actual/4):
        split_time = time.split(":")
        while Time_Actual_holder >= 4:
            Time_Actual_holder -= 4
        split_time[1] = str(Time_Actual_holder*15)
        if split_time[1] == "0":
            split_time[1] = "00"
        if split_time[1] >= "60":
            split_time[1] = "00"
            split_time[0] = (Time_Actual/4)
        print(split_time)
        time = split_time[0] + ":" + split_time[1]

    Time_Actual += 1
    """

    if stamina < max_stamina:
        stamina += 0.1
        stamina = round(stamina, 1)
        if movement_checker == False:
            stamina += 0.4
        if stamina > (max_stamina-0.5):
            stamina = max_stamina
    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)



pygame.quit()

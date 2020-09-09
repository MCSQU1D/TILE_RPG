# import the pygame module, so you can use it
import pygame
from time import sleep
import random
import os
import math
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

Map_Work_1 = pygame.image.load(os.path.join('backgrounds', 'Map_Work_1.png'))
Map_Park = pygame.image.load(os.path.join('backgrounds', 'Map_Park.png'))
Map_Work_2 = pygame.image.load(os.path.join('backgrounds', 'Map_Work_2.png'))
Map_Food = pygame.image.load(os.path.join('backgrounds', 'Map_Food.png'))
Map_Home = pygame.image.load(os.path.join('backgrounds', 'Map_Home.png'))
Map_Bank = pygame.image.load(os.path.join('backgrounds', 'Map_Bank.png'))
Map_Uni = pygame.image.load(os.path.join('backgrounds', 'Map_Uni.png'))
Map_Shop_1 = pygame.image.load(os.path.join('backgrounds', 'Map_Shop_1.png'))
Map_Shop_2 = pygame.image.load(os.path.join('backgrounds', 'Map_Shop_2.png'))
pygame.mixer.music.load("Music.mp3")



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
global inventory
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
global Time_Taken
global Time_Dict
global current_stamina
global max_stamina
global max_stamina
global Stats_Dict
global money
global Bank_account
global Mobster_Dict

Bank_account = 100
health = 100
money = 1000000
Time_Taken = 0
Time_Dict = {
    "day" : 0,
    "hour" : 12,
}
Stats_Dict = {
    "intelligence" : 1000,
    "strength" : 1000,
    "charm" : 1000,
    "karma" : 0
}
current_stamina = 50000
max_stamina = 100
Mobster_Dict = {
    "x" : 360,
    "y" : 360,
    "health" : 100,
    "damage" : 20
}

Sales_Job = "None"
Shipping_Job = "None"
Accounting_Job = "None"


#["Job", Int_req, Str_req, Chm_req, Pay]
global Workplace_List
global Sales_Dict
global Accounting_Dict
global Shipping_Dict


Sales_Dict = [
["Sales", 40, 0, 40, 40],
["Head of Floor", 75, 0, 60, 75],
["Head of Sales", 100, 0, 75, 100]
]
Accounting_Dict = [
["Accountant", 80, 0, 0, 50],
["Head of Accounting", 100, 0, 0, 100]
]
Shipping_Dict = [
["Stacker", 0, 25, 0, 20],
["Forklift Driver", 25, 50, 0, 35],
["Head of Shipping", 30, 75, 0, 60]
]

# all positions: lower are subtracted 4, upper are added 4 to compensate for player size
# [x-4,y-4,x+4,y+4]
obstacle_finder = [
[1, 1, 1, 1]
]
Map_Work_1_Obstacles = [
[-4, -4, 724, 4], # Top boader
[-4, -4, 4, 724], # Left boarder
[-4, -4, 248, 724],
[272, -4, 724, 248],
[452, 456, 476, 480],
[452, 472, 468, 724],
[468, 456, 724, 472]
]
Map_Park_Obstacles = [
[-4, -4, 724, 4], # Top boader
[-4, 456, 308, 472],
[300, 456, 324, 484],
[396, 456, 420, 484],
[716, -4, 724, 248],
[412, 456, 724, 472]
]
Map_Work_2_Obstacles = [
[-4, -4, 724, 4], # Top boarder
[716, -4, 724, 724], # Right boarder
[-4, 456, 248, 472],
[240, 456, 264, 480],
[248, 472, 264, 724],
[-4, -4, 724, 248],
[476, -4, 724, 724]
]
Map_Food_Obstacles = [
[-4, -4, 248, 4], #Building in scene above (Work_1)
[-4, -4, 4, 724], # Left boarder
[452, -4, 468, 248],
[452, 240, 476, 264],
[468, 248, 724, 264],
[-4, -4, 220, 724]
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
[716, -4, 724, 724], # Right boarder
[-4, 248, 248, 264],
[248, -4, 264, 248],
[240, 240, 264, 264],
[-4, 460, 256, 724],
[476, 716, 724, 724],
[492, 12, 724, 708]
]
Map_Uni_Obstacles = [
[-4, -4, 4, 724], #left boarder
[-4, 716, 724, 724], # Bottom boarder
[1, 1, 1, 1]
]
Map_Shop_1_Obstacles = [
[-4, 716, 724, 724], # Bottom boarder
[1, 1, 1, 1]
]
Map_Shop_2_Obstacles = [
[716, -4, 724, 724], # Right boarder
[-4, 716, 724, 724], # Bottom boarder
[1, 1, 1, 1]
]
# for horizontal enterances from above, ylow has 8 subtracted
# for horizontal enterances from below, yhigh has 8 added
# for verticle enterances from left, xlow has 8 subtracted
# for verticle enterances from right, xhigh has 8 added
#[xlow-8, ylow-8, xhigh+8, yhigh+8, scene]
Map_Work_1_Entrances = [
[244, 400, 264, 448, "Work_1_Sales"],
[244, 604, 264, 696, "Work_1_Shipping"],
[532, 244, 604, 264, "Work_1_Accounting"]
]
Map_Park_Entrances = [
[-1, -1, -1, -1, "nothing"]
]
Map_Work_2_Entrances = [
[-1, -1, -1, -1, "nothing"]
]
Map_Food_Entrances = [
[208, 132, 244, 232, "Big_Red"]
]
Map_Home_Entrances = [
[512, 456, 568, 468, "Small_Apartment"],
[176, 580, 224, 604, "House"]
]
Map_Bank_Entrances = [
[480, 216, 496, 280, "Bank"]
]
Map_Uni_Entrances = [
[-1, -1, -1, -1, "nothing"]
]
Map_Shop_1_Entrances = [
[-1, -1, -1, -1, "nothing"]
]
Map_Shop_2_Entrances = [
[-1, -1, -1, -1, "nothing"]
]

###   VARIABLES   END   ###



###   PRINTING   START   ###
def PrintStartButtons(buttontext1, buttontext2, buttontext3):
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
    font = pygame.font.Font('RUSKOF_LIGHT.ttf', 30) #Font size
    text2 = font.render(text2, True, (0, 0, 0)) #Font colour
    linewidth = text2.get_width()
    textRect = text2.get_rect()
    textRect.center = ((display_width/2), 700)
    screen.blit(text2, textRect)
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
    linewidth = buttontext3.get_width()
    textRect = buttontext3.get_rect()
    textRect.center = ((display_width/2), 640)
    screen.blit(buttontext3, textRect)
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
def PrintMap():
    if "Map" in scene:
        Current_Scene_Finder = str(scene) + ".png"
        Current_Scene = pygame.image.load(os.path.join('backgrounds', Current_Scene_Finder))
        screen.blit(Current_Scene, (0, 0))
        CheckObstactles()
        Movement(playerx, playery)
        PrintPlayer(playerx,playery)
        if event.type == pygame.MOUSEBUTTONDOWN:
            GunFired(mx, my, playerx, playery)
        Mobster()
        Current_Scene_Above_Finder = str(scene) + "_Above.png"
        Current_Scene_Above = pygame.image.load(os.path.join('backgrounds', Current_Scene_Above_Finder))
        screen.blit(Current_Scene_Above, (0, 0))
        PrintStats(health, Time_Dict, current_stamina)
        CheckEntrances(playerx, playery)

def PrintBuilding(exit_text, action_1_text, action_2_text, action_3_text, action_4_text, exit_coords, building):
    #print the buttons
    #print the background
    #add exit function
    #screen.fill((255,255,255))  # (R, G, B)
    global scene
    global buttonsDict
    global playerx
    global playery
    playerx = exit_coords[0]
    playery = exit_coords[1]
    scene = building
    Building_Background = pygame.image.load(os.path.join('backgrounds', (building + ".png")))
    screen.blit(Building_Background, (0, 0))
    s = pygame.Surface((720,720)) # Size of Shadow
    s.set_alpha(10) # Alpha of Shadow
    s.fill((150,150,150)) # Color of Shadow
    screen.blit(s, (0, 0))


    buttonsDict = {
        (50, 250, 550, 650) : "button1",  #Exit
        (425, 625, 150, 250) : "button2",
        (425, 625, 250, 350) : "button3",
        (425, 625, 350, 450) : "button4",
        (425, 625, 450, 550) : "button5",
    }

    printlist = [
    [exit_text, 150, 600],
    [action_1_text, 525, 200],
    [action_2_text, 525, 300],
    [action_3_text, 525, 400],
    [action_4_text, 525, 500]
    ]
    font = pygame.font.Font('American_Captain.ttf', 50) #Font size

    for i in printlist:
        if i[0] != "":
            h = i[0]
            h = font.render(h, True, (0, 0, 0)) #Font colour
            linewidth = h.get_width()
            textRect = h.get_rect()
            textRect.center = (i[1], i[2])
            screen.blit(h, textRect)


def BuildlingPrinter():
    if entrance_scene == "Small_Apartment":
        PrintBuilding("EXIT", "SLEEP", "SAVE", "", "SETTINGS", (536, 440), "Small_Apartment")
    if entrance_scene == "House" and "House Keys" in inventory:
        PrintBuilding("EXIT", "SLEEP", "SAVE", "", "SETTINGS", (204, 544), "House")
    if entrance_scene == "Bank":
        PrintBuilding("EXIT", "DEPOSIT", "WITHDRAWL", "BUY HOUSE", "", (460, 248), "Bank")
    if entrance_scene == "Work_1_Sales":
        PrintBuilding("EXIT", "WORK", "PROMOTION", "", "APPLY", (288, 424), "PlayerWork_Sales")
    if entrance_scene == "Work_1_Shipping":
        PrintBuilding("EXIT", "WORK", "PROMOTION", "", "APPLY", (288, 652), "PlayerWork_Shipping")
    if entrance_scene == "Work_1_Accounting":
        PrintBuilding("EXIT", "WORK", "PROMOTION", "", "APPLY", (568, 288), "PlayerWork_Accounting")

def Work(Work_Location):
    global Workplace_List
    global scene
    global ButtonLocationPrintHolder
    global money

    global Sales_Dict
    global Accounting_Dict
    global Shipping_Dict
    global Sales_Job
    global Accounting_Job
    global Shipping_Job




    print(Work_Location)
    if Work_Location == "PlayerWork_Sales":
        PrintBuilding("EXIT", "WORK", "PROMOTION", "", "APPLY", (288, 424), "PlayerWork_Sales")
        Work_Place = "Sales"
        Work_Dict = Sales_Dict
        Job = Sales_Job
    if Work_Location == "PlayerWork_Accounting":
        PrintBuilding("EXIT", "WORK", "PROMOTION", "", "APPLY", (568, 288), "PlayerWork_Accounting")
        Work_Place = "Accounting"
        Work_Dict = Accounting_Dict
        Job = Accounting_Job
    if Work_Location == "PlayerWork_Shipping":
        PrintBuilding("EXIT", "WORK", "PROMOTION", "", "APPLY", (288, 652), "PlayerWork_Shipping")
        Work_Place = "Shipping"
        Work_Dict = Shipping_Dict
        Job = Shipping_Job

    #EXIT
    if ButtonLocationPrintHolder == "button1":
        ButtonLocationPrintHolder = "holder"
        scene = maps[current_map]

    #WORK
    if ButtonLocationPrintHolder == "button2":
        ButtonLocationPrintHolder = "Holder"
        if (Time_Dict["hour"] + 6) < 24:
            if Job == "None":
                PrintGeneral("Apply for a Job")
                print("Apply for a Job")
            else:
                for i in Work_Dict:
                    if Job == i[0]:
                        PrintGeneral("Earnt: " + str(i[4]))
                        print("Earnt: " + str(i[4]))
                        money += i[4]
                        Time_Dict["hour"] += 6
                        scene = maps[current_map]
        else:
            PrintGeneral("Work Closed: Too Late")

    #PROMOTION
    if ButtonLocationPrintHolder == "button3":
        ButtonLocationPrintHolder = "Holder"
        a = 0
        for i in Work_Dict:
            a += 1
            print(a)
            print(i)
            if i[0] == Job:
                holda = Work_Dict[(a-1)]
                if Stats_Dict["intelligence"] >= holda[1]:
                    PrintGeneral("Promoted")
                    print("Promoted")
                else:
                    PrintGeneral("Rejected")
                    print("Rejected")
            elif Job == "None":
                PrintGeneral("Must have job here")
                print("Must have job here")
    #APPLY
    if ButtonLocationPrintHolder == "button5":
        ButtonLocationPrintHolder = "Holder"
        if Job == "None":
            for i in Work_Dict:
                if Stats_Dict["intelligence"] >= i[1] and Stats_Dict["strength"] >= i[2] and Stats_Dict["charm"] >= i[3]:
                    Job = i[0]
                    if "Sales" in Work_Location:
                        Sales_Job = Job
                    if "Accounting" in Work_Location:
                        Accounting_Job = Job
                    if "Shipping" in Work_Location:
                        Shipping_Job = Job
                    PrintGeneral("Hired")
                    print("Hired")
                else:
                    PrintGeneral("Rejected")
        else:
            PrintGeneral("Already have a Job here")
            print("Already have a Job here")

    print(Job)

    Work_Place = "holder"
    Work_Dict = "holder"



def PrintStats(health, time, current_stamina):
    font = pygame.font.Font('American_Captain.ttf', 30) #Font size
    health = "Health: " + str(health)
    time = "DAY:" + (str(Time_Dict['day']) + "–" + str(Time_Dict['hour'])) + ":00"
    current_stamina = int(current_stamina)
    current_stamina = "Stamina: " + str(current_stamina)


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


    current_stamina = font.render(current_stamina, True, (3, 157, 252)) #Font colour
    linewidth = current_stamina.get_width()
    textRect = current_stamina.get_rect()
    textRect.center = ((display_width/2)-200, 30)
    screen.blit(current_stamina, textRect)


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
    global current_stamina
    playerx = x_coord
    playery = y_coord
    key = pygame.key.get_pressed()

    if (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]) and "skateboard" in inventory and current_stamina > 1:

        CheckObstactles()
        #CheckEntrances(playerx, playery)
        Movement(playerx, playery)
        current_stamina -= 0.5
        current_stamina = round(current_stamina, 1)
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            pygame.draw.rect(screen, (3, 252, 11), (playerx-16, playery-4, 24, 8))
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            pygame.draw.rect(screen, (3, 252, 11), (playerx-8, playery-4, 24, 8))
        elif key[pygame.K_UP] or key[pygame.K_w]:
            pygame.draw.rect(screen, (3, 252, 11), (playerx-4, playery-8, 8, 24))
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            pygame.draw.rect(screen, (3, 252, 11), (playerx-4, playery-16, 8, 24))
        else:
            pygame.draw.rect(screen, (3, 252, 11), (playerx-12, playery-4, 24, 8))

    elif (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]) and "skateboard" not in inventory and current_stamina > 1:
        CheckObstactles()
        #CheckEntrances(playerx, playery)
        Movement(playerx, playery)
        current_stamina -= 1
        current_stamina = round(current_stamina, 1)





def CheckEntrances(playerx, playery):
    global scene
    global entrance_scene
    entrance_finder = [[-1,-1,-1,-1, "nothing"]]
    if scene == "Map_Work_1":
        entrance_finder = Map_Work_1_Entrances
    if scene == "Map_Park":
        entrance_finder = Map_Park_Entrances
    if scene == "Map_Work_2":
        entrance_finder = Map_Work_2_Entrances
    if scene == "Map_Food":
        entrance_finder = Map_Food_Entrances
    if scene == "Map_Home":
        entrance_finder = Map_Home_Entrances
    if scene == "Map_Bank":
        entrance_finder = Map_Bank_Entrances
    if scene == "Map_Uni":
        entrance_finder = Map_Uni_Entrances
    if scene == "Map_Shop_1":
        entrance_finder = Map_Shop_1_Entrances
    if scene == "Map_Shop_2":
        entrance_finder = Map_Shop_2_Entrances

    for i in entrance_finder:
        #print(i)
        #print("next")
        entrance_xlow = i[0]
        entrance_ylow = i[1]
        entrance_xhigh = i[2]
        entrance_yhigh = i[3]
        entrance_scene = i[4]
        #print(entrance_xlow,entrance_xhigh,entrance_ylow,entrance_yhigh)
        #print(playerx, playery)
        if entrance_xlow <= playerx <= entrance_xhigh and entrance_ylow <= playery <= entrance_yhigh:
            #print('Entered: ' + entrance_scene)
            BuildlingPrinter()

            #print(scene)

def PrintGeneral(text):
    font = pygame.font.Font('American_Captain.ttf', 50) #Font size
    text = font.render(text, True, (0, 0, 0)) #Font colour
    linewidth = text.get_width()
    textRect = text.get_rect()
    textRect.center = ((display_width/2), (display_height/2))
    screen.blit(text, textRect)


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
            #print('rightobstance')
        if (playerx - 4) == obstacle_xhigh and playery >= obstacle_ylow and playery <= obstacle_yhigh:
            can_left = False
            #print('leftobstance')
        if (playery + 4) == obstacle_ylow and playerx >= obstacle_xlow and playerx <= obstacle_xhigh:
            can_down = False
            #print('downobstance')
        if (playery - 4) == obstacle_yhigh and playerx >= obstacle_xlow and playerx <= obstacle_xhigh:
            can_up = False
            #print('upobstance')


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



def PrintInventory():
    s = pygame.Surface((720,720)) # Size of Shadow
    s.set_alpha(120) # Alpha of Shadow
    s.fill((255,255,255)) # Color of Shadow
    screen.blit(s, (0, 0))
    font = pygame.font.Font('American_Captain.ttf', 50) #Font size

    title_printer = "inventory"
    title_printer = font.render(title_printer, True, (0, 0, 0)) #Font colour
    linewidth = title_printer.get_width()
    textRect = title_printer.get_rect()
    textRect.center = ((display_width/4), (120))
    screen.blit(title_printer, textRect)

    title_printer = "Stats"
    title_printer = font.render(title_printer, True, (0, 0, 0)) #Font colour
    linewidth = title_printer.get_width()
    textRect = title_printer.get_rect()
    textRect.center = (((3*display_width)/4), (120))
    screen.blit(title_printer, textRect)

    font = pygame.font.Font('American_Captain.ttf', 30) #Font size
    a = 0
    b = 0
    for i in inventory:
        a += 1
        i = font.render(i, True, (0, 0, 0)) #Font colour
        linewidth = i.get_width()
        textRect = i.get_rect()
        textRect.center = ((display_width/4), (120+40*a))
        screen.blit(i, textRect)


    Stats_Dict_Printer = Stats_Dict
    Stats_Dict_Printer["max stamina"] = max_stamina
    Stats_Dict_Printer["health"] = health
    Stats_Dict_Printer["money"] = money
    Stats_Dict_Printer["bank account"] = Bank_account

    for j in Stats_Dict_Printer:
        b += 1
        j = str(j) + ": " + str(Stats_Dict[j])
        j = font.render(j, True, (0, 0, 0)) #Font colour
        linewidth = j.get_width()
        textRect = j.get_rect()
        textRect.center = ((3*display_width/4), (120+40*b))
        screen.blit(j, textRect)



def GunFired(mx, my, playerx, playery):
    bulletx = (playerx+mx)/2
    bullety = (playery+my)/2
    pygame.draw.rect(screen, (0, 0, 0), (bulletx, bullety, 8, 8)) # Location, location, size, size
    bulletx = (bulletx+mx)/2
    bullety = (bullety+my)/2
    pygame.draw.rect(screen, (0, 0, 0), (bulletx, bullety, 8, 8)) # Location, location, size, size
    bulletx = mx
    bullety = my
    pygame.draw.rect(screen, (0, 0, 0), (bulletx, bullety, 8, 8)) # Location, location, size, size

def Mobster():
    global playerx
    global playery
    x = Mobster_Dict["x"]
    y = Mobster_Dict["y"]

    s = pygame.Surface((16,16)) # Size of Shadow
    s.set_alpha(180) # Alpha of Shadow
    s.fill((0,0,0)) # Color of Shadow
    screen.blit(s, ((x+4), (y+4))) # Position of Shadow
    pygame.draw.rect(screen, (45, 45, 45), (x, y, 16, 16)) # Location, location, size, size

    mobster_movement = random.randrange(0, 32)
    player_distance = math.sqrt((playerx - x)**2 + (playery - y)**2)
    if player_distance <= 100:
        if playerx > x:
            Mobster_Dict["x"] += 4
        if playery > y:
            Mobster_Dict["y"] += 4
        if playerx < x:
            Mobster_Dict["x"] -= 4
        if playery < y:
            Mobster_Dict["y"] -= 4

    Mobster_right = True
    Mobster_left = True
    Mobster_down = True
    Mobster_up = True

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
        obstacle_xlow = i[0]
        obstacle_ylow = i[1]
        obstacle_xhigh = i[2]
        obstacle_yhigh = i[3]
        if (x + 4) == obstacle_xlow and y >= obstacle_ylow and y <= obstacle_yhigh:
            Mobster_right = False
        if (x - 4) == obstacle_xhigh and y >= obstacle_ylow and y <= obstacle_yhigh:
            Mobster_left = False
        if (y + 4) == obstacle_ylow and x >= obstacle_xlow and x <= obstacle_xhigh:
            Mobster_down = False
        if (y - 4) == obstacle_yhigh and x >= obstacle_xlow and x <= obstacle_xhigh:
            Mobster_up = False

    if mobster_movement == 2 and Mobster_right == True:
        Mobster_Dict["x"] += 4
    if mobster_movement == 4 and Mobster_left == True:
        Mobster_Dict["x"] -= 4
    if mobster_movement == 8 and Mobster_down == True:
        Mobster_Dict["y"] += 4
    if mobster_movement == 16 and Mobster_up == True:
        Mobster_Dict["y"] -= 4



###   PRINTING   END   ###



# main loop
while running == True:
    movement_checker = False
    #print("start of checker")
    #print(scene)
    #print("Current: " + str(current_map))
    #print("Map: " + str(maps[current_map]))
    #print("x: " + str(mx))
    #print("y: " + str(my))


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
    if playerx >= 716:
        playerx = 0
        if current_map != 9 and current_map != 6 and current_map != 3:
            current_map += 1
    if playerx <= -4:
        playerx = 712
        if current_map != 1 and current_map != 4 and current_map != 7:
            current_map -= 1
    if playery >= 716:
        playery = 0
        if current_map != 7 and current_map != 8 and current_map != 9:
            current_map += 3
    if playery <= -4:
        playery = 712
        if current_map != 1 and current_map != 2 and current_map != 3:
            current_map -= 3
    if "Map" in scene:
        scene = maps[current_map]


    if scene == "Start":
        PrintStartButtons("PLAY", "LOAD", "QUIT")
        if ButtonLocationPrintHolder == "button1":
            ButtonLocationPrintHolder = "holder"
            something = "happens"
            scene = "Map_Home"
            current_map = 5
            #pygame.mixer.music.play(0)
        if ButtonLocationPrintHolder == "button2":
            ButtonLocationPrintHolder = "holder"
            something = "happens"
            #scene = "Load_Screen"
        if ButtonLocationPrintHolder == "button3":
            ButtonLocationPrintHolder = "holder"
            running = False

    PrintMap()

    if scene == "Small_Apartment":
        #if "skateboard" not in inventory:
            #inventory.append("skateboard")
        if ButtonLocationPrintHolder == "button1":
            ButtonLocationPrintHolder = "holder"
            scene = maps[current_map]
            print("EXIT")
        if ButtonLocationPrintHolder == "button2":
            ButtonLocationPrintHolder = "holder"
            scene = maps[current_map]
            Time_Dict["day"] += 1
            Time_Dict["hour"] = 6

    if scene == "Bank":
        if ButtonLocationPrintHolder == "button1":
            ButtonLocationPrintHolder = "holder"
            scene = maps[current_map]
        if ButtonLocationPrintHolder == "button2":
            ButtonLocationPrintHolder = "holder"
            if money >= 100:
                Bank_account += 100
                money -= 100
        if ButtonLocationPrintHolder == "button3":
            ButtonLocationPrintHolder = "holder"
            if Bank_account >= 100:
                money += 100
                Bank_account -= 100
        if ButtonLocationPrintHolder == "button4" and "House Keys" not in inventory:
            ButtonLocationPrintHolder = "holder"
            if money >= 100000:
                money -= 100000
                inventory.append("House Keys")


    key = pygame.key.get_pressed()
    if key[pygame.K_i] and "Map" in scene:
        PrintInventory()
    if key[pygame.K_ESCAPE]:
        scene = maps[current_map]


    if "PlayerWork" in scene:
        Work(scene)



    if Time_Dict["hour"] >= 24:
        Time_Dict["day"] += 1
        Time_Dict["hour"] = 0



    if current_stamina < max_stamina:
        current_stamina += 0.1
        current_stamina = round(current_stamina, 1)
        if movement_checker == False:
            current_stamina += 0.4
        if current_stamina > (max_stamina-0.5):
            current_stamina = max_stamina

    #VARIABLE RESET
    ButtonLocationPrintHolder = "holder"
    Bank_account += Bank_account*(0.0001388888889) #Equals 5% per 0.6 seconds or something like that
    Bank_account = round(Bank_account, 2)  #round it so it looks nice

    #print(pygame.mixer.music.get_pos())
    if pygame.mixer.music.get_pos() >= 6000:
        pygame.mixer.music.play()
    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)



pygame.quit()

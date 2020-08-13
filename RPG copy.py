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


# all positions: lower are subtracted 4, upper are added 4 to compensate for player size



###   VARIABLES   END   ###









###   PRINTING   START   ###


def PrintBuilding(exit_text, action_1_text, action_2_text, action_3_text, action_4_text, exit_coords, building):
    #print the buttons
    #print the background
    #add exit function
    #screen.fill((255,255,255))  # (R, G, B)

    global buttonsDict
    scene = building
    Building_Background = pygame.image.load(building + ".png")
    screen.blit(Building_Background, (0, 0))

    #Center coords:
    # exit: 150, 600
    # button1: 525, 200
    # button2: 525, 300
    # button3: 525, 400
    # button4: 525, 500


    playerx = ((exit_coords[0] + exit_coords[1])/2)
    playery = ((exit_coords[2] + exit_coords[3])/2)

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








###   PRINTING   END   ###


# main loop
while running == True:


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
    print("x: " + str(mx), "y: " + str(my))


    PrintBuilding("EXIT", "SLEEP", "DIE", "SAVE", "HIGH", (400, 300, 200, 100), "Building")


    #VARIABLE RESET

    ButtonLocationPrintHolder = "holder"

    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)



pygame.quit()

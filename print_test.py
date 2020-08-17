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



###   PRINTING   END   ###

health = 100


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

    font = pygame.font.Font('American_Captain.ttf', 60) #Font size

    buttontext3 = "Health"
    buttontext3 = font.render(buttontext3, True, (255, 255, 255)) #Font colour
    linewidth = buttontext3.get_width()
    textRect = buttontext3.get_rect()
    textRect.center = (300, 640)
    screen.blit(buttontext3, textRect)

    pygame.draw.rect(screen, (255, 0, 0), (300, 640, 200, 200))

    #VARIABLE RESET

    ButtonLocationPrintHolder = "holder"

    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)



pygame.quit()

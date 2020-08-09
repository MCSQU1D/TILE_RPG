buttonsDict = {
    (214, 506, 400, 480) : "button1",  #Exit
    (213, 506, 500, 580) : "button2",
    (239, 482, 600, 690) : "button3",
    (240, 482, 600, 690) : "button4",
    (241, 482, 600, 690) : "button5",
}
exit_text = "Exit"
action_1_text = "Sleep"
action_2_text = "Some"
action_3_text = "Thing"
action_4_text = "hehe"


printlist = [
[exit_text, 400, 320],
[action_1_text, 400, 320],
[action_2_text, 400, 320],
[action_3_text, 400, 320],
[action_4_text, 400, 320]
]


for i in buttonsDict:
    print("average_x: " + str((i[0] + i[1])/2) + ", average_y: " + str((i[2] + i[3])/2))



font = pygame.font.Font('RUSKOF.ttf', 160) #Font size

for i in printlist:
    i = font.render(i, True, (255, 217, 0)) #Font colour
    linewidth = i.get_width()
    textRect = i.get_rect()
    textRect.center = ((display_width/2), 640)
    screen.blit(i, textRect)

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

variables = [exit_text, action_1_text, action_2_text, action_3_text, action_4_text]

printlist_correct = [
[exit_text, 400, 320],
[action_1_text, 400, 320],
[action_2_text, 400, 320],
[action_3_text, 400, 320],
[action_4_text, 400, 320]
]

printlist = []
a = 0

for i in buttonsDict:
    printlist_holder = []
    #print("average_x: " + str((i[0] + i[1])/2) + ", average_y: " + str((i[2] + i[3])/2))
    printlist_holder.append(variables[a])
    printlist_holder.append((i[0] + i[1])/2)
    printlist_holder.append((i[2] + i[3])/2)
    printlist.append(printlist_holder)
    a += 1

print(printlist)

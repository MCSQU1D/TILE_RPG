playerx = 40
playery = 40
#obstacle = [xlow,xhigh,ylow,yhigh]
playerx = 80
playery = 80
tree1 = [300, 400, 100, 120]
tree2 = [400, 420, 110, 150]

Obstacles = [tree1, tree2]
print(Obstacles)

while True:
    playerx = input("x: ")
    playery = input("y: ")
    for i in Obstacles:
        obstacle_xlow = i[0]
        obstacle_xhigh = i[1]
        obstacle_ylow = i[2]
        obstacle_yhigh = i[3]
        if (playerx + 4) == obstacle_xlow and playery >= obstacle_ylow and playery <= obstacle_yhigh:
            can_left = False
        if (playerx - 4) == obstacle_xhigh and playery >= obstacle_ylow and playery <= obstacle_yhigh:
            can_right = False
        if (playery + 4) == obstacle_ylow and playerx >= obstacle_xlow and playerx <= obstacle_xhigh:
            can_down = False
        if (playery - 4) == obstacle_yhigh and playery >= obstacle_xlow and playerx <= obstacle_xhigh:
            can_up = False
        

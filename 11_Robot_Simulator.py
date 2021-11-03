def robot(movement, coor, orientation):
    compass = ["north", "east", "south", "west"]
    orientation = compass.index(orientation)
    for i in movement:
        if i == "A":
            if orientation == 0:
                coor[1] += 1
            elif orientation == 1:
                coor[0] += 1
            elif orientation == 2:
                coor[1] -= 1
            elif orientation == 3:
                coor[0] -= 1
        if i == "R":
            orientation = (orientation + 1) % 4
        if i == "L":
            orientation = (orientation - 1) % 4
    print (coor, "facing", compass[orientation])
 
 
movement = "RAALAL"
coor = [7, 3]
orientation = "north"
 
robot(movement, coor, orientation)


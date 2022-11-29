import turtle, time

'''
Name: Julius Broomfield
Class: CSc 2510
Assignment: Towers of Hanoi
'''

wn = turtle.Screen()
wn.title("Towers of Hanoi - Julius Broomfield")
wn.bgcolor("White")
turtle.tracer(0, 0)

GROUND = ((-375, -200),(375, -200))
FIRST_ROD = (-200, - 200)
SECOND_ROD = (0, -200)
THIRD_ROD = (200, -200)
#Initial Game State
pen = turtle.Turtle()
positions = []
pen.speed("fastest")
pen.penup()
pen.pensize(15)

while True:
    #Drawing Rods
    def set_rods():
        pen.clear()
        pen.color("black")
        pen.pensize(15)
        pen.penup()
        pen.setposition(THIRD_ROD)
        pen.pendown()
        pen.goto(200, 150)

        pen.penup()
        pen.setposition(SECOND_ROD)
        pen.pendown()
        pen.goto(0, 150)

        pen.penup()
        pen.setposition(FIRST_ROD)
        pen.pendown()
        pen.goto(-200, 150)

        pen.penup()
        pen.setposition(GROUND[0])
        pen.pendown()
        pen.goto(GROUND[1])

    #Creates Disks
    def place_disk(disk, index, rod):
        pen.penup()
        pen.color(disk[1])
        pen.pensize(50)
        pen.setposition(rod[0] - disk[0], rod[1] + 30 + (50 * index))
        pen.pendown()
        pen.goto(rod[0] + disk[0], rod[1] + 30 + (50 * index))

    #Removes Disks
    def remove_disk(disk, index, rod):
        pen.penup()
        pen.setposition(rod[0] - disk[0], rod[1] + 30 + (50 * index))
        pen.pensize(50)
        pen.color("white")
        pen.pendown()
        pen.goto(rod[0] + disk[0], rod[1] + 30 + (50 * index))
        #Replaces Rod
        pen.penup()
        pen.color("black")
        pen.pensize(15)
        pen.goto(rod[0], 150)
        pen.shape("square")
        pen.pendown()
        pen.goto(rod[0], rod[1] + (50 * index))

    set_rods()

    DISK_1 = (80, "Red")
    place_disk(DISK_1, 0, FIRST_ROD)
    DISK_2 = (65, "Green")
    place_disk(DISK_2, 1, FIRST_ROD)
    DISK_3 = (50, "Blue")
    place_disk(DISK_3, 2, FIRST_ROD)
    turtle.update()

    #Moves Smallest Disk: Step 1
    time.sleep(1.5)
    set_rods()
    place_disk(DISK_1, 0, FIRST_ROD)
    place_disk(DISK_2, 1, FIRST_ROD)
    place_disk(DISK_3, 0, THIRD_ROD)
    turtle.update()

    #Moves Middle Disk: Step 2
    time.sleep(1.5)
    set_rods()
    place_disk(DISK_1, 0, FIRST_ROD)
    place_disk(DISK_2, 0, SECOND_ROD)
    place_disk(DISK_3, 0, THIRD_ROD)
    turtle.update()

    #Moves Smallest Disk: Step 3
    time.sleep(1.5)
    set_rods()
    place_disk(DISK_1, 0, FIRST_ROD)
    place_disk(DISK_2, 0, SECOND_ROD)
    place_disk(DISK_3, 1, SECOND_ROD)
    turtle.update()

    #Moves Largest Disk: Step 4
    time.sleep(1.5)
    set_rods()
    place_disk(DISK_1, 0, THIRD_ROD)
    place_disk(DISK_2, 0, SECOND_ROD)
    place_disk(DISK_3, 1, SECOND_ROD)
    turtle.update()

    #Moves Smallest Disk: Step 5
    time.sleep(1.5)
    set_rods()
    place_disk(DISK_1, 0, THIRD_ROD)
    place_disk(DISK_2, 0, SECOND_ROD)
    place_disk(DISK_3, 0, FIRST_ROD)
    turtle.update()

    #Moves Middle Disk: Step 6
    time.sleep(1.5)
    set_rods()
    place_disk(DISK_1, 0, THIRD_ROD)
    place_disk(DISK_2, 1, THIRD_ROD)
    place_disk(DISK_3, 0, FIRST_ROD)
    turtle.update()

    #Moves Smallest Disk: Step 7
    time.sleep(1.5)
    set_rods()
    place_disk(DISK_1, 0, THIRD_ROD)
    place_disk(DISK_2, 1, THIRD_ROD)
    place_disk(DISK_3, 2, THIRD_ROD)
    turtle.update()
    time.sleep(2)

wn.mainloop()
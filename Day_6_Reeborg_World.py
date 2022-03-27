# Reeborg's World puzzle for python beginner - Maze Puzzle
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Angela Yu solution
# This code only work in Reeborg's World

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# to solve a extreme case bug - robot turn in circle in infinity loop in open space(turn right all the time), push robot to the wall
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clera():
        move()
    else:
        turn_left()

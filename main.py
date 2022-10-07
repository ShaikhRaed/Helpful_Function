from stanfordkarel import *


def main():
    move_row()
    turn_left()
    move()
    turn_left()
    move_row()
    turn_right()
    move()
    turn_right()
    move_row()
    turn_left()
    move()
    turn_left()
    move_row()
    turn_right()
    move()
    turn_right()
    move_row()
    turn_left()
    move()
    turn_left()
    move_row()
    turn_right()
    move()
    turn_right()
    move_row()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_row():
    move()
    move()
    move()
    move()
    move()
    move()


if __name__ == "__main__":
    run_karel_program("7x7")

"""
See and make cool art based on templates

Author: Andres Orbe <aeo2136@g.rit.edu>
"""

import turtle
import time

CIRCLE_DEGREE = 360    # GLOBAL CONSTANT that never changes
REC_INCREMENT = (7/4)     # GLOBAL CONSTANT that determines how much bigger the circle get
GOlDEN_RATIO = 1.618      # Golden Ratio num

turtle.speed(0)   # makes the drawing go ZOOM


def circle(size):
    """
    circle draws a circle
    :param size: takes in a size to make the radius
    """
    turtle.circle(size)


def partition_drawing(size, partitions, amt_part):
    """
    partition_drawing is a recursive function that divides the circle into things via partition
    :param size: size of radius
    :param partitions: how many circles it will make in a circle, basically 360/partitions
    :param amt_part: param partitions but the value will decrement so it keeps going until amt of partitions are 0
    :return: partition_drawing(size, partitions, amt_part - 1)
    """
    partitions = abs(partitions)
    amt_part = abs(amt_part)
    if amt_part == 0:
        pass
    else:
        circle(size)
        turtle.left(CIRCLE_DEGREE / partitions)
        return partition_drawing(size, partitions, amt_part - 1)


def dope_circle_art(n, size, partitions):
    """
    dope_circle_art makes some concentric circles based on sie, amount of increments, and how many circle in 360 degrees
        + recursive function
    :param n: how many times the amount of circle are incremented
    :param size: the radius of the circle
    :param partitions: how many circles there are in 360 degrees
    :return: dope_circle_art( n - 1, REC_INCREMENT * size, partitions)
    """
    n = abs(n)
    size = abs(size)
    if n == 0:
        pass
    else:
        partition_drawing(size, partitions, partitions) # calls a recursive (tail recursion) to draw at each partition
        return dope_circle_art(n - 1, REC_INCREMENT * size, partitions)


#  dope_circle_art(4, 50, 40)  # FLAG

# def rec_tree(depth, size):



def nautilus(depth, size):
    dep = abs(depth)
    siz = abs(size)

    turtle.pencolor('gold')
    turtle.down()

    if dep == 0:
        pass
    else:
        turtle.circle(siz, 90)

        return nautilus(depth - 1, size / GOlDEN_RATIO)


#   nautilus(50, 180)    # FLAG

# def bonus_




def ult_circle():
    """
    ult_circle sets up the ultimate circle
    """
    turtle.bgcolor('black')
    turtle.pencolor('white')
    dope_circle_art(4, 50, 40)


def main():
    """
    main() prompts user about various questions
    """
    art_array = {
        0: 'Concentric Circles',
        1: 'Recursive Tree',
        2: 'Nautilus Drawing',
        3: 'Bonus Picture',
        4: 'Custom Baller Circle'
    }
    """
    IDEAS: 
        3: 'Thanos Car',
        4: 'Jackson Pollock'
    }
    """

    length_dict = len(art_array)

    for i in range(0, length_dict):
        print(art_array[i])
        if art_array[i] == art_array[0]:
            dope_circle_art(2, 40, 25)
            time.sleep(5)
            turtle.clear()
        elif art_array[i] == art_array[1]:

            time.sleep(5)
            turtle.clear()
        elif art_array[i] == art_array[2]:

            turtle.up()
            turtle.right(90)
            turtle.forward(200)
            turtle.left(90)

            nautilus(20, 180)
            time.sleep(5)
            turtle.clear()

        elif art_array[i] == art_array[3]:

            time.sleep(5)
            turtle.clear()

        elif art_array[i] == art_array[4]:
            ult_circle()
        else:
            print(' \'what what\' - macklemore')


main()
turtle.done()


#!/usr/bin/env python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area()))

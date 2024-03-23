import math
import turtle

from argparse import ArgumentParser


def scale_factor():
    return math.sqrt(2) / 2


def pythagoras_tree(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        t.forward(size)

        t.left(45)
        pythagoras_tree(t, order - 1, size * scale_factor())
        t.penup()
        t.backward(size * scale_factor())
        t.pendown()

        t.left(-90)
        pythagoras_tree(t, order - 1, size * scale_factor())
        t.penup()
        t.backward(size * scale_factor())
        t.left(45)


def main(order, size=1000):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(-90)
    t.penup()
    t.forward(size / 4)
    t.left(180)
    t.pendown()

    pythagoras_tree(t, order, size / 6)

    window.mainloop()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-o", "--order", default="7", help="Pythagoras' tree order (defaults to 7)"
    )
    args = parser.parse_args()
    main(int(args.order))

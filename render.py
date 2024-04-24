import os
import sys
import turtle

s, t = turtle.getscreen(), turtle.Turtle()
turtle.title("BSC Turtle Path Rendering")

with open(sys.argv[1], "r") as f :
    for line in f:
        exec(line)
        t.goto(cords[0], cords[1])

turtle.done()

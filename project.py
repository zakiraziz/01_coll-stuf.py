

from turtle import *
import colorsys
bgcolor('black')
tracer (500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hls_to_rgb(h,1,1)
        h += 0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor (c)
        begin_fill()
        rt (290)
        circle(i, 12)
        fd(i)
        fd (290)
        lt (29)
        for j in range(190):
            fd(i)
            circle(j, 290, steps=2)
            end_fill()
draw()
done()
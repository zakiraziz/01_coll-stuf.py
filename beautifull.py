import turtle as tur
import colorsys as cs

tur.setup(800, 800)
tur.speed(0)
# tur.tracer(10)  # You can uncomment this later if the code works without it
tur.width(2)
tur.bgcolor("black")

for j in range(25):
    for i in range(15):
        # Corrected the hsv_to_rgb arguments
        color = cs.hsv_to_rgb(i / 15, 1, j / 25)
        tur.color(color)
        
        tur.right(90)
        tur.circle(200 - j * 4, 90)
        tur.left(90)
        tur.circle(200 - j * 4, 90)
        tur.right(180)
        tur.circle(50, 24)

tur.hideturtle()
tur.done()
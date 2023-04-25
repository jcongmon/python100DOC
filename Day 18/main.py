import colorgram
import turtle
import random

def extract_colors(img):
    colors = colorgram.extract(img, 10)
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = (r, g, b)
        color_list.append(rgb)
    return color_list


def draw_row(t, color_list):
    for _ in range(10):
        t.pencolor(random.choice(color_list))
        t.forward(0)
        t.penup()
        t.forward(50)
        t.pendown()


def init_drawing(t, x_coord, y_coord):
    t.penup()
    t.setx(x_coord)
    t.sety(y_coord)
    t.pendown()


image = 'kusama_img.jpeg'
color_list = extract_colors(image)

turtle.colormode(255)
t = turtle.Turtle()
t.hideturtle()
t.pensize(20)
t.speed(0)
x_coord = -225
y_coord = -225

for i in range(10):
    init_drawing(t, x_coord, y_coord + 50*i)
    draw_row(t, color_list)


screen = turtle.Screen()
screen.exitonclick()

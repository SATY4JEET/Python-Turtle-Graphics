import turtle as t
import random
import colorgram

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def shapes():
    for sides in range(3, 10):
        for side in range(sides):
            timmy.color(random.choice(colors))
            timmy.forward(100)
            timmy.right(360/sides)

dir = [0, 90, 180, 270]

def randomwalk():
    timmy.pensize(10)
    timmy.hideturtle()
    timmy.speed('fast')
    for i in range(100):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(random.choice(dir))

def spirograph(size):
    # timmy.pensize(1)
    timmy.hideturtle()
    timmy.speed('fastest')
    for i in range(int(360/size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size)

def hirst(number_of_dots):
    theme = colorgram.extract('wallpaperflare.com_wallpaper.jpg', 10)
    timmy.speed("fast")
    timmy.penup()
    timmy.hideturtle()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    for i in range(1, number_of_dots+1):
        timmy.dot(15, random.choice(theme).rgb)
        timmy.forward(50)
        if i%10 == 0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)


# spirograph(5)
hirst(100)
screen = t.Screen()
screen.exitonclick()
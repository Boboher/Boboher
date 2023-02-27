 
 
import turtle

wn = turtle.Screen()
wn.clear()
wn.reset()
wn.title("bobosoft drawing expierience!")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.addshape("C:\Users\leerling\Downloads\main\start_button.gif")
wn.addshape("C:\Users\leerling\Downloads\main\colors_button.gif")
wn.addshape("C:\Users\leerling\Downloads\main\home_button.gif")
wn.addshape("C:\Users\leerling\Downloads\main\pen_up_button.gif")
wn.addshape("C:\Users\leerling\Downloads\main\pen_down_button.gif")
wn.addshape("C:\Users\leerling\Downloads\main\clear_button.gif")
wn.addshape("C:\Users\leerling\Downloads\main\drawing_size_up.gif")
wn.addshape("C:\Users\leerling\Downloads\main\drawing_size_down.gif")
#pen
pen = turtle.Turtle()
pen.color("black")
pen.speed(0)
pen.shape("square")
pen.shapesize(stretch_wid = 0.75, stretch_len = 2)
pen.left(90)
pensize = 3
pen.pensize(pensize)
pen.penup()
pen.hideturtle()
turtle.hideturtle()

#pen up button
pen_up_button = turtle.Turtle()
pen_up_button.shape("C:\Users\leerling\Downloads\main\pen_up_button.gif")
pen_up_button.penup()
pen_up_button.hideturtle()
pen_up_button.goto(320, -270)

#pen down button
pen_down_button = turtle.Turtle()
pen_down_button.shape("C:\Users\leerling\Downloads\main\pen_down_button.gif")
pen_down_button.penup()
pen_down_button.hideturtle()
pen_down_button.goto(320, -220)


#start button
start_button = turtle.Turtle()
start_button.penup()
start_button.shape("C:\Users\leerling\Downloads\main\start_button.gif")
start_button.goto(0, -220)

#colors button
colors_button = turtle.Turtle()
colors_button.penup()
colors_button.shape("C:\Users\leerling\Downloads\main\colors_button.gif")
colors_button.goto(0, 220)

#home button
home_button = turtle.Turtle()
home_button.penup()
home_button.shape("C:\Users\leerling\Downloads\main\home_button.gif")
home_button.goto(-380, 280)
home_button.hideturtle()

#clear button
clear_button = turtle.Turtle()
clear_button.shape("C:\Users\leerling\Downloads\main\clear_button.gif")
clear_button.penup()
clear_button.hideturtle()
clear_button.goto(-340, 280)

#size buttons
drawing_size_up = turtle.Turtle()
drawing_size_up.penup()
drawing_size_up.shape("C:\Users\leerling\Downloads\main\drawing_size_up.gif")
drawing_size_up.goto(210, -220)
drawing_size_up.hideturtle()

drawing_size_down = turtle.Turtle()
drawing_size_down.penup()
drawing_size_down.shape("C:\Users\leerling\Downloads\main\drawing_size_down.gif")
drawing_size_down.goto(210, -270)
drawing_size_down.hideturtle()



#colors(yellow, orange, red, purple, blue, cyan, green, brown, black, gray, white.)


yellow = turtle.Turtle()
yellow.color("yellow")
yellow.shape("square")
yellow.shapesize(10, 2)
yellow.hideturtle()
yellow.penup()
yellow.goto(-360, 0)

orange = turtle.Turtle()
orange.color("orange")
orange.shape("square")
orange.shapesize(10, 2)
orange.hideturtle()
orange.penup()
orange.goto(-300, 0)

red = turtle.Turtle()
red.color("red")
red.shape("square")
red.shapesize(10, 2)
red.hideturtle()
red.penup()
red.goto(-240, 0)


purple = turtle.Turtle()
purple.color("purple")
purple.shape("square")
purple.shapesize(10, 2)
purple.hideturtle()
purple.penup()
purple.goto(-180, 0)

blue = turtle.Turtle()
blue.color("blue")
blue.shape("square")
blue.shapesize(10, 2)
blue.hideturtle()
blue.penup()
blue.goto(-120, 0)

cyan = turtle.Turtle()
cyan.color("cyan")
cyan.shape("square")
cyan.shapesize(10, 2)
cyan.hideturtle()
cyan.penup()
cyan.goto(-60, 0)

green = turtle.Turtle()
green.color("green")
green.shape("square")
green.shapesize(10, 2)
green.hideturtle()
green.penup()
green.goto(0, 0)

brown = turtle.Turtle()
brown.color("brown")
brown.shape("square")
brown.shapesize(10, 2)
brown.hideturtle()
brown.penup()
brown.goto(60, 0)

black = turtle.Turtle()
black.color("black")
black.shape("square")
black.shapesize(10, 2)
black.hideturtle()
black.penup()
black.goto(120, 0)

grey = turtle.Turtle()
grey.color("grey")
grey.shape("square")
grey.shapesize(10, 2)
grey.hideturtle()
grey.penup()
grey.goto(180, 0)

white = turtle.Turtle()
white.color("black", "white")
white.shape("square")
white.shapesize(10, 2)
white.hideturtle()
white.penup()
white.goto(240, 0)










 
#functions
def pen_follow_mouse(x, y):
    pen.ondrag(None)
    pen.goto(x, y)
    pen.ondrag(pen_follow_mouse, btn=3)
    
def clear_screen(x, y):
    pen.clear()

def pen_up(x, y):
    pen.penup()

def pen_down(x, y):
    pen.pendown()

def start(x, y):
    start_button.hideturtle()
    clear_button.showturtle()
    home_button.showturtle()
    drawing_size_up.showturtle()
    drawing_size_down.showturtle()
    colors_button.hideturtle()
    pen_up_button.showturtle()
    pen_down_button.showturtle()
    pen.showturtle()

def colors(x, y):
    start_button.hideturtle()
    home_button.showturtle()
    yellow.showturtle()
    orange.showturtle()
    red.showturtle()
    purple.showturtle()
    blue.showturtle()
    cyan.showturtle()
    green.showturtle()
    brown.showturtle()
    black.showturtle()
    grey.showturtle()
    white.showturtle()
    
def home_screen(x, y):
    start_button.showturtle()
    clear_button.hideturtle()
    colors_button.showturtle()
    home_button.hideturtle()
    pen_up_button.hideturtle()
    pen_down_button.hideturtle()
    drawing_size_up.hideturtle()
    drawing_size_down.hideturtle()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.clear()
    yellow.hideturtle()
    orange.hideturtle()
    red.hideturtle()
    purple.hideturtle()
    blue.hideturtle()
    cyan.hideturtle()
    green.hideturtle()
    brown.hideturtle()
    black.hideturtle()
    grey.hideturtle()
    white.hideturtle()

def drawing_size_up_pressed(x, y):
    pen.pensize (pensize + 1)

def drawing_size_down_pressed(x, y):
    pen.pensize(pensize - 1)


# clolors
def yellow_pressed(x, y):
    pen.color("yellow")

def orange_pressed(x, y):
    pen.color("orange")

def red_pressed(x, y):
    pen.color("red")

def purple_pressed(x, y):
    pen.color("purple")
    
def blue_pressed(x, y):
    pen.color("blue")

def cyan_pressed(x, y):
    pen.color("cyan") 

def green_pressed(x, y):
    pen_color = "yellow"  

def brown_pressed(x, y):
    pen.color("brown")
    
def black_pressed(x, y):
    pen.color("black") 

def grey_pressed(x, y):
    pen.color("grey")

def white_pressed(x, y):
    pen.color("white")


 
#mouse binding
turtle.listen()
turtle.onscreenclick(pen_follow_mouse, btn=3)
clear_button.onclick(clear_screen)
start_button.onclick(start)
colors_button.onclick(colors)
home_button.onclick(home_screen)
pen_down_button.onclick(pen_down)
pen_up_button.onclick(pen_up)
drawing_size_up.onclick(drawing_size_up_pressed)
drawing_size_down.onclick(drawing_size_down_pressed)
yellow.onclick(yellow_pressed)
orange.onclick(orange_pressed)
red.onclick(red_pressed)
purple.onclick(purple_pressed)
blue.onclick(blue_pressed)
cyan.onclick(cyan_pressed)
green.onclick(green_pressed)
brown.onclick(brown_pressed)
black.onclick(black_pressed)
grey.onclick(grey_pressed)
white.onclick(white_pressed)
 

# Main game loop
while True:
    wn.update()



        
   
   

 



    




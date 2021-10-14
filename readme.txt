thank you for downloading my paint app!

there are a few things you need to do before opening the .py file for it to work.
first you need to make sure all of the files are in the same folder.
then you need to change your file directories as following:
for example: wn.addshape("D:\python\projects\start_button.gif")
change the "D:\python\projects\start_button.gif" in for where your file is located.
if you dont know where it is located you need to select the file wich you want to know the location of,
right click, choose properties, and there you will see the location.
now just copy the location and put \file name.gif behind it
now a part of the first codelines should look like this:

wn.addshape("disk\folder\start_button.gif")
wn.addshape("disk\folder\colors_button.gif")
wn.addshape("disk\folder\home_button.gif")
wn.addshape("disk\folder\pen_up_button.gif")
wn.addshape("disk\folder\pen_down_button.gif")
wn.addshape("disk\folder\clear_button.gif")
wn.addshape("disk\folder\drawing_size_up.gif")
wn.addshape("disk\folder\drawing_size_down.gif")

the disk\folder part should be changes for the file location wich you saw erlier in the properties tab.
also change this part of the code the same way:
#pen up button
pen_up_button = turtle.Turtle()
pen_up_button.shape("disk\folder\pen_up_button.gif")
pen_up_button.penup()
pen_up_button.hideturtle()
pen_up_button.goto(320, -270)

#pen down button
pen_down_button = turtle.Turtle()
pen_down_button.shape("disk\folder\pen_down_button.gif")
pen_down_button.penup()
pen_down_button.hideturtle()
pen_down_button.goto(320, -220)


#start button
start_button = turtle.Turtle()
start_button.penup()
start_button.shape("disk\folder\start_button.gif")
start_button.goto(0, -220)

#colors button
colors_button = turtle.Turtle()
colors_button.penup()
colors_button.shape("disk\folder\colors_button.gif")
colors_button.goto(0, 220)

#home button
home_button = turtle.Turtle()
home_button.penup()
home_button.shape("disk\folder\home_button.gif")
home_button.goto(-380, 280)
home_button.hideturtle()

#clear button
clear_button = turtle.Turtle()
clear_button.shape("disk\folder\clear_button.gif")
clear_button.penup()
clear_button.hideturtle()
clear_button.goto(-340, 280)

#size buttons
drawing_size_up = turtle.Turtle()
drawing_size_up.penup()
drawing_size_up.shape("disk\folder\drawing_size_up.gif")
drawing_size_up.goto(210, -220)
drawing_size_up.hideturtle()

drawing_size_down = turtle.Turtle()
drawing_size_down.penup()
drawing_size_down.shape("disk\folder\drawing_size_down.gif")
drawing_size_down.goto(210, -270)
drawing_size_down.hideturtle()

i hope you are now able to use my app.
note: right click and drag on the pen to move it

have fun!

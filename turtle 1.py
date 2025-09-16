import turtle
#set window file
window=turtle.Screen()
window.title('absolute positing')

#get default turtle and hide
the_turtle=turtle.getturtle()
the_turtle.hideturtle()

#create square(absolute positioning)
the_turtle.setposition(100,0)
the_turtle.setposition(100,100)
the_turtle.setposition(0,100)
the_turtle.setposition(0,0)

#exit on close window
turtle.exitonclick()

import turtle # Import Turtle
t = turtle.Turtle() # Create Turtle Object
wn = turtle.Screen() # Create turtle display screen
wn.setup(250,250) # Set display size
def gotopoint(x, y): # Creat callback function
    t.goto(x,y)
wn.onclick(gotopoint) # Create click event and connect it to callback function
wn.listen()
turtle.mainloop() # Loop main program
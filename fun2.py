import turtle
turtle.goto(0,0)

Up = 1
Down = 0
Left = 2
Right = 3
direction = None

def up():
    global direction
    global vertical
    vertical=True
    direction = 50
    print("You pressed the up key.")
    on_move()
def down():
    global vertical
    global direction
    vertical=True
    direction = -50
    print("You pressed the down key.")
    on_move()
def left():
    global vertical
    global direction
    vertical=False
    direction = -50
    print("You pressed the left key.")
    on_move()
def right():
    global vertical
    global direction
    vertical=False
    direction = 50
    print("You pressed the right key.")
    on_move()
    
    
    
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.listen()

def on_move():
    x,y = turtle.pos()
    
    if vertical:
        turtle.goto(x+0,y+direction)
    else:
        turtle.goto(x+direction,y+0)























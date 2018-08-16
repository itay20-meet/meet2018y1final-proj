import turtle


level=1
turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1500
SIZE_Y=1050
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 60
START_LENGTH = 1

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
turtle.register_shape("Dany.gif")
Dany = turtle.clone()
Dany.shape("Dany.gif")
Dany.penup()
Dany.goto(40,-40)

seeds=turtle.clone()
seeds.penup()
turtle.register_shape('seeds.gif')
seeds.shape('seeds.gif')
seeds.goto(40,-120)
seeds.ht()
seeds2 = seeds.clone()
seeds3 = seeds.clone()



seed_follow = False
seed_follow_2 = False
seed_follow_3 = False
num_seeds_taken = 0
holes = 3
bucket_follow = False
bucket_follow_2=False
bucket_follow_3=False
num_buckets_taken = 0
holes = 3

bucket=turtle.clone()
bucket.penup()
turtle.register_shape('bucket_water.gif')
bucket.shape('bucket_water.gif')
bucket.goto(120,-120)
bucket.ht()
bucket2 = bucket.clone()
bucket3 = bucket.clone()


holes = 3
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


UP_EDGE = 400
DOWN_EDGE = -500
RIGHT_EDGE = 600
LEFT_EDGE = -600

b=turtle.clone()
b.pensize(18)
b.pencolor('red')
b.penup()
b.goto(650,400)
b.pendown()
b.goto(650,-500)
b.goto(-600,-500)
b.goto(-600,400)
b.goto(650,400)




UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds

STEP=40
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 1
DOWN = 0
LEFT = 2
RIGHT = 3
direction = None
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP

def up():
    global direction 
    direction=UP #Change direction to up
    x,y=Dany.pos()   
    #print("You pressed the up key!")
    Dany.goto(x,y+STEP)
    if Dany.pos()[1] >= UP_EDGE:
        quit()
    if Dany.pos() in wall_pos:
        quit()
    if seed_follow:
        seeds.goto(Dany.pos())
    if seed_follow_2:
        seeds2.goto(Dany.pos())
    if seed_follow_3:
        seeds3.goto(Dany.pos())
    if bucket_follow:
        bucket.goto(Dany.pos())
    if bucket_follow_2:
        bucket2.goto(Dany.pos())
    if bucket_follow_3:
        bucket3.goto(Dany.pos())
    check()

direction = UP
    
def down():
    global direction
    direction=DOWN #Change direction to up
    x,y=Dany.pos()
    Dany.goto(x,y-STEP)

    if Dany.pos()[1] <= DOWN_EDGE:
        quit()
    if Dany.pos() in wall_pos:
        quit()
    if seed_follow:
        seeds.goto(Dany.pos())
    if seed_follow_2:
        seeds2.goto(Dany.pos())
    if seed_follow_3:
        seeds3.goto(Dany.pos())
    if bucket_follow:
        bucket.goto(Dany.pos())
    if bucket_follow_2:
        bucket2.goto(Dany.pos())
    if bucket_follow_3:
        bucket3.goto(Dany.pos())
    check()

direction = RIGHT    

def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    x,y=Dany.pos()
    Dany.goto(x+STEP,y)       
    print("You pressed the right key!")
    if Dany.pos()[0] >= RIGHT_EDGE:
        quit()
    if Dany.pos() in wall_pos:
        quit()
    if seed_follow:
        seeds.goto(Dany.pos())
    if seed_follow_2:
        seeds2.goto(Dany.pos())
    if seed_follow_3:
        seeds3.goto(Dany.pos())
    if bucket_follow:
        bucket.goto(Dany.pos())
    if bucket_follow_2:
        bucket2.goto(Dany.pos())
    if bucket_follow_3:
        bucket3.goto(Dany.pos())
    check()
    
direction = UP

def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    x,y=Dany.pos()
    Dany.goto(x-STEP,y)
    print("You pressed the left key!")
    if Dany.pos()[0] <= LEFT_EDGE:
        quit()
    if Dany.pos() in wall_pos:
        quit()
    if seed_follow:
        seeds.goto(Dany.pos())
    if seed_follow_2:
        seeds2.goto(Dany.pos())
    if seed_follow_3:
        seeds3.goto(Dany.pos())
    if bucket_follow:
        bucket.goto(Dany.pos())
    if bucket_follow_2:
        bucket2.goto(Dany.pos())
    if bucket_follow_3:
        bucket3.goto(Dany.pos())
    check()
        
num_watered = 0

def check():
    global level, holes, seed_follow, bucket_follow, bucket_follow_2, bucket_follow_3,seed_follow_2,seed_follow_3, num_buckets_taken, toilet, num_seeds_taken, num_watered
    #print(Dany.pos(),toilet.pos())
    if Dany.pos() == toilet.pos():
        toilet.ht()
        toilet.goto(3000,0)
        level =2
    if level == 2:
        pen.clear()
        pen.write("The monster left the light on. Turn it off"
                  , font=("Arial", 20, "normal"))
        light=turtle.clone()
        light.goto(40,120)
        turtle.register_shape("light.gif")
        light.showturtle()
        light.shape("light.gif")
        if Dany.pos() == light.pos():
            light.ht()
            turtle.bgcolor("Grey")
            level =3
            pen.clear()
            pen.write("The monster made big holes in the ground. grow the flowers", font=("Arial", 20, "normal"))
            seeds.st()
            seeds.stamp()
            bucket.st()
            bucket.stamp()
    if level ==3:    
        pot1 = turtle.clone()
        turtle.register_shape("pot.gif")
        pot1.shape("pot.gif")
        pot1.goto(-560,0)
        pot1.stamp()
        pot2 = turtle.clone()
        
        pot2.shape("pot.gif")
        pot2.goto(-560,-80)
        pot2.stamp()
        pot3 = turtle.clone()
       
        pot3.shape("pot.gif")
        pot3.goto(-560,-160)
        pot3.stamp()

        #print("Follow bools: ",bucket_follow,seed_follow,seed_follow_2,seed_follow_3)

        #print("num watered:",num_watered)
        if bucket.pos() == pot1.pos() and num_watered == 0:
            bucket_follow = False
            #print("w1")
            bucket.stamp()
            num_watered += 1
        if bucket2.pos() == pot2.pos() and num_watered == 1:
            #print("w2")
            bucket_follow_2 = False
            bucket2.stamp()
            num_watered += 1
        if bucket3.pos() == pot3.pos() and num_watered == 2:
            #print("w3")
            bucket_follow_3 = False
            bucket3.stamp()
            num_watered += 1
        if seeds.pos() == pot1.pos() and num_watered == 3:
            #print("seeds at pot")
            seeds.stamp()
            seed_follow = False
            num_watered += 1
        #print("positions:",seeds2.pos(),pot2.pos())
        if seeds2.pos() == pot2.pos()and num_watered == 4:
            seed_follow_2 = False
            seeds2.stamp()
            num_watered += 1
        if seeds3.pos() == pot3.pos()and num_watered == 5:
            seed_follow_3 = False
            seeds3.stamp()
            num_watered += 1

        flower=turtle.clone()
        turtle.register_shape("sunflower.gif")
        flower.shape("sunflower.gif")
        if num_watered == 6:
            print("TREEEEEES!")
            bucket.ht()
            bucket2.ht()
            bucket3.ht()
            seeds.ht()
            seeds2.ht()
            seeds3.ht()
            
            
        
            #########MAKE FLOWERS SHOW UP!

        #print(Dany.pos(),seeds.pos())
        #print("num seeds:",num_seeds_taken)
        if Dany.pos() == seeds3.pos():
            
            #print("SEEEDS!")
            seed_follow = True
            if num_seeds_taken == 0:
                seed_follow = True
                num_seeds_taken += 1
                #print(num_seeds_taken)
                seeds.st()
            if num_seeds_taken == 1:
                seed_follow_2 = True
                seeds2.st()
                num_seeds_taken += 1
            if num_seeds_taken == 2:
                seed_follow_3 = True
                seeds3.st()
            
                
        if Dany.pos() == bucket3.pos():
            print(1)
            if num_buckets_taken == 0:
                bucket_follow = True
                num_buckets_taken += 1
                print(num_buckets_taken)
            if num_buckets_taken == 1:
                bucket_follow_2 = True
                bucket2.st()
                num_buckets_taken += 1
            if num_buckets_taken == 2:
                bucket_follow_3 = True
                bucket3.st()
            
            

                
        
turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)


turtle.listen()

pencil = turtle.clone()
turtle.resizemode("user")
pencil.shapesize(4)

pencil.penup()
pencil.goto(-150,300)
pencil.pendown()
pen = pencil.clone()
pen.write("The monster left the toilet dripping, stop it.", font=("Arial", 20, "normal"))




wall_pos = [(-180, 180), (-180, 140), (-220, 140), (-180, 60), (-220, 60), (-260, 60), (-220, 20), (-100, 180), (-100, 140), (-100, 100), (-100, 60), (-100, 20), (-100, -20), (-100, -60), (-140, -60), (-60, 100), (-20, 100), (20, 100), (-20, 60), (-20, 20), (20, 20), (60, 20), (100, 20), (100, 60), (-260, -140), (-220, -140), (-180, -140), (-180, -180), (-180, -220), (-60, -260), (-60, -220), (-60, -180), (-60, -140), (-20, -180), (20, -180), (20, -140), (100, -180), (100, -220), (100, -180), (100, -140), (140, -140), (100, -140), (100, -100), (300, -60), (260, -60), (220, -60), (220, -100), (260, 140), (260, 140), (260, 140), (260, 100), (260, 60), (260, 20), (220, 100), (180, 100), (180, 60), (180, 20)]

pencil.penup()
pencil.shape("square")
for i in range(len(wall_pos)):
    wall_pos[i] = (wall_pos[i][0]*2, wall_pos[i][1]*2)
    


for wall in wall_pos:
    pencil.goto(wall)
    pencil.stamp()

toilet=turtle.clone()
turtle.register_shape("toilet.gif")
toilet.goto(440,-360)
toilet.shape("toilet.gif")
toilet.showturtle()
#toilet.stamp()


    







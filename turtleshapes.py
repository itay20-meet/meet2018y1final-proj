#import turtle

#num_pts = 5
#for i in range(num_pts):
   #turtle.left(360/num_pts)
   #turtle.forward(100)
   
#turtle.mainloop()


for i in range(100):
    count = i + 1
    if count %3 == 0:
        print("fizz")
    elif count %5 == 0:
        print("buzz")
    elif count %5 %3 == 0:
        print("fizzbuzz")
    else:
        print(count)

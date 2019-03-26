import turtle as Bobbie

# there are a few shapes you can give the pen
# eg turtle, circle, etc; the default is an arrow
Bobbie.shape("turtle")

# five pointed star
# five turns around 2 circles,
# gives a regular exterior angle of 144 degrees
Bobbie.color("green")
for x in range(5):
   Bobbie.forward(100)
   Bobbie.right(144)

# pentagon
# five turns around 1 circle
# gives a regular exterior angle of 72 degrees
Bobbie.color("red")
for x in range(5):
    Bobbie.forward(100)
    Bobbie.right(72)

# 6 squares drawn with a nested loop
Bobbie.color("blue")
angle = 10
for x in range(6):
    angle += 10
    Bobbie.left(angle)
    
    for x in range(4):
        Bobbie.forward(50)
        Bobbie.left(90)

# import turtle again so we are not calling it Bobbie
import turtle

# draw the tree recursively
# ie turn left & right and call yourself again
def tree(branchLen,t):
    if branchLen > 10:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    t.shape("turtle")
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("purple")
    tree(75,t)
    myWin.exitonclick()

main()


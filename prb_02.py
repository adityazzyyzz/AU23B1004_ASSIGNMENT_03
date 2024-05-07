import turtle 

wn = turtle.Screen()  

def squarepattern(t):
    """Draws a square pattern using the Turtle object t."""
    for i in range(5):
        for j in range(4):
            t.forward(50)
            t.right(90)
        t.right(72)        

def circlepattern(t):
    """Draws a circular pattern using the Turtle object t."""
    t.penup()
    t.goto(-200, -50)
    t.pendown()
    for i in range(4):
        t.circle(20 * (i + 1))

def triangle(t):
    """Draws a triangle using the Turtle object t."""
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    for i in range(3):
        t.forward(120)
        t.left(120)

def square(t):
    """Draws a square using the Turtle object t."""
    t.penup()
    t.goto(100, -100)
    t.pendown()
    for i in range(4):
        t.forward(90)
        t.right(90)

def star(t):
    """Draws a star using the Turtle object t."""
    t.penup()
    t.goto(100, 100)
    t.pendown()
    for i in range(5):
        t.right(144)
        t.forward(50)

def trianglepattern(t):
    """Draws a triangle pattern of hexagon using the Turtle object t."""
    t.penup()
    t.goto(-100, 130)
    t.pendown()
    for i in range(6):
        for j in range(3):
            t.forward(50)
            t.left(120)
        t.right(60)

def circle(t):
    """Draws a circle using the Turtle object t."""
    t.penup()
    t.goto(220, 200)
    t.pendown()
    t.speed(-5)
    for i in range(36):
        t.forward(10)
        t.right(10)

def sketch():
    """Draws various shapes and patterns using Turtle graphics."""
    t = turtle.Turtle()
    squarepattern(t)
    circlepattern(t)
    triangle(t)
    square(t)
    star(t)
    trianglepattern(t)
    circle(t)
    wn.exitonclick()

if __name__ == "__main__":
    sketch()

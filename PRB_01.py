import turtle

def repeat_shape(turtle_obj):
    
    for _ in range(15):
        for j in range(1):
            turtle_obj.forward(50)
            turtle_obj.left(90)
            turtle_obj.forward(50)
            turtle_obj.left(90)
            turtle_obj.forward(50)
            turtle_obj.left(90)
            turtle_obj.forward(50)
            turtle_obj.left(90)
        turtle_obj.left(30)


Demo_1 = turtle.Turtle()

repeat_shape(Demo_1)

turtle.done()

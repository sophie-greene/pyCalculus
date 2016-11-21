import turtle

def draw_square(turt):
    for i in range(1 ,5):
        turt.forward(200)
        turt.right(90)
def draw_art():
    win=turtle.Screen()
    win.bgcolor("red")
    
    brad=turtle.Turtle()
    brad.color("yellow")
    for i in range(72):
        draw_square(brad)
        brad.right(5)
    
    win.exitonclick()
draw_art()
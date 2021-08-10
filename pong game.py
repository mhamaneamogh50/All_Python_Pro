
import turtle

turtle.Screen()
turtle.title("Amogh Mhamane")
turtle.bgcolor("black")
turtle.setup(width=800,height=600)
turtle.tracer(0)

#main game loop

while True:
    turtle.update()


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(350,0)
# paddle B

# paddle Ball

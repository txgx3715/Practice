import turtle 
import time
turtle.color("red", "yellow")
turtle.speed(10)
turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()
time.sleep(3)

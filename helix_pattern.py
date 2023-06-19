import turtle 
loadWindow = turtle.Screen()
turtle.speed(10)
for i in rangew(100):
    turtle.circel(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()
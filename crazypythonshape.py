import turtle

# Hello, this is a really interesting shape I made with the 'turtle' library. 

turtle.bgcolor("black")
turtle.speed(9*10^800)
turtle.color("pink")

side=100
turtle.penup()
turtle.goto(0,0) 
turtle.pendown()

for side in range (1,400):
  turtle.forward(side)
  turtle.left(110)
  side=side+7

turtle.penup()
turtle.goto(500,500)

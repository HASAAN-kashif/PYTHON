import turtle
turtle.Screen().bgcolor('Aqua')
board=turtle.Turtle()
for c in range(3):
    board.forward(100)
    board.left(120)
board.penup()
board.left(90)
board.forward(50)
board.right(90)
board.pendown()
for c in range(3):
    board.forward(100)
    board.right(120)
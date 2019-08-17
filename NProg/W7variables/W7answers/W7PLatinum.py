# Variable Platinum
#magical shape modbil
import turtle
sides =  input("How Many sides?")
sideLength = input("How long should the sides be")
angle = input("Turning angle?")
colorLine = input("Color line?")
colorFill = input("color fill?")
lineThick = input("line thick?")



turtle.color(colorLine, colorFill)
turtle.pensize(int(lineThick))
turtle.begin_fill()
for i in range(int(sides)):
	turtle.forward(int(sideLength))
	turtle.left(int(angle))
turtle.end_fill()
turtle.done()
	

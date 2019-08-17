#turtleSilver
from turtle import *

#Goal: Introduct Fill and colors, draw an equalateral triangle 
#Note: Each Angle in an equilateral triangle is 60 Degrees.
	# The number we want is actually 180 - 60 = 120 Degrees for the turn 


color('purple', 'gold')
pen( pensize = 25)

begin_fill()

forward(200)
left(120)
forward(200)
left(120)
forward(200)
end_fill()
done()



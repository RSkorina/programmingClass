#W3 Platinum
from turtle import *
import math
#colors
americaRed = '#B22234'
americaBlue = '#3C3B6E'
americaWhite = '#FFFFFF'

start = position()
height = 300
length = height * 1.9
widthOfUnion = height * 7/13
lengthOfUnion = height/100 * 76
diameterOfStar = height*6.1/100
widthOfStripe = height/13
VerticleDistanceStar = height * 5.4/100
starSide = lengthOfUnion/ 15.4
starWidth = starSide * math.sin(36)




speed(0)
bgcolor('grey')

def stripe(selColor):
	color(selColor, selColor)
	begin_fill()
	forward(length)
	right(90)
	forward(widthOfStripe)
	right(90)
	forward(length)
	right(180)
	end_fill()
	
def star():
	color(americaWhite, americaWhite)
	begin_fill()
	i = 0
	while(i < 5):
		forward(starSide)
		right(144)
		i = i + 1
	end_fill()
	pass
	
def starSix():
	penup()
	right(90)
	forward(starSide)
	left(90)
	forward(starSide)
	pendown()
	i = 0
	
	while(i < 6):
		star()
		penup()
		forward(starSide * 2 * 1.2)
		pendown()
		i = i + 1
		
	penup()
	left(180)
	forward(starSide * 15.4)
	left(180)
	pendown()
	pass
	
def starFive():

	penup()
	right(90)
	forward(starSide * 1.2)
	left(90)
	forward(starSide * 2.2)
	pendown()
	i = 0
	while(i < 5):
		star()
		penup()
		forward(starSide * 2 * 1.2)
		pendown()
		i = i + 1
		
	penup()
	left(180)
	forward(starSide * 14.2)
	left(180)
	pendown()
	pass
	


i = 0
while(i < 12):
	i = i + 2
	stripe(americaRed)
	stripe(americaWhite)
stripe(americaRed)

penup()
goto(start)
pendown()


color(americaBlue, americaBlue)
begin_fill()
forward(lengthOfUnion)
right(90)
forward(widthOfUnion)
right(90)
forward(lengthOfUnion)
right(90)
forward(widthOfUnion)
right(90)

end_fill()

penup()
right(90)

left(90)
pendown()


starSix()
i = 0
while (i < 4):
	starFive()
	starSix()
	i = i + 1

done()
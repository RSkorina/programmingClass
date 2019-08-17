#W4 circle
from turtle import *
import math

bgcolor('black')
length = 400
width = length * 2 /3
radiusC = width/3
radiusDisk = radiusC /2

speed(0)
#first blue Stripe
color('#003366', '#003366')
begin_fill()
forward(length)
right(90)
forward(width/3)
right(90)
forward(length)
right(90)
 forward(width/3)
end_fill()
penup()
right(180)
 forward(width/3)
left(90)
pendown()

#White Stripe
color('white', 'white')
begin_fill()
forward(length)
right(90)
forward(width/3)
right(90)
forward(length)
right(90)
forward(width/3)
end_fill()
penup()
	right(180)
forward(width/3)
left(90)
pendown()
#blue stripe
color('#003366', '#003366')
start_fill()
forward(length)
right(90)
forward(width/3)
right(90)
forward(length)
right(90)
forward(width/3)
stop_fill()
penup()
right(180)
forward(width/3)
left(90)
pendown()

# Outer circle
penup()
forward(length/5 + radiusC)
left(90)
forward(width/6)
pendown()
right(90)
color('#BF0A30', '#BF0A30')
beginfill()
circle(radiusC)
endfill()

#Go up to white Stripe
penup()
	left(90)
forward(width/3 - width/6)
right(90)
#find the proper position of the triangle

altitude = width/(2.5)

forward(altitude)
turn = 90 - math.degrees(math.atan((width/6)/altitude))

lengthSide = ((width/6)**2 + altitude**2)**0.5
pendown()
color('white', 'white')
begin_fill()

left(90 + turn)

forward(lengthSide)
right(2* turn)
forward(lengthSide)
right(180 - turn)
forward(width/3)
end_fill()

penup()
right(90)
forward(altitude)
left(90)
forward(width/3 - width/6)
left(90)
pendown()


# #inner disk
penup()
left(90)
forward(radiusC - radiusDisk)
right(90)
pendown()
begin_fill()
color('#FFD700', '#FFD700')
circle(radiusDisk)
end_fill()


ending()
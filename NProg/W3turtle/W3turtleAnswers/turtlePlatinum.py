#turtle Platinum

#Goal: Make a Stop Sign. 

#import turtle
from turtle import *


#speed(10)


#Make the Octogon
color('black', 'red')
pen(pensize = 10)

begin_fill()
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
end_fill()

#Transition from Oct to S
#Replace red with no color
penup()	
#color('green', 'blue')
left(90)
forward(80)
left(90)
forward(40)
pendown()
#Make the S
color('white', 'blue')
left(180)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)

#Transition from S to T
penup()
forward(20)
pendown()
#Make the T
color('white', 'blue')
forward(30)
left(180)
forward(15)
left(90)
forward(80)

#Transition from T to O
penup()
left(90)
forward(35)
pendown()
#Make the O
color('white', 'blue')
forward(30)
left(90)
forward(80)
left(90)
forward(30)
left(90)
forward(80)
left(90)
forward(30)

#Transtition from O to P
penup()
forward(20)
pendown()

#Make the P 
color('white', 'blue')
left(90)
forward(80)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)


done()

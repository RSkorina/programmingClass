# Platinum if
#base snake
from turtle import *
dist = 20
pensize(10)
while(True):
	instructions = input("turtle: ")
	if(instructions == 'l'):
		left(90)
		forward(dist)
	elif(instructions == 'r'):
		right(90)
		forward(dist)
	else:
		forward(dist)
	

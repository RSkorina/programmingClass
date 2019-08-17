#W3 gold

#Redo all Turtle on one Screen With while loops
# Figure out How to clear the Screen
# Figure out How to paint the Screen


from turtle import *
i = 0
while(i < 4):
	forward(200)
	right(90)
	i =i + 1

color('purple', 'gold')
pen( pensize = 25)
begin_fill()
i = 0
while(i <3):
	forward(200)
	left(120)
	i = i +1
end_fill()


color('blue','blue')
pen( pensize = 10)
begin_fill()
i = 0
while(i < 5):
	forward(200)
	left(144)
	i = i +1
end_fill()

done()
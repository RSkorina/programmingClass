#W3 Silver
from turtle import *

color('green', 'brown')
pensize(10)

begin_fill()
i = 0
while(i < 13):
	i = i + 1
	forward(50)
	left(360/13)
end_fill()
done()
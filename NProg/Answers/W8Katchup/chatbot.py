# Python file Chatbot
for i in range(100):
	message = input("Next Command ")
	if(message == "hello"):
		print("hi")
		
	elif(message == "draw me a sqaure"):
		from turtle import *
		for j in range(4):
			forward(100)
			left(90)
		message2 = input("do you want me to draw you anything else?")
		if(message2 == "circle"):
			circle(100)
			
	else: 
		print("I don't understand, could you repeat that again?")
		
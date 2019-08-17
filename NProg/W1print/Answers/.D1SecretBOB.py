print("What is your name")
name = input()

while(True):
	print("How old are you?")
	age = input()
	try:
		float(age)
		break
	except:
		print("You can't be", age, "years old")



print("Hello", name, "you are", str(age), "years old")
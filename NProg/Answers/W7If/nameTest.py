name = input("What is your name?")
print(name + " Hi")

if (name == 'russell'):
	print("Welcome sir what would you like to do")
	response = input()
	if (response == "dance"):
		print("Well I guess we can dance, Let me find someone")
	elif(response == 'code'):
		print("Well I'll leave you alone")
	else:
		print("Sorry, I only dance")
else:
	print("leave")
	
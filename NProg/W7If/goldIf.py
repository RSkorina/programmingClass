# Gold if

print('welcome pLease enter your passwords')
pw1 = input("password1: ")
if (pw1 == 'paSSword'):
	print('1st password is correct')
else: 
	print("Sorry \"" + pw1 + "\" is the wrong password")
	exit()
	
pw2 = input("password2: ")
if (int(pw2) == 22):
	print('2nd password is correct')
else: 
	print("Sorry \"" + pw2 + "\" is the wrong password")
	exit()	
	
pw3 = input("password3: ")
if(int(pw3) > 10 and int(pw3) < 12):
	print('3rd password is correct')
else:
	print("Sorry \"" + pw3 + "\" is the wrong password")
	exit()

pw4 = input("password4: ")
haveFun = "have " + "fun"
if(pw4 == haveFun):
	print('4th password is correct')
else:
	print("Sorry \"" + pw4 + "\" is the wrong password")
	exit()

pw5 = input("password5: ")
password = "password"
for i in range(5):
	password = password + 'a'

	

if(pw5 == password):
	print('5th password is correct')
else:
	print("Sorry \"" + pw5 + "\" is the wrong password")
	exit()

print("congradulations you have completed gold")

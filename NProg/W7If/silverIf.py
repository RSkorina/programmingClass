# Siler IF
fakeName = 'Cicero'
answer1 = input('is ' + fakeName + ' your real name?')
if (answer1 == 'yes'):
	print('Hello ' + fakeName)
	
else: 
	realName = input('What is your real name?')
	print("Your name isn't " + fakeName + " so I guess it's " + realName)
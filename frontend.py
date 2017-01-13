from backend import updateLift
x = True
while x is True:
	option = input("Press <1> to see your lifts, press <2> to update them: ")
	if option == 1:
		f = open('lifts.txt', 'r')
		print f.read()
	elif option == 2:
		liftToChange = raw_input("What is the lift being updated?: ")
		updatedWeight = input("What weight are you lifting?: ")
		updateLift(liftToChange, updatedWeight)
	else:
		x = False
	cont = input("Press 1 to quit: ")
	if cont == 1:
		x = False
	else:
		x = True



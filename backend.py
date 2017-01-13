def read(self):
	f = open('lifts.txt', 'r')
	print file.read

def updateLift(self, liftDictionary, lift, weight):
	liftDictionary[lift] = weight
	f = open('lifts.txt', 'r')
	lines = f.readlines()
	f.close

	f = open('lifts.txt' ,'w')
	for line in lines:
		words = line.split(" ")
		if words[0] != 'lift':
			f.write(line)
	f.close()

	f = open('lifts.txt', 'a')
	f.write("{0} - {1}").format(lift, weight)
	f.close()





def updateLift(self, lift, weight):
	f = open('lifts.txt', 'r')
	lines = f.readlines()
	f.close

	f = open('lifts.txt' ,'w')
	for line in lines:
		words = line.split(" ")
		if words[0] != lift:
			f.write(line)
	f.close()

	f = open('lifts.txt', 'a')
	f.write("{0} - {1}").format(lift, weight)
	f.close()




import numpy as np
import sys
def print_my_name(name):
	#sys.stdout.write(name)
	arr = []
	for item in range(100):
		arr.append(name)
	return arr

listOfArguments = sys.argv[1:]
Name = str(listOfArguments[0])

sys.stdout.write(str(print_my_name(Name)))
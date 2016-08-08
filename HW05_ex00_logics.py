#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
	""" Print even or odd:
		Takes one integer from user
			accepts only non-word numerals
			must validate
		Determines if even or odd
		Prints determination
		returns None
	"""

	try:
		num = int(input("Enter the number "))
		if num % 2 == 0:
			print ("Even")
		else:
			print ("Odd")
	

	except:
		print ("Please enter a number in numerals")

def ten_by_ten():
	""" Prints integers 1 through 100 sequentially in a ten by ten grid."""
	for x in range (1,101):
		
		if x%10 == 0:
			print(str(x))
		else:
			print (str(x).ljust(2),end = " ")

	


def find_average():
	""" Takes numeric input (non-word numerals) from the user, one number
	at a time. Once the user types 'done', returns the average.
	"""
	sum = 0
	count = 0 
	while True:
		try:
			num = input("Enter the number ")
			if num == 'done':
				break
			count += 1
			number = int(num)
			sum = sum + number
		except:
			print("Enter a number in numerals")
	return (sum/count)
		
	


#############################################################################

def main():
	""" Calls the following functions:
		- even_odd()
		- ten_by_ten()
	Prints the following function:
		- find_average()
	"""
	even_odd()
	ten_by_ten()
	print("The average is " + str(find_average()))
	
if __name__ == '__main__':
	main()

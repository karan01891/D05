#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body

name = input("Enter file:")
if len(name) < 1 : name = "words.txt"
handle = open(name)

def counter():
	for line in handle:
		line.strip()
		if len(line) > 20:
			print (line)

##############################################################################
def main():
      # Call your functions here.
	counter()

if __name__ == '__main__':
    main()

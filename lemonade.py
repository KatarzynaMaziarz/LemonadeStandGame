#!/usr/bin/env python3
from random import *

def startGame():
	print("The weather is hot and you're broke.")
	print("With only $1 left in your pocket, the only thing you can do")
	print("is start a lemonade stand.")
	answer = input("Interested? (y/n) ")
	answer = answer[0].lower()
	
	while not (answer == 'y' or answer == 'n'):
		print("It's not a huge decision:")
		print("you either want to start a lemonade stand")
		print("or you don't.")
		answer = input ("Interested?(y/n) ")
		answer = answer[0].lower()
	
	if answer == 'n':
		print("Totally understable. The small business life"
		print("isn't for everyone.")
		quit = True
		
	else:
		print("Fantastic! Get out some posterboard and markers")
		print("and get ready to triumph!")
		print()
		quit = False
		print("Press enter to continue...")
		print()
		input()
	
	return quit

quit = startGame()



print()
print("Goodbye!")

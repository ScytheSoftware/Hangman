#DaVonte' Whitfield

import os
import re

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")
#nt is a window check, if you are on window use cls, else clear(Mac)


def lowerCase(t):   #To compare the input throughout the code with lowercase only
	return t.lower()

def upperCase(j):
	return j.upper()

def HangManWord(): #This is a one time prompt to enter a word to start the game.
	
	loop_count =0
	clear_screen()
	fixed = False

	while fixed != True:
		hmw = input("Enter a Word or sentence: ")
		
		for letter in hmw:
			#Number check
			if letter > "A": #Lexicographical at work here 0 < 9 < A < a
				if loop_count < len(hmw):
					fixed = True

			#Symbol check
			elif re.search(r'[^\w]', letter) and letter != " ":
				print("Symbols shouldn't be entered. Re-enter the word or sentence.")
				fixed = False
				loop_count = 0 #Resetting loop counter
				break

			elif letter == " ":
				continue

			else:
				print("Numbers shouldn't be entered. Re-enter the word or sentence.")

				fixed = False
				loop_count = 0 #Resetting loop counter
				break

			loop_count += 1

	return hmw


def convertion(theWord): #Converting the game word with underscores
    underscoreWord = ("_" * len(theWord)) #This might be the place to do the "space" logic

    return underscoreWord
    

def guess(unscoreWord): #The guessing letter function. It also displays the number of mistakes and the playing board
	fixed = False
	
	print("Current playing board")
	print(f"Number of mistakes: {mistakeCounter}")
	print(unscoreWord) #The playing board
	print("\n")

	guessedLetter = input("Guess a letter for the word on the board: ")

	while fixed != True: #Triggering the error means you've entered a letter, correct
		
		try:#Number check
			if int(guessedLetter):
				print("Invaild character entry. Type in letters, try again.")
				guessedLetter = input(">> ")

		except:
			fixed = True

			#Checking for symbols
		if re.search(r'[^\w]', guessedLetter):
			print("Symbols shouldn't be entered. Type in letters, try again.")
			fixed = False
			guessedLetter = input(">> ")


		elif len(guessedLetter) > 1:
			print("There shouldn't be more than one characters entered. Type in letters, try again.")
			fixed = False
			guessedLetter = input(">> ")

	return guessedLetter


def fix_guess():
	guessedLetter = input("Guess a letter for the word on the board: ")

	return guessedLetter


def auto_space():
	return " "


def Winner(): #If you guessed evrything correct
	print("")
	print("You've Won!")
	print(f"The number of mistakes left were: {mistakeCounter}")
	print(unscoreWord)
	print("\n")


def Lose(): #If you failed to guess
	print("")
	print("You've Lose... You've made too many mistakes.")
	print(f"The word was '{GameWord}'")
	print("\n")


mistakeCounter = 0 
cheakerCounter = 0 #This is used to cheaker if the playing board variable has any underscores left.
underscoreCheaker = r"_" #regular expressions used in a if statement to check for underscores
Finished = False #Changes if game is finished or not based on mistakes or guessed correctly

print("Hello, Welcome to the game HangMan!")
print("To get started, type a word/phrase to use for the game and you can guess each letter." +
"\nThe letters with be underscores until you guess right. You get 10 mistakes max, so be careful!")


GameWord = HangManWord()
unscoreWord = convertion(GameWord)
confirmed_letters = []
letter_check = False
loop_count = 0


while (mistakeCounter != 10) and (Finished == False):

	if " " in GameWord and loop_count == 0:
		guessedL = auto_space()

	else:
		clear_screen()
		print("Letters that were Used: ")

		print(*confirmed_letters, sep = (", "))
		guessedL = guess()

	letter_check = False # Resetting variable

	while letter_check == False and loop_count >= 1:
		if guessedL not in confirmed_letters:
			confirmed_letters.append(guessedL.lower())
			letter_check = True

		else:
			print("You already typed that letter in. Type in a different letter.")
			guessedL = fix_guess(unscoreWord)

	for letter in range(len(GameWord)):
		if lowerCase(guessedL) == lowerCase(GameWord[letter]):

			temp = list(unscoreWord)#These three line makes the word an array of chars to change the correct item out. 
			
			for i in range(len(GameWord)):
				if lowerCase(guessedL) == lowerCase(GameWord[i]): #If a word has two of the same letters, replace both
					if upperCase(guessedL) == GameWord[i]:#UpperCase
						temp[i] = upperCase(guessedL)

					elif lowerCase(guessedL) == GameWord[i]:#Lowercase
						temp[i] = lowerCase(guessedL)

			unscoreWord = ''.join(temp) #Joins them in finished.

			cheakerCounter = 0 #This is reset to 0 if you entered a correct letter. 
			break

		else:
			cheakerCounter += 1

	if cheakerCounter >= 1: #If entered a incorrect letter, add to mistakeCounter and reset cheakerCounter.
		mistakeCounter += 1
		cheakerCounter = 0	

	if re.search(underscoreCheaker, unscoreWord): #Cheaking to see if there are underscores in the playing board still.
		Finished = False

	else:
		clear_screen()

		print("Letters that were Used: ")
		print(*confirmed_letters, sep = (", "))
		Winner()
		Finished = True

	loop_count += 1

	

if mistakeCounter == 10: #If 10 mistakes are reached, end the game.
	clear_screen()

	print("Letters that were Used: ")
	print(*confirmed_letters, sep = (", "))
	Lose()

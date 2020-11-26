import random

def GuessMe():
	print("Hi, I'm Julie. Welcome to my Challenge!")
	# --- Measure to avoid exceptions --- #
	print("Here are some things to take note of:")
	print("\n** You are required to select a difficulty to begin your challenge.")
	print("\n** All guesses entered should be entered in integers.\n\nGreat. Now you know the rules.\nLet's begin!!")
	
	PlayOneRound()
	
	while True:		# --- Allow for continous playing till user says otherwise --- #
		goAgain = input("Play Again? [Press 'Y' to continue or 'N' to quit]: ").upper()
		if goAgain == "N":
			print("Thank you for playing my challenge. Till next time. Cheers.")
			break
		else:
			PlayOneRound()

def PlayOneRound():
	levels = ["Easy", "Medium", "Hard", "Legend", "Wizard"]    # --- Difficulty to make the game challenging and interesting --- #
	print("\nDifficulty:-")		# --- Difficulty to make the game challenging and interesting --- #
	
	for i in levels:
		print("=> {}".format(i))
	
	difficulty = input("\nPlease select a difficulty: ").title()
	if difficulty == "Easy":
		MAX_GUESS = 5
		MAX_RANGE = 25
	elif difficulty == "Medium":
		MAX_GUESS = 5
		MAX_RANGE = 50
	elif difficulty == "Hard":
		MAX_GUESS = 5
		MAX_RANGE = 75
	elif difficulty == "Legend":
		MAX_GUESS = 5
		MAX_RANGE = 100
	else:
		MAX_GUESS = 5
		MAX_RANGE = 200
	print("\nHere's how it goes; I'll pick a number between 1 and ",MAX_RANGE,". Try guessing the number.")
	print("Alright, let's see how lucky you feel. You have",MAX_GUESS,"trials.")
	target = random.randrange(1,MAX_RANGE + 1)
	guesscounter = 0
	
	while True:		# ---- Loop the guessing process --- #
		userGuess = int(input("\nTake a guess: "))	
		guesscounter = guesscounter + 1
		if userGuess == target and guesscounter == 1:
			print("\nBoy!! You must be a Wizard because that is incredible and definitely not natural")
			print("Congrats!! You got the number right in",guesscounter,"attempt")
			break
		elif userGuess == target and guesscounter == 2:
			print("\nHot stuff man! You are blazing. Who got some ice please?")
			print("Congrats!! You got the number right in",guesscounter,"attempts")
			break
		elif userGuess == target and guesscounter == 3:
			print("\nNice going. You're good at this.")
			print("Congrats. You got the number right in",guesscounter,"attempts")
			break
		elif userGuess == target and guesscounter == 4:
			print("\nSpot on. Shows how adaptable you are.")
			print("Congrats. You got the number right in",guesscounter,"attempts")
			break
		elif userGuess == target and guesscounter == 5:
			print("\nLOL!! You must really be lucky today because this was your last try. All the same, nice job.")
			print("Congrats. You got the number right in",guesscounter,"attempts")
			break
		elif userGuess > target:
			print("\nNice effort. Just a bit high off.")
			print("Go again.")
		else:
			print("\nNot a chance. That's too low.")
			print("Try a higher guess this time.")
		
		if guesscounter == MAX_GUESS: 	  # --- GAMEOVER --- #
			print("\nSorry, you've exhausted your chances. Maybe next time, you'll get it right.")
			print("The number I had in mind was",target,". Better Luck in the future. <smiles>.")
			print("Try playing again.")
			break


if __name__ == "__main__":
	GuessMe()	
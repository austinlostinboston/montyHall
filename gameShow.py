import random

def playGame(iterations,style="switch"):

	'''Plays the famous Monty Hall Gameshow.
	The gameshow consists of three doors. Behind two
	doors are goats (for TV entertainment purposes)
	and behind one door is a new car (probably some Chevy
	Citation that your grandmother drove you around in when
	you were a kid). The player chooses one door. After this,
	the gameshow reveals a door that neither contains the door
	or the palyers first guess. After seeing the door,
	the player has the option to switch their answer to the
	third, unseen door. The paradox here is that the player has
	a 2/3 chance of winning the car when they switch their answer.
	The code simulates this and proves this theory correct.

	playGame(iterations)
	iteration - integer: simulates gameshow for specified iterations.
	'''
	wins = 0
	losses = 0

	for i in range(iterations):

		## Initialize separate lists to keep track of the
		#  gameshows options, the player's options, and the 
		#  the options available to show the goat
		showsOptions = [1,2,3]
		playersOptions = [1,2,3]
		doorShowOptions = []

		## Randomly place car behind 1 of 3 doors
		#  Player randomly chooses door
		car = random.choice(showsOptions)
		playerChoice = random.choice(playersOptions)

		## Remove the door that the car is behind from the
		#  gameshows list and do the same for the players
		#  first choose
		showsOptions.remove(car)
		playersOptions.remove(playerChoice)

		## Take the union bewteen the doors left in the
		#  gameshow's and players options of doors to
		#  choose from. The results are the doors that
		#  that don't contain the car or the players 
		#  first choose
		doorShowOptions = list(set(showsOptions).intersection(playersOptions))
		
		## Randomly pick from 1 or two doors that
		#  don't contain the car, to show to the 
		#  player.
		doorShow = random.choice(doorShowOptions)

		## After seeing the door open with a goat,
		#  the player has the option to stick with
		#  their first guess or change to the unseen
		#  door. In this case, the player chooses to
		#  change to the unseen door, from their orig-
		#  nal guess.
		if style == "switch":
			playersOptions.remove(doorShow)
			finalChoice = playersOptions[0]

		if style == "stay":
			finalChoice = playerChoice
		
		## Count numbers of wins and losses
		if finalChoice == car:
			wins += 1
		else:
			losses += 1

	## Print out stats
	print "Games Simulate: " + str(iterations)
	print "  Wins: " + str(wins)
	print "Losses: " + str(losses)

	#print car, playerChoice, secondChoice

if __name__ == "__main__":
	playGame(1000000,"stay")


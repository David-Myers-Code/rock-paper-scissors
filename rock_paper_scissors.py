'''
David Myers
CITPT 106
Rock Paper Scissors

Algorithm:
Intro to game
create function for computer turn
Create main function for game
make WHILE TRUE function that loops game until user quits
Display scores
get input from user
run computer turn
compare the two choices and let player know who won
update scoreboard

'''
import random
print "Welcome to Rock, Paper, Scissors."
print "Remember, paper beats rock, rock beats scissors, and scissors beat paper."

def computer_play():	#computer turn function
	global computer_turn
	computer_turn = random.randint(1, 3) #1 for rock, 2 for paper, 3 for scissors
	return computer_turn

computer_score = 0		#computer score starts at zero
player_score = 0		#player score starts at zero

	
def main():			#main function
	while True:		#run function while true
		#scoreboard
		global computer_score, player_score, computer_turn
		print "------------------------------------------------------------------------"
		print "The score is Player: {} and Computer: {}".format(player_score, computer_score)
		
		#get player input
		print "What do you choose to play?"
		print "Type one:  rock - paper - scissors	"
		print "Type quit to exit program"
		player_turn = raw_input("")
		
		#format input
		player_turn = player_turn.strip()
		player_turn = player_turn.lower()
		
		#run computer turn
		computer_play();
		
		print ""
		print "You choose {}".format(player_turn, computer_turn)
		
		#if else statements based on choices
		if player_turn == "rock" and computer_turn == 3:
			print "The computer chooses scissors"
			print "You win"
			player_score = player_score + 1
			continue
			
		elif player_turn == "rock" and computer_turn == 2:
			print "The computer chooses paper"
			print "You lose"
			computer_score = computer_score + 1
			continue
			
		elif player_turn == "rock" and computer_turn == 1:
			print "The computer chooses rock"
			print "It's a tie"	
			continue
					
		if player_turn == "paper" and computer_turn == 1:
			print "The computer chooses rock"
			print "You win"
			player_score = player_score + 1
			continue
			
		elif player_turn == "paper" and computer_turn == 3:
			print "The computer chooses scissors"
			print "You lose"
			computer_score = computer_score + 1
			continue
			
		elif player_turn == "paper" and computer_turn == 2:
			print "The computer chooses paper"
			print "It's a tie"	
			continue			
		if player_turn == "scissors" and computer_turn == 2:
			print "The computer chooses paper"
			print "You win"
			player_score = player_score + 1
			continue
			
		elif player_turn == "scissors" and computer_turn == 1:
			print "The computer chooses rock"
			print "You lose"
			computer_score = computer_score + 1
			continue
			
		elif player_turn == "scissors" and computer_turn == 3:
			print "The computer chooses scissors"
			print "It's a tie"	
			continue	
			
		elif player_turn == "quit":
			break	
		
		else:
			print "Invalid play.  Try again"
			continue
			
main();
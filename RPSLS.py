# Rock-paper-scissors-lizard-Spock 

# helper functions
import random

def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        return "Not found"


def number_to_name(number):
    if number ==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number ==4:
        return "scissors"
    else:
        return "Number not found - 404"
    

    

def rpsls(player_choice): 
    print

    print "Player chooses " + player_choice
    
    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0,5)

    comp_choice = number_to_name(comp_number)

    print "Computer chooses " + comp_choice        
   
    difference = (player_number - comp_number)%5
    
    # use if/elif/else to determine winner, print winner message	       
    if difference==0:
        print "Tie"
    elif difference==1:
        print "Player wins!"
    elif difference==2:
        print "Player wins!"
    elif difference==3:
        print "Computer wins!"
    elif difference==4:
        print "Computer wins!"
    else:
        print "Something went wrong"
            
 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




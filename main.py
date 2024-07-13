from speech import speech
import random
import time


def manageplaystate():
    playstate = input("Do you still want to play? ")
    if "yes" in playstate.lower():
        playstate = True
    
    elif "no" in playstate.lower():
        playstate = False

    else:
        print("Couldn't undesrtand the input. Try again.")
        manageplaystate()
    return playstate



levels = {
    "easy": ["dairy", "mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]
}

#make sure player wants to play
playstate = manageplaystate()
# Print the 'hard' level words





#this will count the amount of right answers
winner_counter = 0

if not playstate:
    print("I see how it is...")
    quit()


difficulty = input("Pick a difficulty easy/medium/hard: ")


while playstate:
    match difficulty:
        case "1"|"easy":
            print(f"say the following words: {levels['easy']}")
            ans = speech()
            if all(word in ans.lower() for word in levels["easy"]):
                print(f"You got it! I could understand all those words: {ans}") 
                winner_counter += 1
                print(f"You got {winner_counter} points.")
                
            else:
                print("honestly, I'm surprised that you lost... This was easy as hell...")
                print(f"Here is your amount of points: {winner_counter}")
                
 
        case "2"|"medium":
            print(f"say the following words: {levels['medium']}")
            ans = speech()
            if all(word in ans.lower() for word in levels["medium"]):
                print(f"You got it! I could understand all those words: {ans}")  
                winner_counter += 1
                print(f"Here is your amount of points: {winner_counter}")
                

            else:
                print("Aw man, I guess you mispronounced something...")
                print(f"Here is your amount of points: {winner_counter}")
                
        case "3"|"hard":
            print(f"Say these words {levels['hard']}")
            ans = speech()

            if all(word in ans.lower() for word in levels["hard"]):
                winner_counter += 1
                print(f"You got it! I could understand all those words: {ans}")
                print(f"Here is your amount of points: {winner_counter}")
                
            
            else:
                print("you failed")
                print(f"Here is your amount of points: {winner_counter}")
    playstate=manageplaystate()            


print("Was nice having ya, bye!")
print(f"The amount of points you have was {winner_counter}")
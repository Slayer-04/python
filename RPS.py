#Rock paper Scissors Game
import random
def play_rps():
        user_score = 0
        computer_score = 0
        
        choices= ['rock', 'paper', 'scissors']
        rounds=(input("Play best of 7 or inifinitely? (Enter '7' or 'inf'): "))
        if rounds == '7':
            for i in range(8):
                if i ==7:
                      if(user_score>computer_score):
                            print("You win the game!")
                            break
                      elif(user_score==computer_score):
                            print("It's a tie!")
                            break
                      else:
                            print("Computer wins the game!")
                            break
                      
                print(f"Round {i+1}")
                user=input("Enter rock, paper, scissors: ").lower()
                computer=random.choice(choices)
                print("Computer chose: ",computer)
                if user == computer:
                    print("It's a tie!")
                    print("Score: You:", user_score, "Computer:", computer_score)
                elif (user == 'rock' and computer == 'scissors') or \
                    (user == 'paper' and computer == 'rock') or \
                    (user == 'scissors' and computer == 'paper'):
                        user_score += 1
                        print("Score: You:", user_score, "Computer:", computer_score)
                        if user_score == 4:
                            print("You win the game!")
                            break
                                
                                
                else:
                    computer_score +=1
                    print("Score: You:", user_score, "Computer:", computer_score)
                    if computer_score == 4:
                        print("Computer wins the game!")
                        break
                            
        if rounds == 'inf':
            while True:
                user=input("Enter rock, paper, scissors or Quit: ").lower()
                if user =="quit":
                        print("Thanks for playing!")
                        break
                computer=random.choice(choices)
                print("Computer chose: ",computer)
                if user == computer:
                        print("It's a tie!")
                elif (user == 'rock' and computer == 'scissors') or \
                        (user == 'paper' and computer == 'rock') or \
                        (user == 'scissors' and computer == 'paper'):
                        print("You win!")
                else:
                        print("You lose!")
                       
           
        
                

def main():
    play_rps()
main()

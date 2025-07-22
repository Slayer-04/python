# Guess the number
import random
import math
def guess(num,actual):
    if(num==actual):
        print("Your Guess is correct.")
        return False
    elif(num-50>actual):
        print("Your guess is too high.")
        return True
    elif(num+50<actual):
        print("Your guess is too low.")
        return True   
    elif (abs(num-actual)<5):
        print("You are close.")  
        return True
    elif(num>actual):
        print("Your guess is high.")
        return True
    elif(num<actual):
        print("Your guess is  low.")
        return True
    else:
        return True
   
        
def main():
    actual=random.randint(0,100)  
    print("Guess the number between 1 and 100.")
    num=int(input("Enter Your Guess:"))
    while guess(num,actual):     
        num=int(input("Enter Your Guess:"))   
main()        

         
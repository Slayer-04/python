import random
import time

def math():
    score = 0
    start = input("Enter 'start' if you are ready: ").lower()

    if start == "start":
        print("You have 15 seconds! Go!")
        start_time = time.time()
        while time.time() - start_time < 15:
            operator = random.choice(['+', '-', '*', '/'])
            a = random.randint(0, 20)
            b = random.randint(1, 20) if operator == '/' else random.randint(0, 20)

            try:
                ans = float(input(f"{a} {operator} {b} = "))
                score = check(a, operator, b, ans, score)
            except ValueError:
                print("Invalid input. Moving on...")

        print("⏰ Time's up!")
        print("✅ Your final score is:", score)

def check(a,operator,b,ans,score):
    if operator== '+':
        if ans== a+b:
            score +=1
    elif operator== '-':
        if ans== a-b:
            score +=1
    elif operator== '*':
        if ans== a*b:
            score +=1
    elif operator== '/':
        if ans== a/b:
            score +=1  
    return score  
       
       

def main():
    math()
main()            



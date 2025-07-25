#Timer
import time
def timer():
    minutes=int(input("Enter the timer in minutes:"))
    total_seconds=minutes*60

    while total_seconds:
        minutes,seconds=divmod(total_seconds,60)
        print("minutes:",minutes,"seconds:",seconds)
        time.sleep(1)
        total_seconds -=1

    print("Times up")    

def reminder():
    remind=input("Enter the message to remind:")
    minutes = int(input("Enter the time to remind in minutes: "))
    total_seconds=minutes*60
    time.sleep(total_seconds)
    print(remind)    
def main():
    mode=int(input("Enter 1 to set timer and 2 to set reminder:"))
    if (mode==1):
        timer()
    elif(mode==2):
        reminder() 
    else:
        print("Invalid choice")       

main()
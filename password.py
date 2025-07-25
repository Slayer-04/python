import random
import string
def main():
    passLength=int(input("Enter the length of your password:"))
    character = (input("Enter character you need in password separated by space: ")).split()
    if len(character)>passLength:
        print("You have more characters than password length")
        return
    chars = string.ascii_letters + string.digits + string.punctuation
    randomList = [random.choice(chars) for _ in range(passLength-len(character))]
    passwordList = randomList + character
    random.shuffle(passwordList)
    password=''.join(passwordList)
    print("Your password is ",password)


main()    


 



import re
import string



def check():
    
    n = 0
    capital = normal = special = number = False
    
    while n <= 8 or capital == False or normal == False or special == False or number == False:
        
        password = input("enter your password: ")
        n = len(password)

        capital = False
        normal = False
        special = False
        number = False
        if n<=8: 
            print("password too short")
        if re.search(r"[A-Z]", password):
            capital = True
        if re.search(r"[a-z]", password):
            normal = True
        if any(char in string.punctuation for char in password):
            special = True
        if re.search(r"[0-9]", password):
            number = True
        
        if not capital:
            print("miss capital character")
        if not normal:
            print("miss normal character")
        if not special:
            print("miss special character")
        if not number:
            print("miss number")
    print("strong password")

def main():
    check()

main()
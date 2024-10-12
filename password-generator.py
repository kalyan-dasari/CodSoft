import random
import string

def generate_password(length):
    #combine all the lower case, upper case, numbers and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    #generates the password of all combinations
    password = ''.join(random.choice(characters) for i in range(length))
    return password



try:
    length = int(input("Enter the password length: "))    #input password length

    #condition for password length
    if length < 6:
        print("password must be atleast 6 characters length..! ")

    elif length > 15:
        print("password is too longer... max length is 15 only")
        
    else:    
        password = generate_password(length)
        print("The Generated password is: ",password)

except Exception:
    print("INVALID length.. Enter only numbers") 
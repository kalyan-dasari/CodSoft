#addition function
def add(a,b):
    return a + b

#subtraction function
def sub(a,b):
    return a - b

#multiplication function 
def mul(a,b):
    return a * b

#division function
def div(a,b):
    return a / b

#modulus function
def mod(a,b):
    return a % b

#input of two numbers
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
print("----------------------------")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division")
print("5. Modulus")
print("----------------------------")

choose = int(input("Enter which operation you want: " ))
#choose operation 
if choose == 1:
    print(f" {num1} + {num2} = {add(num1,num1)}")

elif choose == 2:
    print(f" {num1} - {num2} = {sub(num1,num1)}")

elif choose == 3:
    print(f" {num1} * {num2} = {mul(num1,num2)}")

elif choose == 4:
    print(f" {num1} / {num2} = {div(num1,num2)}")

elif choose == 5:
    print(f" {num1} % {num2} = {mod(num1,num2)}")

else:
    print("Incorrect option.. RETRY..!")
    
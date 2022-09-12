print("Pythagoras’ Calculator")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

option = int(input("Pick your option: "))

# C**2 = A**2 + B**2

if(option == 2 or option == 3):
    A = float(input("Please type your value for A: "))
if(option == 1 or option == 3):
    B = float(input("Please type your value for B: "))
if(option == 1 or option == 2):
    C = float(input("Please type your value for C: "))

if(option == 1):
    print(C**2 / B**2)
if(option == 2):
    print(C**2 / A**2)
if(option == 3):
    print(A**2 + B**2)
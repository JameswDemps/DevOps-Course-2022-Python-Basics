grade = int(input("What is your exam grade? "))

level = int(input("What is your level? "))

Fail = [50, 40]
Pass = [60, 50]
Merit = [70, 65]

if(grade < 0 or grade > 100):
    print("That mark isn't possible!")
elif(grade < Fail[level-1]):
    print("Fail")
elif(grade <= Pass[level-1]):
    print("Pass")
elif(grade <= Merit[level-1]):
    print("Merit")
else:
    print("Distinction")
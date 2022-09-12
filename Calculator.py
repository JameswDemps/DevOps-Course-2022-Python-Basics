import json

print("It's time to Calculate!")
int1 = int(input("Enter your first number: "))
int2 = int(input("Enter your second number: "))

options = [
    [
        1,
        "Add",
        "+"
    ],
    [
        2,
        "Subtract",
        "-"
    ],
    [
        3,
        "Multiply",
        "*"
    ],
    [
        4,
        "Divide",
        "%"
    ],
    [
        5,
        "Square",
        "s"
    ]
]

print("What would you like to do with your numbers?")

for item in options:
    print(str(item[0]) + ': ' + item[1] + ', ' + item[2])

choice = int(input("Please type the number of your option: "))

if(choice == 1):
    print(int1 + int2)
elif(choice == 2):
    print(int1 - int2)
elif(choice == 3):
    print(int1 * int2)
elif(choice == 4):
    print(int1 / int2)
elif(choice == 5):
    print(int1 ** int2)
else:
    print("Oops! That's not an option :(")
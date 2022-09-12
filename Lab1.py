print('Hello World!')

username='Bob'
age=32
print(username,'is',age,'years old')

print(username,' is '+ str(age) +' years old')

username=input('Please enter your name')
age = input('Please enter your age')
print(username,'is',age,'years old')

length=input('Please enter your length')
print(length)
lengthInt = int(length)
print(lengthInt)

width=input('Please enter your width')
widthInt = int(length)

print('Perameter=', lengthInt*2 + widthInt*2)
print('area=', lengthInt* widthInt)
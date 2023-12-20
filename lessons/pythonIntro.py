"""
Comments are preceded by a '#' or wrapped in triple quotes
Press `ctrl + /` to comment/uncomment a single line of code

Code written in this file will execute when you run this file. To run this file:
	1. Press ctrl + ` to open the terminal
	2. Type `python ./lessons/pythonIntro.py` to run this file
	3. After making a change, save the file and run it again to see the changes
		 `ctrl + s` to save, `up arrow` to recall the last command in the terminal, `enter` to run in the terminal

Now, we'll learn the basics, for more information, check out the Python docs:
https://docs.python.org/3/tutorial/index.html
https://www.w3schools.com/python/python_intro.asp
"""



# Variables
# Variables are used to store data for use in your program, different types have different advantages in different situations

exampleString = "This is a string"
exampleNumber = 42
exampleBoolean = True
exampleList = [1, 2, 3, 4, 5]
exampleDictionary = {
	"key1": "value1",
	"key2": "value2"
}

print("Variables: ", exampleString)



# Operators
# Operators are used to perform operations on variables and values, a few examples:

print("Operators: ", 1 + 1)
print("Operators: ", 2 - 1)
print("Operators: ", 2 * 2)
print("Operators: ", 4 / 2)
print("Operators: ", 5 % 2) # Can you guess what this does?



# If/Else Statements
# If/Else statements are used to make decisions in your code, a few examples:

a = 33
b = 200
if b > a:
	print("If/Else: b is greater than a")
else:
	print("If/Else: b is not greater than a")


	
# For Loops
for number in exampleList:
	print("For loop: ", number)



# While Loops
i = 1
while i < 6:
	print("While loop: ", i)
	i += 1 # Add 1 to i to keep this loop from running for ever



# Functions
# Functions are used to perform actions, they can be called from anywhere in your code
# Variables created inside functions are local, meaning they can only be used inside that function
# Variables created outside of functions are global, meaning they can be used anywhere in your code

def myFunction():
	localString = "This is a local string inside of a function"
	print("Function: ", localString)
	print("Function: ", exampleString)

# Uncomment the line below and attempt to print localString, it will throw an error
# print("Function: ", localString)
	
# Your function can take dynamic arguments, meaning you can pass in different values each time you call it
def myFunctionWithArgs(key):
	if key in exampleDictionary:
		print("Function with arg: ", exampleDictionary[key])
	else:
		print("Function with arg: Key not found")

myFunctionWithArgs("key1")
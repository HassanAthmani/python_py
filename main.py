# math function in python
import math
pi = 3.14
print(round(pi))  # rounds the number to the nearest whole number
print(math.ceil(pi))  # rounds of the number UP to the nearest integer
print(math.floor(pi))  # rounds the number down to the nearest integer
print(abs(pi))
print(pow(pi, 2))  # raises the number to the base
print(math.sqrt(420))  # finds square root of numbers"""

# string slicing-used to create a sub-string by extracting elements from another string indexing[] or slicing()
name = "Car Code"
first_name = name[0]  # finds the first element of the string
print(first_name)
last_name = name[:7]  # lists all the 7 elements from 0
print(last_name)
# slice functions
website = "https://google.com"
slic = slice(7, -4)
print(website[slic])

# if statement-A block of code that will execute if it's condition is true
age = int(input("How old are you:"))
if age > 100:
    print("You are old")
elif age > 0 and age >= 18:
    print("You're an adult")
else:
    print("You're a minor")

# logical operators-used to check if 2 or more conditional statements satisfy the condition given.
temp = int(input("enter your temperature:"))
if temp >= 0 and temp <= 30:
    print("abnormal temperature")
elif temp > 30:
    print("Very high temperature")
elif temp >= 25 and temp <= 28:
    print("Good temperature")

#  while loop-a statement that will execute it's block of code, as long as it's condition remains true.
name = " "
while len(name) == 0:
    name = input("Enter your name")
    print("hello"+ name)

#  for loop-A statement that will execute it's block of code a limited amount of time
for i in range (10):
    print(i)
for i in range(50,100):
    print(i)
import time
for seconds in range(10,0,-1): # This block of code executes a time count down and prints the message happy new year
    time.sleep(1)
    print(seconds)
    print("Happy New Year")

# Nested loops-
rows = int(input("Enter number of rows:"))
columns = int(input("Enter number of columns:"))
symbol = input("Enter the symbol you want to use")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
        print()

# Dictionaries-A changeable, disordered collection of unique value pairs fast because they use hashing allow us to
# use hashing allow us to use a value quickly
capitals = {
    'USA': 'Washington DC',
    'China': 'Beijing',
    'India': 'New Delhi',
    'Kenya': 'Nairobi'
}
print(capitals['Kenya'])
print(capitals.get('Kenya'))  # .get is used to find the value of a key
print(capitals.keys())  # used to list the keys in the dictionary
print(capitals.values())  # used to list the values in the dictionary
print(capitals.items())  # used to list the keys and their values in the dictionary
for key, value in capitals.items():
    print(key, value)
   

capitals.update({'Germany': 'Berlin'})  # adds the key and value in the dictionary
capitals.update(({'India': 'Mumbai'}))  # updates the value of an existing key
capitals.pop('China')

# Indexing-index operator[]-gives access to a sequences element(str,list,tuples)
name = "car Code"
if name[0].islower():
    name = name.capitalize()
    print(name)
first_name = name[0:3].upper()  # turns the 3 first elements to uppercase
print(first_name)
name = "CAR CODE"
last_name = name[4:0].lower()  # turns the
print(last_name)
last_character = name[-1]  # this negative indexing the last element is printed
print(last_character)

# functions-a block of code which is executed only when it is called


def hello(first_name, last_name, age):

    print("You are " + str(age) + " years old")
    print("Hello " + first_name + " " + last_name + ", you are " + str(age) + " years old.")


hello(first_name="Car", last_name="code", age=21)

#  Return statement-functions send python values/objects back to the caller.These valued
#  objects are known as functions return value


def multiply(num1, num2):
    result = num1*num2
    return result


print(multiply(6, 8))


#  *Args-parameter that will pack all arguments into a tuple,useful so that a function can accept a varying
#  amount of arguments, make sure you add the asterisk

def add(*args):
    sums = 0
    for i in args:
        sums += i
        return sums
    print(add(1, 2, 3, 4, 5))


#  **kwargs-parameter that will pack all the arguments into a dictionary useful so that a function
#  can accept a varying amount of keyword arguments.


def hello(**kwargs):
    print("hello"+""+kwargs['first']+""+kwargs['last'])

    hello(first="Bro", middle="Code", last="Car")

#  Iterating through each key and value in the dictionary


def hello(**stuff):
    print("hello", end=" ")
    for key, value in stuff.items():
        print(value, end=" ")
        hello(first="Bro", middle="Code", last="Dude")

#  Exception handling-events detected during execution that interrupt the flow of the program

try:
    numerator = int(input("enter a number to be divided:"))
    denominator = int(input("enter a number to divide by:"))
    result = numerator/denominator

except ZeroDivisionError:
    print("You cannot divide a number by zero!")
except ValueError:
    print("Enter only numbers!")
except Exception:
    print("Something is wrong:")
else:
    print("the result is"+" "+str(result))
finally:
    print("Thank you ):")


# Rock,Paper,Scissors code snippet 

import random  # use the random module for random choice.
choice = ["rock", "paper", "scissors"]
comp_choice = random.choice(choice)
player_choice = input("Please input your choice(rock/paper/scissors):").lower()
while player_choice is not choice:
    player_choice = input("Invalid choice.Enter your choice(rock/paper/scissors)")
    comp_choice = random.choice(choice)
    print("You chose:", player_choice)
    print("You chose:", comp_choice)
    if player_choice == comp_choice:
        print("You tied")
    elif player_choice == "paper" and comp_choice == "rock":
        print("You won (:")
    elif player_choice == "rock" and comp_choice == "scissors":
        print("You won (:")
    elif player_choice == "scissors" and comp_choice == "paper":
        print("You won (:")

    else:
        print("You lost ):")


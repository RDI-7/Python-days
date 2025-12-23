print("Found\nYou")     #print a new line after Found
print("Found\"You")     #print a double qoutation after Found
#print("Found\You")      #just print the backslash also known as escape character

phrase = "found you"
print(phrase + ", gini")    #doing concatenation(appending a string to a string)
print(phrase[0])            #get specific character from a string

print(phrase.index("u"))    #get specific character position in a string
print(phrase.replace("you", "gold"))    #replace specific word/character with specific word/character

number = 65
print(str(number) + " my score")        #converting a number into a string and append a string with it
print(pow(3,2))     #doing 3^2 math using pow() funtion

number = -7
print(abs(number))      #getting absolute value(only positive number) of a variable
print(max(3,5,22,34))   #getting the max(big) number among the provided numbers
print(min(3,2,35,6,1))  #getting the min(lowest) number among the provided numbers
print(round(3.7))       #round follow the natural rule of rounding a number  

from math import *      #importing everything from the math library
print(sqrt(36))         #performing the square root math
print(floor(3.9))       #no matter what floor funtion will print a round value
print(ceil(3.1))        

friends = ["kevin", "hudge", "john", "mathew"]
print(friends[1:])      #this will grab everything from index 1 to the end
print(friends[1:3])     #this will print everything between index 1 to 3, except 3
print(friends[-1])      #this will print back of the list, and back of the list start from -1
friends[1] = "kem"      #this change the index 1 to the assign value
print(friends[1])
friends2 = friends.copy()   #this copy the friends list into friends2 
print(friends2)

#number = int(input("Input the number you want to check: "))

# Age Group Checker 
age = int(input("Enter your age: "))
if age >= 20:
    print("Senior")
elif 18 <= age < 20:
    print("Adult")
elif 14 <= age < 18:
    print("Teen")
else:
    print("Child") 


#even/odd number loop
for num in range (1,20):
    if num % 2 == 0:
        print("even number", num)
    else:
       print("odd number", num)

# Multiplication table
number = int(input("enter your number: "))
for num in range(1,11):
    result = number * num
    print(number, "*", num, "=", result)
    

# Guess the Number Game
import random
secret_number = random.randint(1,10)

guess = 5
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess > secret_number:
        print("too high")
    elif guess < secret_number:
        print("too low" )
    else:
        print("Yes you are correct, you win !: ")


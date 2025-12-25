# exponent funtion
def power_of_number(num,pow_num):           #difining a function
    result = 1                              
    for number in range(pow_num):           #looping through number of pow_num, n this case between 0 to 3 but not 3 
        result = result * num               
    return result                           #returning the value of final result

print(power_of_number(3,3))                 # calling the function

#2D list
numbers = [
    [1, 2, 3, 4],                           #creating lists in a list
    [5, 6, 7, 8],
    [9, 10]
]

#nested loop
for row in numbers:                         
    for col in row:                 # this will first print 1 and that loop goes unless rows 2 col 1 not printed
        print(col)


# simple translator
def translator(phrase):
    translation = ""                #
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():        #if letter is uppercase, then this condition will apply
                translation = translation + "G"     #
            else:
                translation = translation + "g"
        else:
            translation = translation + letter      #if letter is not a vowel then apply this
    return translation      # returning the final value of translation to function

print(translator(input("Enter your Phrase: ")))

# Catching ERROR and handling it
# By this way we can handle ERRORS without making the program fall

try:
    value = 10/1
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError as err:            # if that specific error occur then it will printout as err
    print(err)
except ValueError as err:                   # if that specific error occur then it will printout as err
    print(err)

# Reading files
report = open("report.csv", "r")        #opening the file with read mode, other modes are w = write, r+ = read and write, a = append 
#print(report.read())                    #this will print everything inside the file
#print(report.readable())                #this will print boolean if the file is readable or not 
#print(report.readlines())               #this will print first line 
print(report.readlines()[1])            #this will print the line that is given as index
report.close()

# Writting files 
report1 = open("report1.csv", "w")                   #this will create a new file 
report1.write("This is a new file !")        #this will write that string to that file
report1.close()

#appending to a file
report = open("report.csv", "a")        # a = append, only alow to append something in the file
report.write("\nEnd of the file ! ")         #every time this code run , this will add that to the line
report.close()

# dictionaries
marks = {                       # a dict have keys and values
    "rafi":80,
    "ethan":40,
    "mark":78 
}
print("Rafis mark:", marks["rafi"])         # a dict key can call in square bracket []


# classes and object
            #file_name                  #class_name
from day3_sub_water_botol_class import water_botol      #water_botol is the name of class

water_botol1 = water_botol("spider_botol", "mum", "80tk", "Jisan")      # here i am creating a object called water_botol1 and assining values/data for the object 
print(water_botol1.name)        # here i am calling the object to give a specific attributes/variables data




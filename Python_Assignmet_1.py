#____________________________Task 1: Variables and Data Types ______________________________________

# a) Create three variables: one for storing your age (integer), one for your name (string), and one to 
#       check if you are a student (Boolean). Print the variables. 

name = "Tariq"       # String datatype variable
age = 22             # integer datatype varaible
student = True       # Boolean datatype varaible

if( student == True):
    print(f"My name is { name } and age is { age }") 
else:
    print("You are not a Student!")
#_______________________________________________________
#b) Perform the following operations and print the results: - Add 25 to your age variable. - Concatenate your name with
#     the string "Smith." - Negate the Boolean variable (if True, make it False, and vice versa). 
    
name = name + " Smith"   #  we concatenate one string to another string

age+=25                # we added 25 to the  age variable

student = not student    # I negate the student using not operator
# print(student)

if (student == False):
    print(f"My new name is { name } and age is { age } ")
else:
    print("You are not a Student!")


#__________________________________Task 2: String Manipulation _______________________________

# a) Create a string variable called "sentence" containing the sentence "Python is a powerful 
#    programming language." Print the sentence. 

sentence = "Python is powerful programmming language"
print(sentence)

#________________________________________________________
#b) Count the number of characters in the "sentence" and print the result. 

count_Char = len(sentence)    # Total number of character in the sentence i.e length of the sentence
print(count_Char)

#__________________________________Part c____________________
#c) Check if the word "Python" is present in the "sentence" and print the result (True/False).

if "Python" in  sentence:   # Check if "Python" is present in the sentence  or not
    print(True)
else:
    print(False)

#_________________________________Part d____________________
# d) Replace the word "powerful" with "versatile" in the "sentence" and print the updated sentence.  


sentence = sentence.replace("powerful","versatile")    # I replace the "powerful" by "versatile" in the original string
print(f"New sentence = {sentence}")

#_________________________________Part e____________________
# e) Split the "sentence" into a list of words and print the list. 


list_Of_Words= []

list_Of_Words = sentence.split(" ")   # split the sentence by space

print(f"List of words = {list_Of_Words}")

#_____________________________________________________________________________________________________________________

#___________________________________TASK 3: Expressions and Operators _________________________________
"""
a) A rectangle has a width of 5.5 units and a height of 3.25 units. Store width and height in variables. 
Create a new variable called area and write an expression to calculate the area. Print the area in the output. 
"""

length= 5.5                    # length of rectangle
width = 3.25                   # Widht of a rectangle

area = length * width          # Area of a rectangle

print(f"Area of a rectangle is = {area}")

#__________________________________Part b_____________________
"""
b) Create a temperature variable in Celsius. Convert it to Fahrenheit using the formula: F = (C * 9/5) + 32. Store this 
temperature in a variable called Fahrenheit and print this variable
"""

celsius = 28

fahrenheit = (celsius * 9/5) + 32

print(f"The temperature in Fahrenheit is = {fahrenheit}")

#_________________________________Part c_____________________________

""" 
Create a variable called radius and give it a value of 5. Calculate the area of a circle with this radius and store it in
a variable called area. Print area at the end of your code. (Use the formula: area = π * radius^2, where π (pi) is approximately 3.14159). 
"""

radius = 5     # A radius variable is initialze with 5 it the time of declaration

area = 3.14159 * (radius **2)
print(f"Area of Circle = {area}")


#_________________________________Task 4: Introduction to Data Structures List ___________________________________________

"""
a) Create a list called "fruits" containing the following fruits: "apple," "banana," "orange," "grape," and "kiwi."
 Print the list. 
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(f"The list of fruits is = {fruits}")

#_________________________________part b_____________________________________
"""
b) Create another list called "vegetables" containing the following vegetables: "carrot,
" "lettuce," "tomato," "broccoli," and "spinach." Print the list.
"""

vegetables = ["carot", "lettuce", "tomato","broccoli", "spinach"]
print(f"Vegetables are = {vegetables}")

#________________________________Part c____________________________
#c) Concatenate the "fruits" list with the "vegetables" list and store the result in a new list called "groceries". Print the "groceries" list. 

groceries = fruits + vegetables   # We concatenate the two lists 
print(f"groceries = {groceries}")

#______________________________Part d __ Sorting______________________
# d) Sort the "groceries" list in alphabetical order and print it

groceries = sorted(groceries)   # The sorted fun return a new sorted list  
# print(groceries.sort())   # sort() fun use inplace sorting . It does not return  a sorted list

print(f"The new sorted list is = { groceries}")

#-_______________________________part e ___________________--
# e) Remove the "banana" from the "fruits" list and print the updated "fruits" list. 

fruits.remove("banana")
print(f"The updated list of fruits = { fruits }")



### _______________________________TUPLE_________________________________________________________________________

#    a) Create a tuple named "colors" with the names of three colors of your choice. Print the tuple. 
colors = ( "red" , "green" , "blue" )
print(f"The tuple of colors is = { colors }")



# b) Access the second element of the "colors" tuple and print it. 

tuple_Element = colors[1]     # 2nd element of tuple
print(f"The second element of colors = { tuple_Element}")

#c) Concatenate the "months" tuple with the "colors" tuple and store the result in a new tuple called "combined_tuple". 
#      Print the "combined_tuple".

months = ("January", "Febuary", "March", "April","June")

combined_Tuple = colors + months
print(f"The combined tuple = { combined_Tuple }")




s
#                Python Assignment 2 Solution

#__________________________________________ Task 01:  ________________________________________________________

#_________ Question 01: Write a for loop that calculates the sum of numbers from 1 to 10. ____________________

total_Sum = 0
for var in range(11):
    total_Sum = total_Sum + var

print(f"total Sum from 1 to 10 = {total_Sum}")

#__________Question 02: Print the items of the list [“Python”, “Numpy”, “Pandas”] in reverse order  using a for loop. 

list1 = ["Python", "Numpy", "Pandas"] 

for number  in range(-1,-4, -1):   # -1 to -4 , decrement by -1 and -1 is included but -4 is excluded
    print(list1[number ])

#______________________________________________________________________________________________________________________

#____________________________________________Task 02:  ______________________________________________________________

"""_______ Question 01: Implement a guessing game with a while loop where the user has to  guess a set number
 (e.g., 3). The loop terminates once the user guesses correctly. """

guess_Number = 3

while True:
    user_Number = int(input("Enter a guess number >> "))
    if user_Number == guess_Number:
        print(f"You successfuly guessed the number {guess_Number}")
        break


"""
__________Question 02: Write a while loop that asks for user input and adds it to a list. Exit the  
loop when the user types "done". 
"""

user_List = []

while True:
    input_Data = input("Enter list element or done to exit >> ")

    if input_Data.lower() == "done":
        break
    else:
        user_List.append(input_Data)

print(f"The user input list = {user_List}")

#__________________________________________________________________________________________________________________

#___________________________________________Task 03:_______________________________________________________________
  
#________________Question 01: Write a function that prints all even numbers between 1 and 20. 

number = 1
print("Even number from 1 to 20 are : ")
while number <= 20:
    if number % 2 == 0:
        print(number )
    number += 1


#______________02: Write a function that takes a list and a number as arguments and returns. ____________________________

def fun_Return( list_Arg ,  num_Arg):
    list_Arg *= 2                   # double the list .. it is extra work.
    return list_Arg ,  num_Arg        # returun list_Arg and num_Arg

list1=[11,22,33]
num = 2
print(f"Original list = { list1 } and Number = { num}")

list_Returned , num_Returned = fun_Return( list1 , num)  

print(f"List Returned = {list_Returned}")
print(f"Number Returned = { num_Returned}")
    

#__________Question 03: Write a function calculator that takes three arguments: two numbers and an  operation
#____ (as a string, e.g., "add", "subtract", "multiply", "divide") and returns the result  of the operation. 

def calculator(num1 , num2 , operation ):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2 
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid Operation")
        quit()
    return result

num1 = 6
num2 = 2
print("Enter operation symbol from + , -  , * , / ")
operation = str(input (">>  "))  # We used str fun here b/c if user enter & , | it will not crush the program

result = calculator( num1 , num2 , operation)

print(f" Result = {result}")


#___________Question 04: Write a function that takes a list of numbers and returns the maximum  number in the list?

def fun_Max(list_Arg):
    max_Num = list_Arg[0]
    for check_Num in list_Arg:
       
        if max_Num < check_Num:
            max_Num = check_Num
        
    return max_Num

list1 = [11,77,22,99,24,101]
max_Num= fun_Max( list1)

print(f"Maximum number = { max_Num }")



#________________Question 05: Create a lambda function that takes two numbers and returns their product_____________

result = lambda num1 , num2 : num1 * num2

num1 = 3 
num2= 5
product = result ( 3, 5)
print(f"Product of {num1} * {num2} = {product}")



#_______________ Question 06: Write a function that takes a list and returns a new list containing only the  
#__________________________even numbers from the original list.

def fun_Check_Even(list_Arg):
    even_List = []
    for num in list_Arg:
        if (num %2) == 0 :
            even_List.append(num)
    
    return even_List


list_Orignal = [20,24,27,67,71,36,80,48,56,90,67,102,99]

even_List = fun_Check_Even( list_Orignal )
print(f"Even number list = {even_List}")


#__________________End  of Python Assignment 02____________________________________________________________________
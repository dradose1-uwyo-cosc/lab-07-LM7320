# Luke Jackson
# UWYO COSC 1010
# 11/03/24
# Lab 07
# Lab Section: 14
# Sources, people worked with, help given to: 
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered
message = "Give a posative number: "
answer = input(message)
answer = int(answer)
factorial = 1
factorial2 = 1
factored = 0
while(True):
    if answer > 0:
        if factored != answer:
            factorial2 = factorial2 * factorial
            factorial += 1
            factored += 1
            continue
        else:
            print(f"the factorial answer is {factorial2}")
            break
    else:
        answer = input(message)
        answer = int(answer)
        continue


print(f"The result of the factorial based on the given bound is {factorial}")

# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

message2 = "Give any number or type 'exit' to stop: "
num_sum = 0 

while message2.lower() != "exit":
    message2 = "Give any number or type 'exit' to stop: "
    message2 = input(message2)
    if message2 != "exit":
        n_answer = int(message2)
        num_sum = num_sum + n_answer
        continue
    
print(f"Your final sum is {num_sum}")

# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 


while(True):
    message3 = "Input a number an operation then another number: "
    answer3 = input(message3)
    a_list = []
    if "exit" not in answer3.lower():
        if " " in answer3:
            n_answer3 = "".join(answer3.split())
        else:
            n_answer3 = answer3
        if "+" in n_answer3:
            a_list = n_answer3.split('+')
            x = int(a_list[0]) + int(a_list[1])
            print(f"the sum is {x}")
        elif "-" in n_answer3:
            a_list = n_answer3.split('-')
            x = int(a_list[0]) - int(a_list[1])
            print(f"the difference is {x}")
        elif "/" in n_answer3:
            a_list = n_answer3.split('/')
            x = int(a_list[0]) / int(a_list[1])
            print(f"the quotient is {x}")
        elif "*" in n_answer3:
            a_list = n_answer3.split('*')
            x = int(a_list[0]) * int(a_list[1])
            print(f"the product is {x}")
    else:
        break
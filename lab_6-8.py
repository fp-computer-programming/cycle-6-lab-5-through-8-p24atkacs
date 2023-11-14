"""
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_6-5
Create a program that will take a list (of numbers) of any length and return the highest and lowest value in the list. If the list does not have at least 2 unique numbers, return the string: “error: list does not meet specifications”)
hint: test the program on lists of 0,1,2 + lengths, as well as lists that do and do not meet specifications! 


________________________________________________________________________________
Create a Python file named lab_6-6

Create a program that asks a user to input 5 unique words.
Construct a list of the 5 input values, in the order that the user gave them.
Have the program display a list where each index corresponds to the length of the word given by the user at the corresponding index.
You may assume accurate input values. NO LOOPS

_________________________________________________________________________________
Create a Python file named lab_6-7
Create a program that asks a user to input 3 numeric values
Construct a list of the 3 input values, in the order that the user gave them.
Have the program display a list with each of the values as integers that have been doubled 
You may assume accurate input values.

_________________________________________________________________________________
Create a Python file named lab_6-8
Create a program that asks a user to input 3 numeric values
Construct a list of the 3 input values, in the order that the user gave them.
Have the program display the string “even” if all numbers in the list are even.
Have the program display the string “odd” if all numbers in the list are odd.
Have the program display the string “mixed” if the numbers in the list are both even and odd.
You may assume accurate input values. You may NOT use a loop. 



"""

# Author: Andrew Tkacs

# Function to get input
def get_user_input():
    num_list = []  # Initialize an empty list to store numeric values
    
    # Get input from the user for 3 numeric values
    num_list.append(float(input("Enter a numeric value: ")))  # Using float to handle decimal inputs
    num_list.append(float(input("Enter another numeric value: ")))
    num_list.append(float(input("Enter the last numeric value: ")))
    
    return num_list

# Function to determine and display the nature of the numbers in the list
def display_number_classification(num_list):
    # Check if all numbers in the list are even
    if all(num % 2 == 0 for num in num_list):
        print("even")
    # Check if all numbers in the list are odd
    elif all(num % 2 != 0 for num in num_list):
        print("odd")
    # If the numbers in the list are both even and odd
    else:
        print("mixed")

# Main program
if __name__ == "__main__":
    # Get user input and construct the list
    user_numbers = get_user_input()
    
    # Display the string based on the nature of the numbers in the list
    display_number_classification(user_numbers)

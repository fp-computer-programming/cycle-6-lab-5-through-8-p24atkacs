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

def find_high_low(input_list):
    # Check if the list has at least two unique numbers
    unique_numbers = set(input_list)
    
    if len(unique_numbers) < 2:
        return "error: list does not meet specifications"
    
    # Find the highest and lowest values in the list
    highest_value = max(input_list)
    lowest_value = min(input_list)
    
    return highest_value, lowest_value


# test
test_list_1 = [4, 7, 2, 9, 1]
result_1 = find_high_low(test_list_1)
print("Test 1 Result:", result_1)

test_list_2 = [3, 3, 3, 3]
result_2 = find_high_low(test_list_2)
print("Test 2 Result:", result_2)

test_list_3 = [5]
result_3 = find_high_low(test_list_3)
print("Test 3 Result:", result_3)

test_list_4 = []
result_4 = find_high_low(test_list_4)
print("Test 4 Result:", result_4)

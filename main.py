# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
'''

The app will interactively take a string representing a simple mathematical expression from the user
(e.g. “12435+34569-12345*10+50”).
After the user inputs the string, the app will check if the string represents a valid expression (no unexpected string characters, no duplicate operation characters, etc.).
After validating the expression, the app will output a string containing the result.
 In case of invalid expression, it should output an appropriate error message.
For simplicity, we will consider only addition, subtraction, and multiplication operations.
Also, we will only consider integers. 
'''


def Numbers(number):
    #check if character is a number or symbol
    nums=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if number in nums:
        return True
    # return number == '0' or number == '1' or number == '2' or number == '3' or number == '4' or number == '5' or number == '6' or number == '7' or number == '8' or number == '9'
    return False

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
    # check if character is a number or symbol
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if number in nums:
        return True
    # return number == '0' or number == '1' or number == '2' or number == '3' or number == '4' or number == '5' or
    # number == '6' or number == '7' or number == '8' or number == '9'
    return False


def num_append(string):
    n = 0
    curr = ''  # current number string
    try:
        while Numbers(string[n]):
            curr += string[n]
            n += 1
    except:
        pass  # ignore
    return int(curr), n


def operator(symbol):
    operations = ['+', '-', '*']
    if symbol in operations:
        return True
    return False
    # return symbol == '+' or symbol == '-' or symbol == '*'


def operation(string, num1, num2):
    if string == '+':
        return num1 + num2  # defining operation functionality
    if string == '-':
        return num1 - num2
    if string == '*':
        return num1 * num2


def print_string(chars):
    print(chars + "=")


negated = False  # by default, the first string is not negative
string = input('')


while True:  # begin combing through the string
    try:
        if string[0] == '-':  # for negative numbers
            negated = True  # because here the numbers are in a string format
            string = string[1:]  # focus on rest of string
        number1 = num_append(string)[0]
        if negated:
            number1 = -number1
            negate = False
        end_number1 = num_append(string)[1]
        string = string[end_number1:]
        if string == '':
            print(number1)  # print result
            break
        sym = string[0]  # get the operation symbol
        string = string[1:]
        number2 = num_append(string)[0]
        end_number2 = num_append(string)[1]
        result = operation(sym, number1, number2)  # carry out functionality
        number1 = result  # obtain result of operation
        string = str(number1) + string[end_number2:]  # replace nums1 and nums2 with result to track accuracy
        print_string(string)  # print updated string
    except:
        break

"""

The app will interactively take a string representing a simple mathematical expression from the user
(e.g. “12435+34569-12345*10+50”).
After the user inputs the string, the app will check if the string represents a valid expression (no unexpected string characters, no duplicate operation characters, etc.).
After validating the expression, the app will output a string containing the result.
 In case of invalid expression, it should output an appropriate error message.
For simplicity, we will consider only addition, subtraction, and multiplication operations.
Also, we will only consider integers.
"""


def main():
    negated = False  # by default, the first string is not negative
    string = input('')
    string = string.replace("--", '+')
    string = multiples(string)
    for ch in string:
        if ch not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", " "]:
            print("Error: incorrect character.")
            return -1
    if string == "quit":
        return None
    elif string == "":
        print("Error - Please give a valid input")

    while True:  # begin combing through the string
        try:
            if string[0] == '-':  # for negative numbers
                negated = True  # because here the numbers are in a string format
                string = string[1:]  # focus on rest of string
            number1 = num_append(string)[0]
            if negated:
                number1 = -number1
                negated = False
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


def numbers(number):
    # check if character is a number or symbol
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if number in nums:
        return True

    return False


def num_append(string):
    n = 0
    curr = ''  # current number string
    try:
        while numbers(string[n]):
            curr += string[n]
            n += 1
    except:
        pass  # ignore
    return int(curr), n


# specifically handles multiplication
def multiples(string):
    symbol_index = string.find("*")

    # If there is no *' in the equation
    if symbol_index == -1:
        return string

    # Find the start of the multiplicand
    num2_start = symbol_index - 1
    while num2_start - 1 >= 0 and string[num2_start - 1].isdigit():
        num2_start -= 1
    if num2_start - 1 == 0 and string[num2_start - 1] == "-":
        num2_start -= 1

    # Calculate the multiplicand
    multiplicand = int(string[num2_start:symbol_index])

    # Find the end of the multiplier
    num1_end = symbol_index + 1
    if string[num1_end] == "-":
        num1_end += 1
    while num1_end < len(string) and string[num1_end].isdigit():
        num1_end += 1

    # Calculate the multiplier
    multiplier = int(string[symbol_index + 1:num1_end])

    #  Swap the part that was calculated with the answer
    return multiples(string[:num2_start]
                    + str(multiplicand * multiplier) + string[num1_end:])


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
    print(chars + "=") # shows the level by level breakdown on what's going on


if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod()

#Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.


def mul(a, b):
    ''' Function for multiplication of two numbers
        where a is first number and b is second number
        the operation is a*b'''
    return a*b

print(mul(45, 2.3))
help(mul)
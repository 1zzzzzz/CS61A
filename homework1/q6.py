"""
Write a one-line program that prints itself, using only the following features of the Python language:

    Number literals
    Assignment statements
    String literals that can be expressed using single or double quotes
    The arithmetic operators +, -, *, and /
    The built-in print function
    The built-in eval function, which evaluates a string as a Python expression
    The built-in repr function, which returns an expression that evaluates to its argument

"""

s = 'print("s = " + repr(s) + "; eval(s)")'; eval(s)


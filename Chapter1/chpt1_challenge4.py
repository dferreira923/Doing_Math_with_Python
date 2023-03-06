'''
Challenge 4

Write a calculator that can perform the basic mathematical operations on two fractions.
It should ask the user for two fractions and the operation the user wants to carry out.
'''

from fractions import Fraction


def add(a, b):
    print("Result of Addition: {0}".format(a + b))


def sub(a, b):
    print("Result of Subtraction: {0}".format(a - b))


def div(a, b):
    print("Result of Division: {0}".format(a / b))


def mult(a, b):
    print("Result of Multiplication: {0}".format(a * b))


if __name__ == '__main__':
    a = Fraction(input("Enter first fraction: "))
    b = Fraction(input("Enter second fraction: "))
    op = input("Operations to perform: Add, Subtract, Divide, Multiply: ").lower()
    if op == "add":
        add(a, b)
    if op == "subtract":
        sub(a, b)
    if op == "divide":
        div(a, b)
    if op == "multiply":
        mult(a, b)

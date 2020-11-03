"""
Apparently, this is how you do a multiline comment in python.
I wanted to give it a shot and thought I could try out the whole branching thing as well.
learned from geeksforgeeks.org
"""
'''
new stuff from geeksforgeeks.org
this is a 'Division(float) of number' whatever that means
and a 'modulo of both numbers'
I will be testing this today
'''
print("Choose first int:")
x = int(input())
print("Choose operator (+,-,*,/,//,%):")
print("/ = with decimal, // = without decimal. % = ramainder")
mode = input()
print("Choose second int:")
y = int(input())

print("Your result:")
if mode == "+":
    print(x+y)
elif mode == "-":
    print(x-y)
elif mode == "*":
    print(x*y)
elif mode == "/":
    print(x/y)
# 'Division(float) of number'
# this just gets ride of the decimal point
elif mode == "//":
    print(x//y)
# modulo of both numbers
# the gets the remainder
elif mode == "%":
    print(x%y)

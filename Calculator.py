"""
Apparently, this is how you dod a multiline comment in python.
I wanted to give it a shot and thought I could try out the whole branching thing as well.
learned from geeksforgeeks.org
"""
print("Choose first int:")
x = int(input())
print("Choose operator (+,-,*,/):")
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

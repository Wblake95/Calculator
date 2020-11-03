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

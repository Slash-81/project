actions = ["+", "-", "*", "/"]
arg1 = input("Enter the first number>>")
arg2 = input("Enter the second number>>")
action = input("Enter the action>>")

arg1 = int(arg1)
arg2 = int(arg2)

if action not in actions:
    print("Error")

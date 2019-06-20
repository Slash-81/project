actions = ["+", "-", "*", "/"]

arg1 = input("Enter the first number>> ")
arg2 = input("Enter the second number>> ")
action = input("Enter the action>> ")

try:
    if "." in arg1:
        arg1 = float(arg1)
    else:
        arg1 = int(arg1)
except ValueError:
    print ("Error arg1")
    exit(1)

try:
    if "." in arg2:
        arg2 = float(arg2)
    else:
        arg2 = int(arg2)

except ValueError:
    print ("Error arg1")
    exit(1)

if action not in actions:
    print("Error action")
    exit()

if action == "+":
    print(arg1+arg2)

elif action == "-":
    print(arg1-arg2)

elif action == "*":
    print(arg1*arg2)

elif action == "/":
    print(arg1/arg2)

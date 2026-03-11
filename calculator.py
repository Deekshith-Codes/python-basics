val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))
op = input("Enter an arithmetic operator: ")

if op == '+':
    print("Sum =", val1 + val2)

elif op == '-':
    print("Difference =", val1 - val2)

elif op == '*':
    print("Product =", val1 * val2)

elif op == '/':
    print("Quotient =", val1 / val2)

else:
    print("Invalid operator")

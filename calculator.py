#BEGINNING OF CALCULATOR


# 1) use if-statements to complete this calculator program with 4 operations
# Example run (what it should look like):
#       0 - add
#       1 - subract
#       2 - multiply
#       3 - divide
#   Enter a number to choose an operation:
#   1
#   Enter your first input: 10
#   Enter your second input: 4
#   10 - 4 = 6

# 2) add a fifth operation, power, that does a to the power of b
# 3) add a sixth operation, square root, that only asks for 1 input number and outputs its sqrt
# 4) seventh operation, factorial(a), one input
# 5) eighth operation, fibonacci(a), one input
# 6) talk to instructors when finished


print("  0 - add")
print("  1 - subtract")
print("  2 - multiply")
print("  3 - divide")
print("Enter a number to choose an operation: \n")

op =""
while op != "quit":
    op = int(input("Enter a number to choose an operation"))

    if op <=4:
        a = (input())
        b = (input())
    elif (op) <= 7:
        a = (input("Enter your first input: ")
    elif op == 0: #need to add
        print("a + b =",a+b)
    elif op == 1: #need to subtract
        print("a - b =",a-b)
    elif op == 2: #need to multiply
        print("a * b",a*b)
    elif op == 3: #need to divide
        print("a / b",a/b)
    elif op == 4: #need to power
        print()
        elif op == 5: #need to sqrt
        print("sqrt(a) ="a**(1/2))
    elif op == "6":
        i = 1
        factorial = 1
        while i < a+1:
        factorial = factorial * i
            i = i+1
        print("a-factorial is", factorial)

#END OF CALCULATOR
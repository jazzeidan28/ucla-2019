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
op = int(input())

a = int(input())
b = int(input())

item = ""
while item != "quit":
    print("Enter an item to check the price: ")
    item = input()

    if item == "pizza":
        print("$3 per slice")
    else:
        print("We don't have that.")
        
if op == 0: #need to add
    print("a + b =",a+b)
elif op == 1: #need to subtract
    print("a - b =",a-b)
elif op == 2: #need to multiply
    print("a * b",a*b)
elif op == 3: #need to divide
    print("a / b",a/b)





#END OF CALCULATOR
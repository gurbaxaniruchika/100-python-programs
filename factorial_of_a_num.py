num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial cannot be defined for negative number.")
else:
    for i in range(1, num+1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")
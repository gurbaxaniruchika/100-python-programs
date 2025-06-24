num1 = int(input("Enter the lower bound: "))
num2 = int(input("Enter the upper bound: "))

sum = 0
for i in range(num1, num2+1):
    sum += i
print(f"The sum in the given range is: {sum}")
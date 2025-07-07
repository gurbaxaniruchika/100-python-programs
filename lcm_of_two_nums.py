num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

lcm = 1

for i in range(max(num1, num2), (num1 * num2)+1):
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
print(f"LCM of {num1} and {num2} is {lcm}")
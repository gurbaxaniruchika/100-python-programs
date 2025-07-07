# same as hcf

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

gcd = 1

for i in range(1, min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print(f"The GCD of {num1} and {num2} is {gcd}")
num = int(input("Enter a number: "))

binary_value = num
decimal_value = 0
base = 1
while num > 0:
    rem = num % 10
    decimal_value = decimal_value + rem * base
    num = num // 10
    base = base * 2
print(f"The decimal conversion of binary number {binary_value} is {decimal_value}")
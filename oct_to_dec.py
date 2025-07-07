num = int(input("Enter a number: "))
octal_value = num

decimal_value = 0
base = 1

while num:
    rem = num % 10
    decimal_value = decimal_value + rem * base
    num = num // 10
    base = base * 8
print(f"The decimal conversion of octal number {octal_value} is {decimal_value}")
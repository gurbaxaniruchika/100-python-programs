def is_abundant(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum > num

number = int(input("Enter the number: "))
if is_abundant(number):
    print(f"{number} is an abundant number.")
else:
    print(f"{number} is not an abundant number.")
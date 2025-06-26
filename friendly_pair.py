def get_divisor_sum(num):
    total = 0
    for i in range(1, num+1):
        if num % i == 0:
            total += i
    return total

def is_friendly_pair(a, b):
    sum_a = get_divisor_sum(a)
    sum_b = get_divisor_sum(b)
    return (sum_a / a) == (sum_b / b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if is_friendly_pair(a, b):
    print(f"{a} and {b} are a friendly pair. ")
else:
     print(f"{a} and {b} are not a friendly pair. ")
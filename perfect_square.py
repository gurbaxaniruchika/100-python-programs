from math import sqrt

def is_perfect_square(num):
    if num > 0:
        sr = int(sqrt(num))
        return (sr * sr) == num
    return False

number = int(input("Enter the number: "))
if is_perfect_square(number):
    print(f"{number} is perfect square.")
else:
    print(f"{number} is not perfect square.")

import math

def findRoots(a, b, c):
    if a == 0:
        print("Invalid")
        return -1
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))
    if d > 0:
        print("The roots are real and different")
        print((- b + sqrt_val) / (2 * a))
        print((- b - sqrt_val) / (2 * a))
    elif d == 0:
        print("The roots are real and same")
        print(- b / (2 * a))
    else:
        print("The roots are complex")
        print(f"{- b / (2 * a)} + i {sqrt_val}")
        print(f"{- b / (2 * a)} - i {sqrt_val}")


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

findRoots(a, b, c)
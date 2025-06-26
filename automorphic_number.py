def is_automorphic(num):
    square = num * num
    return str(square).endswith(str(num))

number = int(input("Enter the number: "))
if is_automorphic(number):
    print(f"{number} is an automorphic number.")
else:
     print(f"{number} is not an automorphic number.")
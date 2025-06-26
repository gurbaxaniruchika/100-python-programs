def is_harshad(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return num % sum == 0

number = int(input("Enter a number: "))
if is_harshad(number):
    print(f"{number} is a harshad number.")
else:
    print(f"{number} is not a harshad number.")

 
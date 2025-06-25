num = int(input("Enter a number: "))
temp = num
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
print(f"The reverse is: {reverse}")



# using recursion

# def recursum(num, reverse):
#     if num == 0:
#         return reverse
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     return recursum(int(num/ 10), reverse)

# number = int(input("Enter the number: "))
# reverse = 0
# print(f"The reverse is: {recursum(number, reverse)}")
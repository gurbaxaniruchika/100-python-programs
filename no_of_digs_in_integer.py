def countDigit(num):
    digit = 0
    while num != 0:
        num = num // 10
        digit += 1
    return digit

number = int(input("Enter the number: "))
print(countDigit(number))
number = int(input("Enter the number: "))
num = number
digit = 0
sum = 0
length = len(str(num))

while num > 0:
    digit = int(num % 10)
    num = num / 10
    sum += pow(digit, length)

if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")
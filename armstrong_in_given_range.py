low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

for n in range(low, high + 1):
    order = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += pow(digit, order)
        temp = temp // 10

    if n == sum:
        print(n, end=" ") 
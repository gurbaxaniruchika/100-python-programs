def printDivisors(num):
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, end =" ")
        i += 1

number = int(input("Enter the number: "))
printDivisors(number)
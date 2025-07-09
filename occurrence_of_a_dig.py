def countOccurrences(num, digit):
    count = 0
    while num > 0:
        if num % 10 == digit:
            count += 1
        num //= 10
    return count

d = int(input("Enter the digit you want to count: "))
n = int(input("Enter the number: "))

print(f"The number of times {d} appear in {n} are: {countOccurrences(n, d)}")

def prime_factors(num):
    factors = []
    i = 2
    while i * i <= num:
        if num % i == 0:
            factors.append(i)
            num = num // i
        else:
            i += 1
    if num > 1:
        factors.append(num)
    return factors
    
number = int(input("Enter the number: "))
print(prime_factors(number))
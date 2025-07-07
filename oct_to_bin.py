def convert(octal):
    i = 0
    decimal = 0
    while octal != 0:
        digit = octal % 10
        decimal += digit * pow(8, i)
        octal //= 10
        i +=1
    print(f"Decimal value: {decimal}")
    binary = 0
    rem = 0
    i = 1
    while decimal != 0:
        rem = decimal % 2
        decimal //= 2
        binary += rem * i
        i = i * 10
    print(f"Binary value: {binary}")

octal = int(input("Octal value: "))
convert(octal)
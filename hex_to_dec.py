def convert(hex):
    l = len(hex)
    decimal = 0
    pos = 0
    for i in range(l-1, -1, -1):
        if '0' <= hex[i] <= '9':
            digit = int(hex[i])
            decimal = decimal + digit * pow(16, pos)
            pos = pos + 1
        elif 'A' <= hex[i] <= 'F':
            digit = ord(hex[i]) - 55
            decimal += digit * pow(16, pos)
            pos = pos + 1
    return decimal

hex = input("Enter the string: ").upper()
print(f"The decimal conversion of hexadecimal {hex} is: {convert(hex)}")
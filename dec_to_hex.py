decimal = int(input("Enter the number: "))
hex = []
while decimal > 0:
    rem = decimal % 16
    if rem < 10:
        hex.append(chr(rem + 48))
    else:
        hex.append(chr(rem + 55))
    decimal = decimal // 16

for i in reversed(hex):
    print(i, end="")

def convert(binary_str):
    while len(binary_str) % 3 != 0:
        binary_str = '0' + binary_str
    octal = []
    for i in range(0, len(binary_str), 3):
        group = binary_str[i:i+3]
        octal_digit = int(group, 2)
        octal.append(str(octal_digit))
    return "".join(octal)

binary_input = input("Enter a binary number (e.g., 1010): ").strip()
print(convert(binary_input))
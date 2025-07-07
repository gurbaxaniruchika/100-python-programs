decimal = int(input("Enter a number: "))
binary = []
while decimal > 0:
    r = decimal % 2
    binary.append(r)
    decimal = decimal // 2
for i in reversed(binary):
    print(i, end=" ")



# using function

# def convertBinary(num):
#     binaryArray = []
#     while num > 0:
#         binaryArray.append(num % 2)
#         num = num // 2
#     for bit in reversed(binaryArray):
#         print(bit, end= " ")

# decimal_num = int(input("Enter the number: "))
# convertBinary(decimal_num)
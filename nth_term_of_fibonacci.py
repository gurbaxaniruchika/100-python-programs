# 1 based indexing

num = int(input("Enter the number: "))
a, b = 0, 1

if num == 0:
    print(0)
elif num == 1:
    print(1)
else:
    for i in range(2, num):
        a, b = b, a + b
    print(b)
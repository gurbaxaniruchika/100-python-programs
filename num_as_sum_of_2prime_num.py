num = int(input("Enter the number: "))

arr = []

for i in range(2, num):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    if flag == 0:
        arr.append(i)

flag = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == num:
            flag = 1
            print(f"{str(arr[i])} and {str(arr[j])} are prime when added which give the number {str(num)}.")

if flag == 0:
    print(f"The number {str(num)} does not have two prime numbers which add up to it.")

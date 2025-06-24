low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

for i in range(low, high+1):
    if i == 1:
        continue
    for x in range(2, i):
        if i % x == 0:
            break
    else:
        print(i)
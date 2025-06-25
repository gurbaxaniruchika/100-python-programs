num = int(input("Enter the number of terms: "))

n1, n2 = 0, 1

if num <= 0:
    print("Please enter a positive integer.")
elif num == 1:
    print(f"Fibonacci series: {n1}")
else:
    print(f"Fibonacci series: {n1}, {n2}", end=", ")
    for i in range(2, num):
        n3 = n1 + n2
        print(n3, end=", " if i < num - 1 else "")
        n1, n2 = n2, n3
    print()


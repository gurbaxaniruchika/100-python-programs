# method 1: using Iteration

# arr = list(map(int, input("enter the elements: ").split()))
# sum = 0

# for i in range(len(arr)):
#     sum = sum + arr[i]

# print(sum) 

# method 2: using Recursion

# def getSum(arr, n):
#     if n == 0:
#         return 0
#     return arr[n-1] + getSum(arr, n-1)

# arr = list(map(int, input("Enter the elements: ").split()))
# print(getSum(arr, len(arr)))

# method 3: using inbuilt function

arr = list(map(int, input("Enter the elements: ").split()))

print(sum(arr))
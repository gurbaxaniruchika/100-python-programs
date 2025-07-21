# method 1: using two loops

# import math

# arr = list(map(int, input("Enter the elements: ").split()))
# first = math.inf
# second = math.inf

# for i in range(len(arr)):
#     if arr[i] < first:
#         first = arr[i]

# for i in range(len(arr)):
#     if arr[i] != first and arr[i] < second:
#         second = arr[i]

# print(second)

# method 2: using sort() function

arr = list(map(int, input("Enter the elements: ").split()))
arr.sort()
print(arr[1])
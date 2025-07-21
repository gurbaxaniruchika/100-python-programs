# method 1: using Iteration


# arr = list(map(int, input("enter the elements: ").split()))
# min = arr[0]

# for i in range(len(arr)):
#     if arr[i] < min:
#         min = arr[i]

# print(min)

# method 2: using sorting

# arr = list(map(int, input("Enter the elements: ").split()))

# arr.sort()

# print(arr[0])


# method 3: using min() function

arr = list(map(int, input("Enter the elements: ").split()))
print(min(arr))
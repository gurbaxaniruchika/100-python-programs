# method 1: using iteration

# arr = list(map(int, input("Enter the elements: ").split()))
# mini = arr[0]
# maxi = arr[0]

# for i in range(len(arr)):
#     if arr[i] < mini:
#         mini = arr[i]

#     if arr[i] > maxi:
#         maxi = arr[i]

# print(mini)
# print(maxi)

# method 2: using sort() function

# arr = list(map(int, input("Enter the elements: ").split()))
# arr.sort()

# print(arr[0])
# print(arr[-1])

# method 3: suing max() and min() function

arr = list(map(int, input("Enter the elements: ").split()))

print(max(arr))
print(min(arr))
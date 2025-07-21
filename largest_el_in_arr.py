# method 1: using iteration

# arr = [10, 89, 9, 56, 4, 80, 8]
# max_element = arr[0]

# for i in range(len(arr)):
#     if arr[i] > max_element:
#         max_element = arr[i]

# print(max_element)

# method 2: using max() function

# arr = list(map(int, input("Enter the elements: ").split()))

# max_element = arr[0]

# for i in range(len(arr)):
#     if arr[i] > max_element:
#         max_element = arr[i]

# print(max_element)


# method 3: using sort() function

arr = list(map(int, input("Enter the elements: ").split()))
print(max(arr))
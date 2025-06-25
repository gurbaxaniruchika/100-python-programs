def checkPalindrome(str):
    for i in range(0, len(str)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

string = input("Enter the sring: ")

if checkPalindrome(string):
    print("It's a palindrome") 
else:
    print("It's not a palindrome") 







# num = int(input("Enter a number: "))
# temp = num
# reverse = 0

# while num > 0:
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10

# print(reverse)
# if temp == reverse:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")
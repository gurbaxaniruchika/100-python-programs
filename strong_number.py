def is_stron_number(num):
    def factorial(n):
        result = 1
        for i in range(2, n+1):
            result = result * i
        return result
    sum_of_factorial = 0
    for digit in str(num):
        sum_of_factorial += factorial(int(digit))
    return sum_of_factorial == num

number = int(input("Enter the number: "))
if is_stron_number(number):
    print(f"{number} is a strong number.")
else:
    print(f"{number} is not a strong number.")
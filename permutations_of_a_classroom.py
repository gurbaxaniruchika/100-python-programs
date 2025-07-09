def factorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact

people = int(input("Enter the number of people: "))
seats = int(input("Enter the number of seats: "))

permutation = factorial(people) // factorial(people - seats)
print(permutation)

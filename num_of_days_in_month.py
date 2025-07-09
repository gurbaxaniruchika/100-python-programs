month = int(input("Enter month: "))
year = int(input("Enter the year: "))

if year % 400 == 0 and (year % 100 != 0 or year % 4 == 0):
    print("Number of days is 29")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("Number of days is 31")
else:
    print("Number of days is 30")
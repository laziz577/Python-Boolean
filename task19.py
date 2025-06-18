year = int(input("Enter year:"))

result = year % 4 == 0 or year % 100 == 0
print(result)

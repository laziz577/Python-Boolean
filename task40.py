correct_pin = "1234"
pin = input("Enter pin kod:")

result = pin != correct_pin or len(pin) != 4
print(result)

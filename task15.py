from getpass import getpass
pasword = getpass("Password:")
confirm = getpass("Confirm Password:")

result = pasword == confirm

print(result)

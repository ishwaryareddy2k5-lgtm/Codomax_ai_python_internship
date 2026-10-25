password = input("Enter a sample password: ")

if (len(password) >= 8
    and any(c.isalpha() for c in password)
    and any(c.isdigit() for c in password)):
    print("Basic checks passed")
else:
    print("Use at least 8 characters, including letters and digits")

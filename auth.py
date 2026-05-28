def login():

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login successful!")
        return True

    else:
        print("Invalid username or password")
        return False
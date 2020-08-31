def checkPassword(password):
    # Flags for checking if a password is strong:
    # Minimum 8 characters length
    # Contains 3/4 of the following items: 
    #   - Uppercase letters, Lowercase letters, numbers or symbols.
    counter = 0
    items = []
    secure = False
    
    if len(password) < 8:
        secure = True
    else:
        for x in password:
            if x.isupper():
                items.append("Upper")
            if x.islower():
                items.append("Lower")
            if x.isnumeric():
                items.append("Numeric")
    
    items = list(dict.fromkeys(items))
    print(len(items))


def menu():
    out = False
    while out != True:
        print("\n---- OPTION MENU ----")
        print("1. Check if a password is secure.")
        print("2. Crack passwords.")
        print("3. Stop.\n")
        option = int(input("Please choose an option: "))
        if option == 1:
            password = input("Please enter your password: ")
            checkPassword(password)
            break
        if option == 3:
            out = True

menu()


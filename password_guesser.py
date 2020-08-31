def checkPassword(password):
    # Flags for checking if a password is strong:
    # Minimum 8 characters length
    # Contains 3/4 of the following items: 
    #   - Uppercase letters, Lowercase letters, numbers or symbols.
    counter = 0
    items = []
    secure = True
    
    if len(password) < 8:
        secure = False
    else:
        for x in password:
            if x.isupper():
                items.append("Upper")
            if x.islower():
                items.append("Lower")
            if x.isnumeric():
                items.append("Numeric")
    
    items = list(dict.fromkeys(items))
    
    if secure != False:
        if len(items) >= 3:
            print("Your password is secure!")
        else:
            print("Your password is not secure!")


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


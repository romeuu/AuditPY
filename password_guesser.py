def menu():
    out = False
    while out != True:
        print("\n---- OPTION MENU ----")
        print("1. Check if a password is secure.")
        print("2. Crack passwords.")
        print("3. Stop.\n")
        option = int(input("Please choose an option: "))
        if option == 1:
            
            break
        if option == 3:
            out = True

password = input("Please enter your password: ")

menu()


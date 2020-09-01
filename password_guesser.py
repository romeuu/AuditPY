import re, random, string
def checkPassword(password):
    # Flags for checking if a password is strong:
    # Minimum 8 characters length
    # Contains 3/4 of the following items: 
    #   - Uppercase letters, Lowercase letters, numbers or symbols.
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

def crackPasswords(name, birth, city):

    matched = re.match("[0-9]{8}", birth)
    is_match = bool(matched)

    if is_match != True:
        print("Birth date is not correctly formatted, skipping this parameter...")


def securePasswords(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
            
def menu():
    out = False
    while out != True:
        print("\n---- OPTION MENU ----")
        print("1. Check if a password is secure.")
        print("2. Crack passwords.")
        print("3. Generate a list of secure passwords.")
        print("4. Stop.\n")
        option = int(input("Please choose an option: "))
        if option == 1:
            password = input("Please enter your password: ")
            checkPassword(password)
            break
        if option == 2:
            name = input("Please enter the target name: ")
            birth = input("Enter the target birth: (DDMMYYYY) ")
            city = input("Enter the city/village of the target: ")

            crackPasswords(name, birth, city)
            break
        if option == 3:
            length = int(input("Please enter the length of your desired password: "))
            for x in range(0,20):
                print(securePasswords(length))
            break

        if option == 4:
            out = True

menu()


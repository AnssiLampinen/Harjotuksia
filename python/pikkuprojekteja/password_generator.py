i = 1

passwords = []

while i > 0:
    uip = input("\nTo save new password press 1 \nTo access you passwords press 2 \n")
    if uip == "1":
        site = input("What site are you on? ")
        if passwords.count(site) > 0:
            input("You already have saved a password for this site. ")
        else:
            username = input("what is your username? ")
            password = input("What is your password? ")
            passwords.append(site)
            passwords.append(username)
            passwords.append(password)    
    elif uip == "2":    
        uip = input("What site are you trying to log in? ")
        if passwords.count(uip) > 0:
            index = passwords.index(uip)
            print("username: " + passwords[index + 1])
            print("password: " + passwords[index + 2])
        else:
            input("Seems like you haven't saved login information for this site. ")
    else:
        input("That wasn't an option.")
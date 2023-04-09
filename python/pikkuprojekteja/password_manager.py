passwords = {}

def add():
    site = input("What site are you on?\n")
    if bool(passwords.get(site)) == False:
        username = input("what is your username?\n")
        password = input("What is your password?\n")
        passwords[site] = {
            "username": username,
            "password": password
        }
    else:
        uip = input("Seems like you already have saved login information for this site.\nDo you want to change something?\n1 to change username\n2 to change password\n3 to change both\nENTER to continue without changing\n")
        if uip == "1":
            username = input("What is your new username?\n")
            passwords[site]["username"] = username
        elif uip == "2":
            password = input("what is your new password?\n")
            passwords[site]["password"] = password
        elif uip == "3":
            username = input("What is your new username?\n")
            password = input("what is your new password?\n")
            passwords[site] = {
                "username": username,
                "password": password
            }

def retrieve(site = None):
    if site == None:
        site = input("What site are you trying to log in?\n")
    if bool(passwords.get(site)):
        credentials = passwords[site]
        print("username: " + credentials["username"])
        print("password: " + credentials["password"])
    else:
        uip = input("Seems like you don't have login info for this site.\n")


def delete():
    site = input("What login info do you want to delete?\n")
    confirm = input("Type CONFIRM to confirm the deletion.\n")
    if confirm == "CONFIRM":
        del passwords[site]
        input("Credentials deleted.\n")
    else:
        input("Credentials not deleted.\n")



while True:
    uip = input("\nTo save new password press 1 \nTo access you passwords press 2 \nTo delete existing credentials 3\n")
    if uip == "1":
        add()
    elif uip == "2":
        retrieve()
    elif uip == "3":
        delete()
    else:
        input("That wasn't an option.\n")

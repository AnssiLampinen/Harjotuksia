input("Pick a number between 0 and 999. I'm going to try to guess your number,\nif my guess is too high type H, \if my guess is too low type L\nand if it's correct type C. Type OK to continue! ")
result = False
top = 999
bot = 0
guess = 500


while result == False:
    user_input = input("Is your number {}? ".format(guess)).upper()

    if user_input == "C":
        input("I WIN!!!")
        result = True
    elif user_input == "H":
        bot = guess
        guess = round((guess + top + 1)/2)
    elif user_input == "L":
        top = guess - 1
        guess = round((guess + bot)/2)
    else:
        user_input = input("That wasn't an option... ")
        

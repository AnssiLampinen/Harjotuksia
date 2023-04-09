import random
from words import words
word = "debendent".upper()
guessed = "_ _ _"
i = 10


while True:
    n = random.randint(0, 2642)
    word = words[n].upper()
    word_lenght = len(word)
    word = list(word)
    guessed = list(word)
    for i in range(0, word_lenght):
        guessed[i] = "_"
    showing = ' '.join(guessed)
    print(showing)


    while i > 0:
        user_input = input("\nGuess a letter! ").upper()
        letter_count = int(word.count(user_input))
        while letter_count > 0:
            index = word.index(user_input)
            guessed[index] = user_input
            word[index] = "_"
            letter_count = letter_count - 1
        showing = ' '.join(guessed)
        print("\n" + showing)
        i = guessed.count("_")


    input("\n" + "YOU WIN!!!")
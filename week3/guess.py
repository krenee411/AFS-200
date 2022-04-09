# secret_word = "MORBID"
# guessed_letter = ""
# guess_count = 6


# print("Can you guess this popular podcast name?")
# print("You get six guesses")
# guessed_letter = input("\n Guess a letter! ").capitalize()

# print(guessed_letter)

# def wordBoard(mask, secret_word):
#     print(len(secret_word)*mask)

# print(wordBoard('_ ', secret_word))

# def checkGuess(guessed_letter):
#     count = 6   
#     while count < 6:
#         if guessed_letter in secret_word:
#             letter = secret_word.find(guessed_letter)
#             wordBoard = wordBoard[:letter] + guessed_letter + wordBoard[letter + 1:]
#             wordBoard.appenend(guessed_letter)
#             print("Great job!")
#             count += 1
#         elif guessed_letter not in secret_word:
#             print("Good try but thats the wrong letter")
#             count -= 1

# print(checkGuess(guessed_letter=))

secret_word = "MORBID"
guessed_letter = ""
correct_guess = []
userGuesses= 6

print("Can you guess this popular podcast name?")
print("You get six guesses")


def wordBoard():
    blanks = "_ " * len(secret_word)
    checkGuess(blanks, secret_word)


def checkGuess(blanks, guessed_letter):
    print("Word: ",blanks * len(secret_word))
    userGuesses= 6
    while userGuesses != 0 :
        userGuesses -= 1
        guessed_letter = input("Guess a letter: ").capitalize()
        if guessed_letter in secret_word :
            newBlanks= "".join(c if c in guessed_letter else "_ " for c in secret_word)
            index = 0
            for letter in newBlanks:
                # I can not figuer out how to get the correct_guess to stay in the next line so the
                # player can keep guessing? 
                if letter != "_" and letter != " ":
                    blanks = blanks[:index] + letter + blanks[index +1:] 
                    correct_guess.append(letter) 
                    index += 1
            print("Correct")
            print(correct_guess)
            print("Word: ", newBlanks)
        
        else: 
            print("Sorry that letter is not in the secret word.")
             

checkGuess("_ ", guessed_letter)


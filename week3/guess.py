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


secret_word = 'MORBID'
guess = []
userGuesses= 6
wordBoard = ['_','_','_','_','_','_']
alive = True

print("Can you guess this popular podcast name?")
print("You get six guesses")


def showBoard():
    while alive:
        print(wordBoard)
        guessed_letter = input("Guess a letter: ").capitalize()
        
        if len(guessed_letter) > 1 or guessed_letter.isnumeric():
                print("Please enter a single letter")
        else:
            checkGuess(guessed_letter)

def addLetter(guessed_letter):
    for i in range(len(secret_word)):
        if secret_word[i] == guessed_letter:
            wordBoard[i] = guessed_letter

def checkGuess(guessed_letter):
    global userGuesses
    global alive
    if userGuesses != 0 :
        userGuesses -= 1
        if guessed_letter in secret_word: 
            if guessed_letter in guess :
                print('you hav already guessed that letter. Try again!') 
            else:
                addLetter(guessed_letter)
                guess.append(guessed_letter)
                print(f"Correct there is a {guessed_letter} in the secret word!")
                print(f"you have {userGuesses} left")
        else:
            if guessed_letter in guess:
                print('you hav already guessed that letter. Try again!') 
            else:
                print(f"Sorry there is no {guessed_letter} in the secret word.")
                print(f"you have {userGuesses} left")
        if userGuesses == 1:
            print("do you think you can guess the word?")
            print(wordBoard)
            final_answer = input().upper()
            if final_answer == secret_word:
                print("Congratulations!! You guessed the secret word!!")
                alive = False
            else:
                alive = False
                print("Sorry you are out of lives and you did not guess the secret word")
                print(f"The secret word was {secret_word}")
showBoard()
# Prompt the user to enter a word
# and assign it to the userWord variable
wordWithoutVowels = ""

userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        wordWithoutVowels += letter

# Print the word assigned to wordWithoutVowels.
print(wordWithoutVowels)

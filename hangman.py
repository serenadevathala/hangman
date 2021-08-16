import random

wordBank = ["Texas", "California", "Maine", "Connecticut", "Florida", "devathala"]

wordIndex = random.randrange(0, len(wordBank)-1 , 1)

word= wordBank[wordIndex]

i=0
dash = []
while i < len(word):
    dash.append("_")
    i+=1

num = 6
letter = " "
while num > 0:
    letter = raw_input("Guess a letter: ")
    if letter in word and len(letter)==1:
        index=0
        while index < len(word):
            if word[index] == letter:
                dash[index] = letter
                index += 1
            else:
                index +=1
        print(dash[0:])
        if "_" not in dash:
            print("Congrats you've guessed the word.")
            quit()
    else:
          num = num-1
          print("You have " + str(num) + " tries left")


userGuess = raw_input("You've run out of tries. Guess word.")
if userGuess == word:
    print("Congrats you've guess the word!!")
else:
    print("Sorry. You lost hangman")


    #letterIndex = word.index(letter)
    #dash[letterIndex] = letter
    #print(dash[0:])

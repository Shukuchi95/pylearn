import random

word_list = ["eagle", "frame", "piano", "apple", "cloud", "brown", "birth", "court", "anger", "abuse", "Acute",  "Alive",  "Alone",  "Angry",  "Aware",  "Awful",  "Basic",  "Black",  "Blind",  "Brave",  "Brief",  "Broad",  "Brown",  "Cheap",  "Chief",  "Civil",  "Clean",  "Clear",  "Close",  "Crazy",  "Daily",  "Dirty",  "Early",  "Empty",  "Equal",  "Exact",  "Extra",  "Faint",  "Final",  "First",  "Fresh",  "Front",  "Funny",  "Giant",  "Grand",  "Great",  "Green",  "Gross",  "Happy",  "Harsh",  "Heavy",  "Human",  "Ideal",  "Inner",  "Joint",  "Large",  "Legal",  "Level",  "Light",  "Local",  "Loose",  "Lucky",  "Magic",  "Major",  "Minor",  "Moral",  "Naked",  "Nasty",  "Naval",  "Other",  "Outer",  "Plain",  "Prime",  "Prior",  "Proud",  "Quick",  "Quiet",  "Rapid",  "Ready",  "Right",  "Roman",  "Rough",  "Round",  "Royal",  "Rural",  "Sharp",  "Sheer",  "Short",  "Silly",  "Sixth",  "Small",  "Smart",  "Solid",  "Sorry",  "Spare",  "Steep",  "Still",  "Super",  "Sweet",  "Thick",  "Third",  "Tight",  "Total",  "Tough",  "Upper",  "Upset",  "Urban",  "Usual",  "Vague",  "Valid",  "Vital",  "White",  "Whole",  "Wrong",  "Young",]
userfacingword = ["*", "*", "*", "*", "*"]  # will be populated as user guesses correctly,(inside loop??)
guesscount = 0
badguesses = []
allguesses = []
random_word = random.choice(word_list).lower()  # should this be inside while loop or outside?
correctguesscount = 0
def printboard(guesses):
    if guesses == 0:
        print ("_________")
        print ("|	 |")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif guesses == 1:
        print ("_________")
        print ("|	 |")
        print ("|    0")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif guesses == 2:
        print ("_________")
        print ("|	 |")
        print ("|    0")
        print ("|    |")
        print ("|    |")
        print ("|")
        print ("|________")
    elif guesses == 3:
        print ("_________")
        print ("|	 |")
        print ("|    0")
        print ("|   \|")
        print ("|    |")
        print ("|")
        print ("|________")
    elif guesses == 4:
        print ("_________")
        print ("|	 |")
        print ("|    0")
        print ("|   \|/")
        print ("|    |")
        print ("|")
        print ("|________")
    elif guesses == 5:
        print ("_________")
        print ("|	 |")
        print ("|    0")
        print ("|   \|/")
        print ("|    |")
        print ("|   /")
        print ("|________")
    elif guesses == 6:
        print ("_________")
        print ("|	 |")
        print ("|    0")
        print ("|   \|/")
        print ("|    |")
        print ("|   / \ ")
        print ("|________")   # this is the board

while guesscount <6 and correctguesscount != 5:
    printboard(guesscount) # print the board
    print(" ".join(userfacingword)) # print the word the user can see
    print("You have guessed: " + ", ".join(badguesses))
    guessedletter = input("guess a letter: ") # ask user for letter
    if guessedletter == "":
        while guessedletter =="":
            guessedletter = input("guess a non blank letter please: ")
    elif guessedletter in badguesses:
        while guessedletter in badguesses:
            print("You have guessed: " + ", ".join(badguesses))
            guessedletter = input("input unique letter: ")
    else:
        badguesses.append(guessedletter)
    if guessedletter in random_word:
        if random_word.index(guessedletter) != random_word.rindex(guessedletter):
            userfacingword[(random_word.index(guessedletter))] = guessedletter
            userfacingword[(random_word.rindex(guessedletter))] = guessedletter
            correctguesscount += 2
            print("Well done! ")
        else:
            userfacingword[(random_word.index(guessedletter))] = guessedletter
            correctguesscount += 1
            print("Well done !")
    if guessedletter not in random_word:
        guesscount +=1
        print("sorry! letter not in word.")
if correctguesscount == 5:
    printboard(guesscount)
    print(" ".join(userfacingword))
    print("Well done, you win ! The word was " + random_word)
if guesscount == 6:
    printboard(6)
    print(" you are out of guesses! the word was " + random_word)









#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# IN THE NAME OF GOD

import random
import math

animals=["cat","dog","lion","tiger","elephant","octopus","dolphin","shark","eagle","frog"]
fruits=["apple","bnana","orange","strawberry","grape","watermelon","pineapple","mango","peach","cherry"]
countries=["iran","japan","canada","france","italy","spain","china","brazil","germany","america"]
politician=["Vladimier Putin","Xi Jinping","Ali Khamenei","Qasem Soleimani","Benjamin Netanyahu","George W.Bush","Emmanuel Macron","Pedro Sanchez","Charles","Justin Trudeau"]

all_lists=[]
all_lists.extend(animals)
all_lists.extend(fruits)
all_lists.extend(countries)
all_lists.extend(politician)


# Choose category and get a random word from it
def choose_category():
    while True:
        try:
            number=int(input("Enter your choice: "))

            match number:
                case 1:
                    return random.choice(animals)
                case 2:
                    return random.choice(fruits)
                case 3:
                    return random.choice(countries)
                case 4:
                    return random.choice(politician)
                case 5:
                    return random.choice(all_lists)
                case _:
                    print("choose a natural number between 1 and 5!")

        except ValueError:
            print("Just enter a number! ")


# Choose difficulty and return number of lives
def difficulty_level():
    while True:
        try:
            number=int(input("Enter your choice: "))

            match number:
                case 1:
                    return 8
                case 2:
                    return 6
                case 3:
                    return 4
                case _:
                    print("choose a natural number between 1 and 3!")

        except ValueError:
            print("Just enter a number! ")


# Get a single valid letter from the user
def get_letter(guessed_letters):
    while True:
        letter=input("Guess a letter: ").lower()

        if len(letter)!=1:
            print("Enter only ONE letter! ")
            continue

        if not letter.isalpha():
            print("Enter only a letter, not a number or symbol! ")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter! ")
            continue

        return letter


# Show the word with guessed letters revealed
def show_word(secret_word,guessed_letters):
    displayed=""
    for letter in secret_word:
        if letter.lower() in guessed_letters:
            displayed+=letter+" "
        elif letter==" ":
            displayed+="  "
        else:
            displayed+="_ "
    print(displayed)


# Draw the hangman for easy mode (8 mistakes allowed)
def draw_hangman_easy(mistakes):
    match mistakes:
        case 0:
            print("""
        ___________




         """)
        case 1:
            print("""
        ___________



           \\
         """)
        case 2:
            print("""
        ___________



         / \\
         """)
        case 3:
            print("""
        ___________


           \\
         / \\
         """)
        case 4:
            print("""
        ___________


          |\\
         / \\
         """)
        case 5:
            print("""
        ___________


         /|\\
         / \\
         """)
        case 6:
            print("""
        ___________

        (O_O)
         /|\\
         / \\
         """)
        case 7:
            print("""
        ___________
          |

        (O_O)
         /|\\
         / \\
         """)
        case _:
            print("""
        ___________
          |
          |
        (*_*)
         /|\\
         / \\
         """)


# Draw the hangman for normal mode (6 mistakes allowed)
def draw_hangman_normal(mistakes):
    match mistakes:
        case 0:
            print("""
        ___________




         """)
        case 1:
            print("""
        ___________



           \\
         """)
        case 2:
            print("""
        ___________



         / \\
         """)
        case 3:
            print("""
        ___________


           \\
         / \\
         """)
        case 4:
            print("""
        ___________


         /|\\
         / \\
         """)
        case 5:
            print("""
        ___________

        (O_O)
         /|\\
         / \\
         """)
        case _:
            print("""
        ___________
          |
          |
        (*_*)
         /|\\
         / \\
         """)


# Draw the hangman for hard mode (4 mistakes allowed)
def draw_hangman_hard(mistakes):
    match mistakes:
        case 0:
            print("""
        ___________




         """)
        case 1:
            print("""
        ___________



         / \\
         """)
        case 2:
            print("""
        ___________


         /|\\
         / \\
         """)
        case 3:
            print("""
        ___________

        (O_O)
         /|\\
         / \\
         """)
        case _:
            print("""
        ___________
          |
          |
        (*_*)
         /|\\
         / \\
         """)


print("""==== HANGMAN GAME====
 Choose a category:

 1. Animals
 2. Fruits
 3. Countries
 4. politician
 5. All of them""")
secret_word=choose_category()

print("""What defficulty level do you want? (Pick a number!)
1. Easy
2. Normal
3. Hard""")
lives=difficulty_level()
max_lives=lives

match max_lives:
    case 8:
        draw_hangman=draw_hangman_easy
    case 6:
        draw_hangman=draw_hangman_normal
    case 4:
        draw_hangman=draw_hangman_hard

print(f"Your word has {len(secret_word)} letters! ")

guessed_letters=[]
won=False

while lives>0:

    mistakes=max_lives-lives
    draw_hangman(mistakes)

    show_word(secret_word,guessed_letters)
    print(f"Lives left: {lives}")

    letter=get_letter(guessed_letters)
    guessed_letters.append(letter)

    if letter in secret_word.lower():
        print("Nice one! That letter is in the word! ")
    else:
        lives-=1
        print("Nope! That letter is not in the word! ")

    won=True
    for c in secret_word.lower():
        if c!=" " and c not in guessed_letters:
            won=False

    if won:
        break

print("")
mistakes=max_lives-lives
draw_hangman(mistakes)

if won:
    show_word(secret_word,guessed_letters)
    print(f"You won! The word was: {secret_word}")
else:
    print(f"You lost! The word was: {secret_word}")


# In[ ]:





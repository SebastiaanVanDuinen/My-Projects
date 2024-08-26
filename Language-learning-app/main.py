# This is a language learning app where flash cards are shown. You need to think of the translated word which will be shown after 2 seconds. If you are correct, you press the green checkmark, if you were incorrect you press the red X. Every time you get a card correct it is taken out of the deck, forcing you to repeat the ones you didn't get correct until you get them correct.
#
# There are 4 levels, beginner, medium, hard and expert. At the start of the app you need to select which difficulty level you take.
#
#
# I scraped the 100 most common used words for each available language in order to be able to quickly pick up the langauge if you were ever to visit the country.
#
# In arabic there are grammar symbols that can tell you how to pronounce a word, but they are not written down in commonly used arabic. As such, I thought it was nice to implement an actual voice to say the word out loud to help with understanding which word is being meant as there is no context.
#
# In order for the voice to actually say the words out loud, the voice language has to be installed first. I did not know how to properly do this so I used Puneet Singh's solution: https://puneet166.medium.com/how-to-added-more-speakers-and-voices-in-pyttsx3-offline-text-to-speech-812c83d14c13
#
# Then I used pyttsx3 to read the text out loud via text to speech.
#
#
# ------ TO BE ADDED -----
#
# The languages French, German, Spanish and Italian are to be added soon.


from tkinter import *
from tkinter import messagebox
import json
import random
from Data import load_words
import pandas as pd
import pyttsx3

def language_check():
    language_choice = input("What language would you like to practice?: [A]rabic, [D]utch, [F]rance: ")
    if language_choice == 'a':
        language = "Arabic"
    elif language_choice == 'd':
        language = "Dutch"
    elif language_choice == 'f':
        language = "French"
    else:
        print("Type the letter between the brackets to indicate the language you'd like to learn.")
        language_check()
    return language

def difficulty_check():
    amount_of_cards = 0
    while amount_of_cards == 0:
        difficulty = input(
        "What difficulty level do you want?: type [B]eginner for 25 cards, [M]edium for 50 cards, [H]ard for 75 cards and [E]xpert for 100 cards: ").lower()
        if difficulty == "b":
            amount_of_cards = 25
        elif difficulty == 'm':
            amount_of_cards = 50
        elif difficulty == "h":
            amount_of_cards = 75
        elif difficulty == "e":
            amount_of_cards = 100
        else:
            print("Type the letter between the brackets to indicate difficulty level please.")
    return amount_of_cards
# Reading the words used in the cards
def read_data():
    with open("Data/AR_top100.json", "r") as data_file:
        data = json.load(data_file)
        #new_data = [(b, c) for (a, b, c) in data] #arabic reads from right to left, hence (b,c) instead of (a,b)
    return data


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(card_title, text="Arabic", fill="black")
    canvas.itemconfig(card_word, text=current_card[0], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    engine.say(current_card[0])
    engine.runAndWait()
    flip_timer = window.after(3000, flip_card) #giing the player 3 seconds to give the answer


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card[1], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    data.remove(current_card)
    with open("Data/words_to_learn.txt", "w") as data_file:
        json.dump(data, data_file)
    print(len(data))
    next_card()


#Selecting and initiating the right voice for tts

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)



# Creating the background, canvas, the cards and the buttons

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)



#loading in the words and starting the game:

#load_words.get_arab_words()
word_list = difficulty_check()
data = read_data()[0:word_list]
next_card()


window.mainloop()


# TODO:
#   Completed -- Multiple difficulty levels (25-50-75-100 words)
#       Multiple languages to choose from: (Arabic, Dutch, French)
#       Score for correct answers vs incorrect answers
#       A background timer to see how quickly you finished the level,
#       With more than 5 saved background timers, a plot that shows how much you've improved.
#       Multiple categories

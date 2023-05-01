from tkinter import *
import pandas as pd
from random import randint


STUDY_LANG = "Italian"
NATIVE_LANG = "English"
WORDS_FILE = "it_flashcards.csv"
LEARN_FILE = f"words_to_learn_{STUDY_LANG}.csv"
idx = 0

# DATA
# try: # TODO Bring up words to learn instead of main file, remove from csv, and go back to words to learn
#     df = pd.read_csv(LEARN_FILE)
# except FileNotFoundError:
#     df = pd.read_csv(WORDS_FILE)
# finally:
#     data_dict = {key: value for (key, value) in df.iterrows()}

df = pd.read_csv(WORDS_FILE)
data_dict = {key: value for (key, value) in df.iterrows()}


# RANDOM WORD
def flip_card():
    global idx
    translated_word = data_dict[idx][NATIVE_LANG].lower()
    canvas.itemconfig(tagOrId=flashcard, image=back_img)
    canvas.itemconfig(tagOrId=lang_lbl, text=NATIVE_LANG, fill="white")
    canvas.itemconfig(tagOrId=word_lbl, text=translated_word, fill="white")


def next_word():
    global idx
    idx = randint(0, len(data_dict) - 1)
    word = data_dict[idx][STUDY_LANG].lower()
    canvas.itemconfig(tagOrId=flashcard, image=front_img)
    canvas.itemconfig(tagOrId=lang_lbl, text=STUDY_LANG, fill="black")
    canvas.itemconfig(tagOrId=word_lbl, text=word, fill="black")
    window.after(3000, flip_card)


def next_word_wrong():
    global idx
    study_word = data_dict[idx][STUDY_LANG]
    native_word = data_dict[idx][NATIVE_LANG]
    new_dict = {
        STUDY_LANG: [study_word],
        NATIVE_LANG: [native_word],
    }
    new_df = pd.DataFrame(new_dict)
    try:
        file = open(file=LEARN_FILE, mode="r")
    except FileNotFoundError:
        new_df.to_csv(LEARN_FILE, mode="a", index=False)
    else:
        file.close()
        new_df.to_csv(LEARN_FILE, mode="a", index=False, header=False)
    next_word()


# UI
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)
window.title("PyFlash")

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
flashcard = canvas.create_image(400, 265, image=front_img)
lang_lbl = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_lbl = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_word_wrong)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=next_word)
right_btn.grid(row=1, column=1)

next_word()

window.mainloop()

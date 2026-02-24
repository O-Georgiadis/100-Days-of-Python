from pathlib import Path
from tkinter import * 
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"
current_card = {}
to_learn = {}


#----------------Take the first 500 words from the 50K words---------------#
# with open(Path(__file__).parent/"de_50K.txt", "r") as infile, open(Path(__file__).parent/"de_500.txt", "w") as outfile:
#     for i, line in enumerate(infile):
#         if i >= 500:
#             break
#         outfile.write(line)


try:
    df = pd.read_csv(Path(__file__).parent/"data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pd.read_csv(Path(__file__).parent/"data/german_words.csv")
    to_learn = original_df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")




def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, flip_card)


    

def flip_card():
    canvas.itemconfig(card_title, text="Greek", fill="white")
    canvas.itemconfig(card_word, text=current_card["Greek"], fill="white")
    canvas.itemconfig(card_background, image=back_image)
    

        
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg="white", highlightthickness=0)
front_image = PhotoImage(file=str(IMAGE_DIR/ "card_front.png"))
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

back_image = PhotoImage(file=str(IMAGE_DIR/ "card_back.png"))



right_image = PhotoImage(file=str(IMAGE_DIR/ "right.png"))
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file=str(IMAGE_DIR/ "wrong.png"))
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()

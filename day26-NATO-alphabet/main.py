import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index,row) in df.iterrows()}

def generate_phoenetic():
    user_input = input("Enter a word: ").upper()
    try:
        user_output = [new_dict[letter] for letter in user_input]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phoenetic()

    else:
        print(user_output)


generate_phoenetic()
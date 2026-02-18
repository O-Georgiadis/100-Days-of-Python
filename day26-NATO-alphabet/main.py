df = pd.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index,row) in df.iterrows()}

user_input = input("Enter a word: ").upper()

user_output = [new_dict[letter] for letter in user_input]
print(user_output)

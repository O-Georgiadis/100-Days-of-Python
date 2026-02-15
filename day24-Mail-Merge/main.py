
with open("./Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()


with open("./Input/Letters/starting_letter.txt") as letter:
    readed = letter.read()
    for name in list_of_names:
        striped_name = name.strip() 
        new_letter = readed.replace("[name]", striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.docx", mode="w") as finished:
            finished.write(new_letter)

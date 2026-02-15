import random 
word_list = ["aardvak", "baboon", "camel"]

lives = 6

word = random.choice(word_list)
# print(word)

display = ""
placeholder = ""

for position in range(len(word)):
    placeholder += "_"

print(placeholder)

correct_letters = []
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    
    for letter in word:

        if letter == guess:
            display += letter
            if letter not in correct_letters:
                correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    if guess not in word:   
        lives -=1
        print("Lives: ", lives)
        if lives == 0:
            print("You lost!")
            print("the correct word was: ", word)
            game_over = True

    print(display)
    
    if "_" not in display:
        print("You win!")
        game_over = True
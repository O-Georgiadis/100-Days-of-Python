alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


game_over = False

def encoder(message, shift_position):
    encoded_message= ""
    for letter in message:
        if letter in alphabet:
            new_letter = (alphabet.index(letter) + shift_position) %26
            encoded_message += alphabet[new_letter]
        else:
            encoded_message += letter
    print(f"Here is the Encoded message: {encoded_message}")

def decoder(message, shift_position):
    decoded_message = ""
    for letter in message:
        if letter in alphabet:
            decoded_letter = (alphabet.index(letter) - shift_position) %26
            decoded_message += alphabet[decoded_letter]
        else:
            decoded_message += letter
    print(f"Here is the Decoded message: {decoded_message}")

while not game_over:
    action = input("Type 'encode' to encrypt, type 'decode to decrypt: ")
    message = input("Type your message: ").lower()
    shift_position = int(input("Type the shift number: "))

    if action == "encode":
        encoder(message, shift_position)
        

    elif action == "decode":
        decoder(message, shift_position)

    else:
        print("no valid input")
        pass

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if go_again == "no":
        game_over = True

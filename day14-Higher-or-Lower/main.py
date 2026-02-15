import random
# Missing real dictionary of things and their followers, using dummy data for testing
things = {"a":50, "b":30, "c":70, "d":20, "e":90}

print("Welcome to the Higher or Lower Game!")

def evaluate(guess, thing_a, thing_b):
    if guess == 'a' and things[thing_a] > things[thing_b]:
        return True
    elif guess == 'b' and things[thing_b] > things[thing_a]:
        return True
    else:
        return False


game_over = False
score = 0


thing_b = random.choice(list(things.keys()))

while not game_over:
    thing_a = thing_b
    thing_b = random.choice(list(things.keys()))
    if thing_a == thing_b:
        thing_b = random.choice(list(things.keys()))
    print(f"Compare A: {things[thing_a]}")
    print("vs")
    print(f"Compare B: {things[thing_b]}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    evaluate(guess, thing_a, thing_b)
    if evaluate(guess, thing_a, thing_b):
        score += 1
        print(f"You are right! Current score: {score}.")
    else:
        game_over = True
        print(f"Sorry that was wrong. Your final score is {score}.")

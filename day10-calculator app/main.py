
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

game_over = False


while not game_over:
    number1 = float(input("What is the first number?: "))
    for symbol in operators:
        print(symbol)
    operation = input("Pick an operation from the line above: ")
    number2 = float(input("What is the second number?: "))
    if operation == "+":
        answer = add(number1, number2)
        print(f"{number1} + {number2} = {answer}")
    elif operation == "-":
        answer = subtract(number1, number2)
        print(f"{number1} - {number2} = {answer}")
    elif operation == "*":
        answer = multiply(number1, number2)
        print(f"{number1} * {number2} = {answer}")
    elif operation == "/":
        answer = divide(number1, number2)
        print(f"{number1} / {number2} = {answer}")
    else:
        print("You have not typed a valid operator, please run the program again.")
    calculate_again = input("Do you want to calculate again? Type 'y' for yes or 'n' for no: ")
    if calculate_again == "n":
        game_over = True
        print("Goodbye!")
    elif calculate_again == "y":
        game_over = False
    else:
        game_over = True
        print("You have not typed a valid answer, so the program will end now. Goodbye!")

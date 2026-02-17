list_of_words = []
word = input("Enter a word: ")

list_of_words_2 = [char + "Z" for char in word]
print(list_of_words_2)

for char in word:
    list_of_words.append(char)
print(list_of_words)


range_list = [num*2 for num in range(1,5)]
print(range_list)
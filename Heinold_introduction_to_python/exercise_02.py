# Fill the screen with a word(group)

# ask for the word
word = input("Enter a word(group): ")

# fill the screen
for i in range(100):
    print("")
    for j in range(100):
        print(word, end=" ")

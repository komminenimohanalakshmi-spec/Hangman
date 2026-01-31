import random

# Predefined list of words
words = ["python", "hangman", "programming", "science", "university"]

# Randomly choose a word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Display the word with underscores
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

while attempts > 0:
    print("\nWord:", display_word(word, guessed_letters))
    print("Attempts left:", attempts)
    
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        print("Good guess!")
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("Wrong guess.")
        attempts -= 1

if attempts == 0:
    print("\nGame Over! The word was:", word)
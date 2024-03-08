import random

library = ['apple', 'andrew', 'orange']
chosen_word = random.choice(library)
word_length = len(chosen_word)

print("The chosen word has {} letters.".format(word_length))

# Display dashes for each letter in the chosen word
display_word = "-" * word_length
print(display_word)

# Create an empty set to store guessed letters
guessed_letters = set()  

attempts = 5
while attempts > 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You've already guessed that letter.")
    elif guess in chosen_word:
        print("Nice job!")
        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)  
        # Update display_word to reveal guessed letters
        display_word = ''.join([letter if letter in guessed_letters else '-' for letter in chosen_word])
        print(display_word)
        if display_word == chosen_word:
            print("Congratulations! You guessed the word:", chosen_word)
            break
    else:
        print("Oops! Try again.")
        attempts -= 1
        print("You have {} attempts left.".format(attempts))

if attempts == 0:
    print("Sorry, you've run out of attempts. The word was:", chosen_word)

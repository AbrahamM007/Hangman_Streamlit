import streamlit as st
import random

def display_word(word, guessed_letters):
    remaining_letters = 0
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
            remaining_letters += 1
    return displayed_word, remaining_letters


def hangman():
    word_bank = ["apple", "banana", "orange", "grape", "kiwi", "melon", "peach", "pineapple", "mango", "cherry", "berry"]
    word = random.choice(word_bank)
    guessed_letters = []
    attempts = 6

    st.title("Hangman")
    displayed_word, remaining_letters = display_word(word, guessed_letters)
    st.write(displayed_word)

    guess_input_key = "guess_input"  # Initial key

    while True:
        guess = st.text_input("Guess a letter:", key=guess_input_key).lower()

        if guess in guessed_letters:
            st.write("You've already guessed that letter!")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            st.write("Please enter a single letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            st.write(f"Incorrect guess. You have {attempts} attempts left.")
            if attempts == 0:
                st.write(f"You've run out of attempts! The word was: {word}")
                break
        else:
            st.write("Correct guess!")

        displayed_word, remaining_letters = display_word(word, guessed_letters)
        st.write(displayed_word)
        st.write(f"{remaining_letters} letter(s) remaining.")

        if remaining_letters == 0:
            st.write(f"Congratulations! You've guessed the word: {word}")
            break

        # Update key for the next iteration
        guess_input_key = f"guess_input_{len(guessed_letters)}"

if __name__ == "__main__":
    hangman()

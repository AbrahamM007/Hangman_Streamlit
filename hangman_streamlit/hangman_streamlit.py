import streamlit as st
import random

def choose_word():
    word_bank = ["apple", "banana", "orange", "grape", "kiwi", "melon", "peach", "pineapple", "mango", "cherry", "berry"]
    return random.choice(word_bank)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    st.title("Hangman")
    st.write(display_word(word, guessed_letters))

    while True:
        guess = st.text_input("Guess a letter:").lower()

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

        displayed = display_word(word, guessed_letters)
        st.write(displayed)

        if '_' not in displayed:
            st.write(f"Congratulations! You've guessed the word: {word}")
            break

if __name__ == "__main__":
    hangman()

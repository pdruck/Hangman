from src import words, states
import random


# print the current state of the game
def print_state(state, correct):
    print(states.STATE[state])
    print()
    print(''.join([c + ' ' for c in correct]))  # correctly guessed letters separated by spaces
    print(''.join(['- ' for i in range(len(correct))]))  # dashes to display letter count


# check if letter is a correct or incorrect guess
# if correct, remove letter from the list of remaining letters
def make_guess(guess, correct, initial):
    letter_replaced = False

    for count, letter in enumerate(initial):
        if letter == guess:
            correct[count] = letter
            letter_replaced = True

    return correct, letter_replaced


# check for game end state
def game_end(state, initial, correct):
    if ''.join(correct) == initial:
        print("Good job, guy!")
        return True
    elif state == states.STATE_MAX:
        print("GG, ez")
        return True

    return False


# get first letter from user input
def get_user_input(already_guessed):
    while True:
        letter = input("Guess a letter: ").upper()
        if letter and letter[0].isalpha() and letter not in already_guessed:
            return letter[0]


if __name__ == "__main__":
    initial_word = random.choice(words.word_list).upper()  # target word
    guessed_letter = []  # list of letters that have been guessed already
    correct_letters = [' '] * len(initial_word)  # letters that have been guessed correctly
    state_num = 0  # game state number
    game_over = False

    # have user continue to guess letters until game is over
    while not game_over:
        # make guess
        current_letter = get_user_input(guessed_letter)
        guessed_letter.append(current_letter)
        correct_letters, correct_guess = make_guess(current_letter, correct_letters, initial_word)

        # if incorrect letter is guessed, move to next state
        if not correct_guess:
            state_num += 1

        print_state(state_num, correct_letters)

        if game_end(state_num, initial_word, correct_letters):
            game_over = True

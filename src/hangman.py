from src import words, states
import random


def print_state(state):
    print(initial)
    print(states.STATE[state])
    print(*remaining_letters, sep=' ')


# check if letter is a correct or incorrect guess
# if correct, remove letter from the list of remaining letters
def guess(guessed_letter, remaining):
    if guessed_letter in remaining:
        return remaining.replace(guessed_letter, ''), True

    return remaining, False


# check for game end state
def game_end(state):
    if len(remaining_letters) == 0:
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
    initial = random.choice(words.word_list).upper()    # target word
    remaining_letters = initial                         # remaining letters in target word
    guessed = []                                        # list of letters that have been guessed already
    state_num = 0                                       # game state number
    game_over = False

    while not game_over:
        # make guess
        current_letter = get_user_input(guessed)
        guessed.append(current_letter)
        remaining_letters, correct_guess = guess(current_letter, remaining_letters)

        # if incorrect letter is guessed, move to next state
        if not correct_guess:
            state_num += 1

        print_state(state_num)

        if game_end(state_num):
            game_over = True

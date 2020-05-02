from src import words, states
import random

selected = random.choice(words.word_list)
guessed = []


def print_state(state_num):
    print(selected)
    print(states.STATE[state_num])
    print(*guessed, sep=' ')


def guess():
    while True:
        letter = input("Guess a letter: ")
        if letter and letter[0].isalpha():
            letter = letter[0]
            guessed.append(letter)
            break

    if letter in selected:
        return True
    else:
        return False


def main():
    state_num = 0

    # while game is not over
    while state_num < states.STATE_MAX:
        if not guess():
            # if incorrect letter is guessed, move to next state
            state_num = state_num + 1

        print_state(state_num)


if __name__ == "__main__":
    main()

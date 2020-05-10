# bot.py
import asyncio
import os
import random

from src import hangman, words, states
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.command(name='hang', help='Play a game of hangman')
async def hangman_game(ctx):
    initial_word = random.choice(words.word_list).upper()  # target word
    guessed_letters = []  # list of letters that have been guessed already
    correct_letters = ['_'] * len(initial_word)  # letters that have been guessed correctly
    state_num = 0  # game state number
    game_over = False

    # have user continue to guess letters until game is over
    while not game_over:

        await ctx.send("Guess a letter: ")

        def check(msg):
            message = msg.content.upper()
            return message and message[0].isalpha() and message[0] not in guessed_letters and msg.author != bot.user

        try:
            current_letter = await bot.wait_for('message', check=check, timeout=20.0)
        except asyncio.TimeoutError:
            return await ctx.send('Sorry homie, you took too long! The answer is {}.'.format(initial_word))

        response = current_letter.content[0].upper()

        guessed_letters.append(response)
        correct_letters, correct_guess = hangman.make_guess(response, correct_letters, initial_word)

        # if incorrect letter is guessed, move to next state
        if not correct_guess:
            state_num += 1

        # formatting output for Discord
        correct_formatted = '`' + ''.join(''.join([c + ' ' for c in correct_letters])) + '`'
        guessed_formatted = '`' + ''.join(''.join([c + ' ' for c in guessed_letters])) + '`'
        await ctx.send(guessed_formatted)  # all guessed letters separated by spaces
        await ctx.send(states.STATE_FORMATTED[state_num])
        await ctx.send(correct_formatted)  # correctly guessed letters separated by spaces

        if ''.join(correct_letters) == initial_word:
            await ctx.send("Good job, guy!")
            game_over = True
        elif state_num == states.STATE_MAX:
            await ctx.send("The word was " + initial_word)
            await ctx.send("GG, ez")
            game_over = True


@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number=100):
    if number > 1:
        await ctx.send(str(random.choice(range(1, number))))
    else:
        await ctx.send("Don't do that")


bot.run(TOKEN)

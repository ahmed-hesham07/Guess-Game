# Guess-Game
This Python code is an implementation of a simple number guessing game where the user has to guess a randomly generated number between 1 and 10. Let's break down the code:

1. `import random`: This line imports the `random` module, which is used for generating random numbers.
2. `RandomNumber = int(random.randrange(1, 10))`: It generates a random integer between 1 and 9 (inclusive) using `randrange` from the `random` module.
    The generated random number is then converted to an integer.
4. `print('guess the number between 1 and 10')`: This line displays a message prompting the user to guess the number within the specified range.
5. `trials = 5`: The variable `trials` is set to 5, representing the number of attempts the user has to guess the correct number.
6. `UserGuess = int()`: It initializes the `UserGuess` variable as an integer. This is used to store the user's input later.
7. `while trials > 0 and UserGuess != RandomNumber:`: The game runs in a `while` loop as long as the user has remaining trials and has not guessed the correct number.
8. Inside the loop:
   - `UserGuess = int(input())`: The user is prompted to enter their guess, and the input is converted to an integer.
   - If the guess is higher than the random number, it prints 'TOO HIGH' and prompts the user to try again.
   - If the guess is lower than the random number, it prints 'TOO LOW' and prompts the user to try again.
   - If the user's guess is equal to the random number, it prints 'CONGRATULATIONS! YOU WON!' and continues to the next iteration of the loop.

The loop continues until the user guesses the correct number or runs out of trials. If the user guesses correctly within the allowed trials, they win the game. The loop also provides feedback on whether the guess is too high or too low.

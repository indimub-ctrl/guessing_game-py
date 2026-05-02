import random

while True:
    difficulty = input("Choose difficulty level (easy/hard): ")

    if difficulty == "easy":
        limit = 5
    else:
        limit = 3

    secret = random.randint(1, 50)

    tries = 0

    guess = int(input("Guess a number between 1 and 50: "))

    while guess != secret and tries < limit:
        tries += 1

        # Hint system
        if abs(guess - secret) <= 2:
            print("🔥 Very close!")

        print(f"Attempts left:", limit - tries)

        if guess > secret:
            print("Too high!")
        else:
            print("Too low!")

        if tries < limit:
            guess = int(input("Guess again: "))

    # Final result
    if guess == secret:
        print(f"Congratulation! You got it in {tries + 1} tries🎉")
    else:
        print(f"Out of tries ! The number was {secret}")

    # Replay option
    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        break

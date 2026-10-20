import random


def get_guess():
    while True:
        try:
            return int(input("Your guess: "))
        except ValueError:
            print("Please enter a number.")


def play():
    secret = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it in {attempts} attempts!")
            break


if __name__ == "__main__":
    while True:
        play()
        if input("Play again? (y/n): ").lower() != "y":
            print("Thanks for playing!")
            break
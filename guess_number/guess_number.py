import random


def guess_the_number():
    # The computer generates a random number from 1 to 100.
    secret_number = random.randint(1, 100)
    attempts = 0

    print("👋 Hi! I’ve thought of a number from 1 to 100. Try to guess it!")

    while True:
        try:
            # Берём ввод от пользователя
            user_guess = int(input("Enter your number: "))
            attempts += 1

            # We are checking the game conditions.
            if user_guess < secret_number:
                print("📉 No, my number is BIGGER.")
            elif user_guess > secret_number:
                print("📈 No, my number is SMALLER.")
            else:
                print(
                    f"🎉 Hurray! You guessed the {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("❌ Please enter an integer!")


if __name__ == "__main__":
    guess_the_number()

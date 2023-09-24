import random
def guess_number_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts  <= 5:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1
        if attempts == 5:
            print("Maximum number of attempts reached")
            break
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")
    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        guess_number_game()
    else:
        print("Thanks for playing!")
import random
import re

print("===== Number Guessing Game & Word Counter =====")

# Number Guessing Game
print("\n--- Number Guessing Game ---")

secret_number = random.randint(1, 100)
attempts = 0
score = 100

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            print("Attempts:", attempts)
            print("Score:", score)
            break

        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        score -= 10

        if score <= 0:
            print("Game over!")
            print("The correct number was:", secret_number)
            break

    except ValueError:
        print("Please enter a valid number.")

# Word Counter
print("\n--- Word Counter ---")

filename = input("Enter text file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())

    print("Total words:", len(words))

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("\nWord Frequency:")

    for word, count in frequency.items():
        print(word, ":", count)

except FileNotFoundError:
    print("File not found. Please check the file name.")
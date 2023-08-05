import random

def choose_word(category):
    # This function selects a word from the given category
    words = {
        "food": ["apple", "pineapple", "pomegranate", "plum", "banana"],
        "animals": ["cat", "dog", "mouse", "hamster", "squirrel"],
        "countries": ["poland", "germany", "hungary", "angola", "vatican"],
        "plants": ["sunflower", "grass", "tulip", "nettle", "rose"],
        "vehicle brands": ["tesla", "dodge", "hummer", "gmc", "lincoln"]
    }
    return random.choice(words.get(category, []))

def reveal_word(word, guessed_letters):
    # This function reveals part of the word, with the rest replaced by dashes
    revealed_word = ""
    for letter in word:
        if letter in guessed_letters:
            revealed_word += letter
        else:
            revealed_word += "-"
    return revealed_word

def draw_hangman(errors):
    # This function draws the hangman based on the number of errors
    hangman = [
        "   ____",
        "  |    |",
        "  |    " + ("O" if errors > 0 else ""),
        "  |   " + ("/|\\" if errors > 1 else ""),
        "  |   " + ("/" if errors > 2 else "") + (" \\" if errors > 3 else ""),
        "  |",
        "__|___"
    ]
    return "\n".join(hangman)

def get_hint(category, word):
    # This function provides a hint for the given category
    hints = {
        "food": "Category of words related to fruits.",
        "animals": "Category of words related to domestic animals.",
        "countries": "Category of words related to European countries.",
        "plants": "Category of words related to garden plants.",
        "vehicle brands": "Category of words related to US vehicle brands."
    }
    return hints.get(category, "No available hint.") + f" The word has {len(word)} letters."

def main():
    # The main game function. It asks the player to choose a category, initializes the game, reads input letters
    categories = ["food", "animals", "countries", "plants", "vehicle brands"]
    print("Choose a category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.capitalize()}")

    chosen_category = None
    while chosen_category not in range(1, len(categories) + 1):
        try:
            chosen_category = int(input("Enter the category number: "))
            if chosen_category not in range(1, len(categories) + 1):
                print("Invalid category number. Choose a number from 1 to", len(categories))
        except ValueError:
            print("Invalid category number. Try again.")

    word = choose_word(categories[chosen_category - 1])
    lives = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("You have", lives, "chances to guess the word.")
    print("The category is", categories[chosen_category - 1].capitalize() + ":")

    while lives > 0:
        revealed_word = reveal_word(word, guessed_letters)
        print("\nWord:", revealed_word)
    
        if revealed_word == word:
            print("Congratulations! You guessed the word:", word)
            break
    
        letter = input("Enter a letter ('x' for a hint). WARNING! Each hint costs you 1 life! ").lower()
    
        if letter == "x":
            print("You get a hint, but you lose one life.")
            lives -= 1
            print("You have", lives, "lives left.")
            print(draw_hangman(6 - lives))
            print(get_hint(categories[chosen_category - 1], word))
            continue
    
        if letter in guessed_letters:
            print("This letter has already been guessed.")
            continue
    
        guessed_letters.add(letter)
    
        if letter in word:
            print("Well done! The letter", letter, "is in the word.")
        else:
            lives -= 1
            print("Unfortunately, the letter", letter, "is not in the word. You have", lives, "lives left.")
            print(draw_hangman(6 - lives))

    if lives == 0:
        print("\nYou lost! The word was:", word)

if __name__ == "__main__":
    main()


import difflib

# Initialize list to track wrong words
incorrect_words = []

# Function to check if word is available
def check_word_availability(word):
    # Sample logic to check word availability
    given_words = ["phone", "changer", "cat", "dog", "remote"]
    if word in given_words:
        return True
    else:
        return False

# Function to suggest similar words
def ssw(word):
    # Sample logic to suggest similar words
    givenword = ["phone", "changer", "cat", "dog", "remote"]
    suggested_word = difflib.get_close_matches(word, givenword)
    return suggested_word


if __name__ == "__main__":    
    no_of_tries = 0
    while True:
        user_input = input("Enter a word: ")
        if not check_word_availability(user_input):
            incorrect_words.append(user_input)
            no_of_tries += 1
            if no_of_tries >= 2:
                print("You have entered wrong words multiple times. Here are the wrong words you entered so far:")
                print(incorrect_words)
                print("Suggestions for the wrong words:")
                for incorrect in incorrect_words:
                    s = ssw(incorrect)
                    print(f"Word '{incorrect}' not found. Suggestions: {s}")
                break
            else:
                print("Word is not available. Suggestions:")
                s = ssw(user_input)
                print(s)
        else:
            print("Word is available.")
            break
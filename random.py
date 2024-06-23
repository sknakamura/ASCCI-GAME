import random

def generate_word():
    # Generate a random word
    word = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                          'U', 'V', 'W', 'X', 'Y', 'Z'])
    return word

def convert_to_ascii(word):
    # Convert word to ASCII values
    ascii_values = [ord(char) for char in word]
    return ascii_values

def play_game():
    print("Welcome to the ASCII Word Guessing Game!")
    print("You have 3 tries to guess the word.")
    print("The game starts with easier words (single letters) and progresses to harder ones.")
    print("Let's begin!\n")
    
    tries = 3
    difficulty_levels = ['Easy', 'Medium', 'Hard']
    current_difficulty = 0
    
    while tries > 0:
        print(f"Difficulty: {difficulty_levels[current_difficulty]}")
        word = generate_word()
        ascii_values = convert_to_ascii(word)
        
        print(f"ASCII values of the word: {ascii_values}")
        
        guess = input("Guess the word: ").strip().upper()
        
        if guess == word:
            print("Congratulations! You guessed the word correctly.")
            current_difficulty += 1
            tries = 3  # Reset tries for the next level
        else:
            tries -= 1
            if tries > 0:
                print(f"Incorrect guess. You have {tries} tries left.\n")
            else:
                print(f"Sorry, you've run out of tries. The correct word was '{word}'.")
                break
        
        if current_difficulty >= len(difficulty_levels):
            print("Congratulations! You've completed all levels.")
            break

if __name__ == "__main__":
    play_game()

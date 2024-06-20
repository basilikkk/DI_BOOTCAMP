import random

def get_words_from_file(filename):
    """Read words from a file and return them as a list."""
    with open(filename, 'r') as file:
        words = file.read().split()
    return words

def get_random_sentence(words, length):
    """Generate a random sentence of a given length."""
    random_words = random.sample(words, length)
    sentence = ' '.join(random_words).lower()
    return sentence

def main():
    """Main function to run the random sentence generator program."""
    print("This program generates a random sentence of a specified length.")
    
    try:
        length = int(input("How long do you want the sentence to be (2-20)? "))
        
        if length < 2 or length > 20:
            print("Error: The length must be an integer between 2 and 20.")
            return
        
        words = get_words_from_file('sowpods.txt')
        sentence = get_random_sentence(words, length)
        
        print(f"Generated sentence: {sentence}")
        
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()

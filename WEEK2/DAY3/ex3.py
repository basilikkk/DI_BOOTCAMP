import random
import string

def generate_random_string(length=5):
    letters = string.ascii_letters  # This contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_string = ''.join(random.choices(letters, k=length))
    return random_string

# Example usage
print(generate_random_string())

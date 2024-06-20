from anagram_checker import AnagramChecker

def main():
    checker=AnagramChecker('sowpods.txt')
    print(checker.words)
    while True:
        print('welcome!')
        print("1. Input a word")
        print("2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            word = input("Enter a word: ").strip()
            if not word.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue
            if ' ' in word:
                print("Error: Only a single word is allowed.")
                continue

            if checker.is_valid_word(word):
            
                anagrams = checker.get_anagrams(word)
                print(f"Anagrams for '{word}': {', '.join(anagrams) if anagrams else 'No anagrams found.'}")
            else:
                print(f"'{word}' is not a valid English word.")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
  
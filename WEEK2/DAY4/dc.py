class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        """Returns the frequency of a word in the text."""
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return f"The word '{word}' does not appear in the text."
        return count

    def most_common_word(self):
        """Returns the most common word in the text."""
        words = self.text.split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        most_common = max(word_counts, key=word_counts.get)
        return most_common

    def unique_words(self):
        """Returns a list of all unique words in the text."""
        words = self.text.split()
        unique_words = list(set(words))
        return unique_words

    @classmethod
    def from_file(cls, filename):
        """Creates a Text instance from a file."""
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)

# Example usage:
text_example = "A good book would sometimes cost as much as a good house."
text = Text(text_example)
print(f"Frequency of 'good': {text.word_frequency('good')}")
print(f"Most common word: {text.most_common_word()}")
print(f"Unique words: {text.unique_words()}")

# Using the class method to create an instance from a file
text_from_file = Text.from_file('the_stranger.txt')
print(f"Frequency of 'the': {text_from_file.word_frequency('the')}")
print(f"Most common word: {text_from_file.most_common_word()}")
print(f"Unique words: {text_from_file.unique_words()}")

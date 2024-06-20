class AnagramChecker:
    def __init__(self,word_list_file):
        with open(word_list_file,'r') as file:
            self.words=set(file.read().split())


      

    def is_valid_word(self,word:str):
        return word.upper() in self.words



    def get_anagrams(self,word):
        word=word.upper()
        anagrams=[w for w in self.words if self.is_anagram(word,w)]
        return anagrams
    
    def is_anagram(self,word1,word2):
        return sorted(word1)==sorted(word2) and word1 !=word2
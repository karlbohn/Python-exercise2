"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, source):
        
        word_list = open(source)
        self.words = self.parse(word_list)
        print(f"{len(self.words)} words read")
    
    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [word.strip() for word in dict_file]
    
    def random(self):
        '''Returns random word'''
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    
    # def __init__(self, source):
    #     super().__init_(source)

    def parse(self, dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
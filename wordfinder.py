from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""


    def __init__(self, path):
        """ construct a word finder"""
        self.path = path
        self.get_word_list()

    def __repr__(self):
        return f"<Word Finder path={self.path}>"


    def random(self):
        """returns a random word from word_list"""
        return choice(self.word_list)


    def get_word_list(self):
        """creates a list of words from the path """
        with open(self.path, 'r') as file:
            content = file.read()
            content.replace('\n', ' ')
            self.word_list = content.split()

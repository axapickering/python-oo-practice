from random import choice

class WordFinder:
    """Word Finder: finds random words from a file."""


    def __init__(self, path):
        """ construct a word finder"""

        self.path = path
        self.word_list = self.get_word_list()
        self.print_word_count()

    def __repr__(self):
        return f"<Word Finder path={self.path}>"
    # add word count


    def random(self):
        """returns a random word from word_list"""

        return choice(self.word_list)


    def get_word_list(self):
        """creates a list of words from the path """

        word_list = []
        with open(self.path, 'r') as file:
        # return [line.strip() for line in file]
            for line in file:
                word_list.append(line.strip())
        return word_list

    def print_word_count(self):
        """print out the count of words"""

        print(f"{len(self.word_list)} words read")

class SpecialWordFinder(WordFinder):
    '''subclass of WordFinder that can handle empty lines and comments'''

    def get_word_list(self):
        """creates a list of words from the path """

        word_list = super().get_word_list()

        return [word for word in word_list if len(word.strip()) > 0 and word[0] != "#"]
    # if word is not emptystring
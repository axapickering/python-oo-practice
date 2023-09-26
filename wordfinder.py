from random import choice

class WordFinder:
    """Word Finder: finds random words from a file."""


    def __init__(self, path):
        """ construct a word finder"""
        self.path = path
        self.get_word_list()
        self.print_word_count()

    def __repr__(self):
        return f"<Word Finder path={self.path}>"


    def random(self):
        """returns a random word from word_list"""

        return choice(self.word_list)


    def get_word_list(self):
        """creates a list of words from the path """
        word_list = []
        with open(self.path, 'r') as file:
            for line in file:
                line = line.strip()
                word_list.append(line)
        self.word_list = word_list

        file.close()


    def print_word_count(self):
        """print out the count of words"""

        print(f"{len(self.word_list)} words read")

class RandomWordFinder(WordFinder):
    '''subclass of WordFinder that can handle empty lines and comments'''

    def get_word_list(self):
        """creates a list of words from the path """
        word_list = []
        super().get_word_list()

        # for line in self.word_list:
            # if line.startswith('#')


        self.word_list = word_list
        print(f"{len(word_list)} words read")
        file.close()
        #TODO:shouldn't open the file again/start with what the parent

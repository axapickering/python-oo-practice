from random import choice

class WordFinder:
    """Word Finder: finds random words from a file."""


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
            print(f"len(self.word_list) words read")
        file.close()

class RandomWordFinder(WordFinder):
    '''subclass of WordFinder that can handle empty lines and comments'''

    def __init__(self,path):
        '''creates a new instance of RandomWordFinder, requires path'''
        super().__init__(path)

    def get_word_list(self):
        """creates a list of words from the path """
        word_list = []
        with open(self.path, 'r') as file:
            for line in file:
                line.replace('\n',"")
                if (len(line.strip()) != 0 or line.find("#") == -1):
                    for word in line.split():
                        word_list.append(word)

        self.word_list = word_list
        print(f"{len(word_list)} words read")
        file.close()


from random import choice


class WordFinder:
    """ 
    A class used to get a random word from a file on disk
    
    Attributes
    ----------------
    path: path to file on disk
    """
    
    def __init__(self, path):
        # Create a random word from a file
        self.path = path
        self.words = self.read_file() 
        
    def read_file(self):
        # Read file and return list of words
        try:
            return self.get_words()
        except FileNotFoundError as exc:
            print(f'File {exc} does not exist')
            
    def get_words(self):
        # Get list of words from file
        count = 0
        words = []
        
        with open(self.path) as f:
                Lines = f.readlines()
                for line in Lines:
                    count += 1
                    words.append(line.strip())
                return words
            
    def random(self):
        # Returns a random word from the word list
        return choice(self.words)
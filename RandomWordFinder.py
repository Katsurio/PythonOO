from WordFinder import WordFinder

class RandomWordFinder(WordFinder):
    """ 
    A subclass of WordFinder used to get a random word from a file on disk 
    but exclude blank lines and comments.
    
    >>> rwf = RandomWordFinder("comment.txt")
    4 words read

    >>> rwf.random() in rwf.read_file()
    True

    >>> rwf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> rwf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    """
            
    def read_file(self):
        """ Read file and return list items without strings of spaces and comments """
        
        # Strip comments
        word_list = [word for word in super().read_file() if not word.startswith('#')]
        # Strip list items that only contain strings
        return list(filter(None, word_list))
"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)
    
    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """ Create a generator starting from start """
        self.start = start
        self.next = start
        self.count = 0

    def __repr__(self):
        """ Show representation """
        return f"SerialGenerator start={self.start} next={self.next + 1}"
        
    def generate(self):
        """ Increments self.next and self.count both by 1 for every generate() call """
        self.next = self.get_next()
        self.count += 1
        return self.next
    
    def get_next(self):
        """ Gets next value depending on count's current value """
        return self.next + 1 if self.count > 0 else self.next
    
    def reset(self):
        """ Reset start to original value """
        self.next = self.start
        self.count = 0
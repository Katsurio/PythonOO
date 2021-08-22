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
        """ Create a generator from starting from start """
        self.start = start
        self.orignal_value = start

    def generate(self):
        """ Increment start by 1 """
        self.start += 1
        return self.start
    
    def reset(self):
        """ Reset start to original value """
        self.start = self.orignal_value
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

    def __init__(self,start=100):
        '''Creates new instance of SerialGenerator with attribute start,
          defaults to 100'''
        self.start = start
        self.current_serial = start

    def reset(self):
        '''resets the serial number back to initial start number'''
        self.current_serial = self.start


    def generate(self):
        '''return the next sequential number'''
        self.current_serial += 1
        # returning what the number was before incrementing
        return self.current_serial - 1

    def __repr__(self):
        return f'<SerialGenerator: start={self.start}, current_serial={self.current_serial}>'
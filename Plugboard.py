
import string
class Plugboard(object):
    def __init__(self, wires):
        """
        wires: This is the mapping of pairs of characters
        """
        self.map = {}
        for char in string.ascii_uppercase:
            if char in wires:
                ind = wires.index(char)
                if ind % 2 == 0:
                    self.map[char] = wires[ind + 1]
                else:
                    self.map[char] = wires[ind - 1]
            else:
                self.map[char] = char
        
    def process(self, c):
        """
        c: The single character to process
        """
        return self.map[c]
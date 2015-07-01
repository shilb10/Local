import sys

class Node:

    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
    
    def get_val(self):
        return self.val

    def get_neighbors(self):
        return self.neighbors

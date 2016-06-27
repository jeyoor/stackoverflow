from collections import defaultdict

#https://stackoverflow.com/questions/38041857/checking-if-keys-already-in-dictionary-with-try-except

class SimpleNameCounter:
    """Test counting elements using a dict
    Here's a next lines of doc comment"""
    def __init__(self):
        self.number_found = {}
    def _count_occurences(self, ele_name):
    try:
        #this checks to see if the item's already in the dict
        self.number_found[item] = self.number_found[item] + 1
        x = self.number_found[item] 
        #here's a line that fixes the issue presented by op
        return x
    except KeyError:
        x = 1
        #this adds an item if not in the dict
        self.number_found[item] = x
        return x



class BetterNameCounter:
    """Test counting elements using a defaultdict
    Here's a next lines of doc comment"""
    def __init__(self):
        self.number_found = defaultdict(int)
    def _count_occurences(self, ele_name):
    try:
        #this checks to see if the item's already in the dict
        self.number_found[item] = self.number_found[item] + 1
        x = self.number_found[item] 
        #here's a line that fixes the issue presented by op
        return x
    except KeyError:
        x = 1
        #this adds an item if not in the dict
        self.number_found[item] = x
        return x

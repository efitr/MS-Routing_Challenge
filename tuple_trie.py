
# This is a basic node
class NumbersNode(object):
    #
    def __init__(self):
        # self.data = tuple()
        self.children = []*10
        self.pattern_end = False
    
# This is the TupleTrie
class NumbersTrie(object):
    def __init__(self, file_with_prefix): 
        self.root = NumbersNode()

        for route_cost in file_with_prefix:
            self.add_route(route_cost)

    def get_index(self, number_in_telephone):
        # print(letter)
        return ord(number_in_telephone.lower())-ord('a')

    def add_route(self, route):
        # here is where the each possible patterns gets
        # inserted
        node = self.root
    
    # The trie must get you a list of all possible carriers that have the longest prefix
    def search(self, phone_number):
        # here we implement back tracking
        # recursively go down to the furthest possible node

        return #longest_prefix


    


# This is a basic node
class TupleNode(object):
    #
    def __init__(self):
        # self.data = tuple()
        self.children = []*10
        self.pattern_end = False
    
# This is the TupleTrie
class TupleTrie(object):
    def __init__(self, file_with_prefix): 

        self.root = TupleNode()

        # node = self.root
        # for children in node.children:
        #     children = node.children

        for route_cost in file_with_prefix:
            self.add_route(route_cost)

    def get_index(self, letter):
        # print(letter)
        return ord(letter.lower())-ord('a')

    def add_route(self, route):
        # here is where the each possible patterns gets
        # inserted
        node = self.root
    
    def search(self, phone_number):
        # here we implement back tracking
        # recursively go down to the furthest possible node

        return #phone_prefix
    

    

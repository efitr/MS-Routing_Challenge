
# This is a basic node
class NumbersNode(object):
    #
    def __init__(self):
        # self.data = tuple()
        self.children = [None]*10
        self.pattern_end = False
    
# This is the TupleTrie
class NumbersTrie(object):
    def __init__(self, file_with_prefix): 
        self.root = NumbersNode()

        for route_cost in file_with_prefix:
            self.add_route(route_cost)

    def get_index(self, number_in_telephone):
        # print(letter)
        return ord(number_in_telephone)-ord('0')

    def add_route(self, route):
        # we make the node where this starts be the root of the Trie
        node = self.root

        # iterate every number in the route
        for number in route:
    
            index = self.get_index(number)

            # If nothing has been added to that particular index
            if node.children[index] is None:
                # Make a new node
                new_node = NumbersNode()
                # Place in that index the new_node
                node.children[index] = new_node
                # To keep on traversing if there still number in the route
                node = new_node
            else:
                # Given that the place is with a node keep on traversing
                node = node.children[index]
        # The end of the route has been reached make that node be the end
        node.pattern_end = True
    
    # The trie must get you a list of all possible carriers that have the longest prefix
    def search(self, phone_number):
        # here we implement back tracking
        # recursively go down to the furthest possible node

        return #longest_prefix


    

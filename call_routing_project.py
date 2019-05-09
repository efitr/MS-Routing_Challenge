
###########################################################################################
############# Call routing project
###########################################################################################

# Objective

# Process
    # file path for the routing
    # file path for the telephone

    # TupleTrie.search(telephone_number)
        # return the longest prefix

    # def get_cost(longest_prefix, phone_number)
        # here is the dictionary 
        # returns the cost

    # def get_phone_with_cost(telephone):
        # Trie.search for the longest_prefix
        # get_cost(longest_prefix, telephone_number)
        # return tuple with phone number with routing cost

# Scenario1: 


# def get_cost(telephone):
            
def main():
    ##### PATH
    # Phone Number Paths
    path_phone_number_10 = "../../../../../RoutingFiles/CallRouting/phone-numbers-10.txt"
    # path_phone_number_100 = "../../../../../RoutingFiles/CallRouting/phone-numbers-100.txt"
    # path_phone_number_1000 = "../../../../../RoutingFiles/CallRouting/phone-numbers-1000.txt"
    # path_phone_number_10000 = "../../../../../RoutingFiles/CallRouting/phone-numbers-10000.txt"

    # Routing Cost Paths
    path_routing_costs_10 = "../../../../../RoutingFiles/CallRouting/route-costs-10.txt"
    # path_routing_costs_100 = "../../../../../RoutingFiles/CallRouting/route-costs-100.txt"
    # path_routing_costs_600 = "../../../../../RoutingFiles/CallRouting/route-costs-600.txt"
    # path_routing_costs_35000 = "../../../../../RoutingFiles/CallRouting/route-costs-35000.txt"
    # path_routing_costs_106000 = "../../../../../RoutingFiles/CallRouting/route-costs-106000.txt"
    # path_routing_costs_1000000 = "../../../../../RoutingFiles/CallRouting/route-costs-1000000.txt"
    # path_routing_costs_10000000 = "../../../../../RoutingFiles/CallRouting/route-costs-10000000.txt"

    ##### FILE
    # Phone Number File
    phone_numbers_file = open(path_phone_number_10, 'r')
    # Routing Cost File
    routing_costs_file = open(path_routing_costs_10, 'r')
    
    phone_numbers = phone_numbers_file.readlines()
    routing_costs = routing_costs_file.readlines()
    print(phone_numbers)
    print(routing_costs)

if __name__ == '__main__':
    main()
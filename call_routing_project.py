
###########################################################################################
############# Call routing project
###########################################################################################

##### Objective:
#   * Find the least cost route through multiple carriers

##### Process:
#   * Get the data until a point in which it can be processed

#   * Get all the routes without the cost into a Trie DataStructure

#   * The trie gets you the longest prefix available

#   * With the longest available prefix get all the different costs

#   * Pair the cheapest cost in a tuple with the telephone number 

# Scenario1: 

# Functions:

            
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
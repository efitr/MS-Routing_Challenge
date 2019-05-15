
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

from tuple_trie import NumbersNode, NumbersTrie
import re

# Functions:
def cleaning_phone_numbers(data):
    clean_data = []
    for element in data:
        element = re.sub('[+]', '', element)
        element = re.sub('[\n]', '', element)
        clean_data.append(element)
    return clean_data

def cleaning_routes(data):
    clean_data = []
    for element in data:
        element = re.sub('[+]', '', element)
        route, cost = element.split(",")
        del(cost)
        clean_data.append(route)
    return clean_data

def route_dictionary_of_lists(data):
    dictionary = {}
    for element in data:
        element = re.sub('[+]', '', element)
        route, cost = element.split(",")
        # if cost is already in the dictionary
        if route in dictionary:
            previous_cost = dictionary[route]
            dictionary[route] = [cost, previous_cost]
        dictionary[route] = cost
    return dictionary

def tuple_phones_numbers_least_cost():
    pass
            
def main():
    ##### PATH
    # Phone Number Paths
    path_phone_number_10 = "../../../../../RoutingFiles/CallRouting/phone-numbers-10.txt"
    # path_phone_number_100 = "../../../../../RoutingFiles/CallRouting/phone-numbers-100.txt"
    # path_phone_number_1000 = "../../../../../RoutingFiles/CallRouting/phone-numbers-1000.txt"
    # path_phone_number_10000 = "../../../../../RoutingFiles/CallRouting/phone-numbers-10000.txt"

    # Routing Cost Paths
    # path_routing_costs_10 = "../../../../../RoutingFiles/CallRouting/route-costs-10.txt"
    path_routing_costs_100 = "../../../../../RoutingFiles/CallRouting/route-costs-100.txt"
    # path_routing_costs_600 = "../../../../../RoutingFiles/CallRouting/route-costs-600.txt"
    # path_routing_costs_35000 = "../../../../../RoutingFiles/CallRouting/route-costs-35000.txt"
    # path_routing_costs_106000 = "../../../../../RoutingFiles/CallRouting/route-costs-106000.txt"
    # path_routing_costs_1000000 = "../../../../../RoutingFiles/CallRouting/route-costs-1000000.txt"
    # path_routing_costs_10000000 = "../../../../../RoutingFiles/CallRouting/route-costs-10000000.txt"

    ##### FILE
    # Phone Number File
    phone_numbers_file = open(path_phone_number_10, 'r')
    # Routing Cost File
    routing_costs_file = open(path_routing_costs_100, 'r')
    
    phone_numbers = phone_numbers_file.readlines()
    routing_costs = routing_costs_file.readlines()
    print('These are the phone numbers: ',phone_numbers)
    print('These are the routes cost: ',routing_costs)

    # Formatting data before getting it into the Trie
    clean_phone_numbers = cleaning_phone_numbers(phone_numbers)
    clean_routes = cleaning_routes(routing_costs)
    print('These are the phone numbers without + and \ n: ',clean_phone_numbers)
    print('These are the routes without + and cost: ', clean_routes)


    # Make a Trie Data Structure 
    trie = NumbersTrie(clean_routes)
    # print(trie)
    for phone_number in clean_phone_numbers:
        longest_route = trie.search(phone_number)
        print('This is the longest route from this phone number ', longest_route)

    # Making a dictionary with all the data
    dictionary_route_list_costs = route_dictionary_of_lists(routing_costs)


if __name__ == '__main__':
    main()
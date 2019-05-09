
###########################################################################################
############# Call routing project
###########################################################################################

# Scenario1: 

def cost_of_calling_one_route(numbers_list, prefix_dict):

    # Iterate through every number in the numbers list
    for number in numbers_list:
        # For each number get an index
        for prefix, value in enumerate(prefix_dict):
            
            current_prefix = prefix_dict[0]

            if len(current_prefix) > 

            #  If a number coincides with a prefix, return that vuew
            if number in prefix:
                return value
            
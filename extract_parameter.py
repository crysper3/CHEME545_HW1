def extract_parameter(unit, parameter, index):
    '''A function that outputs the value for the unit parameter pair the 
    user is interested in checking. It will return an error if any of the 
    three inputs are incorrect. The user must run have the `unit_operations_data`
    dictionary in order to use this function.'''
    # Check that the inputs are accessible by our dictionary
    if (unit in unit_operations_data.keys() and # Checks that unit is a key
        parameter in unit_operations_data[unit] and # Checks that parameter corresponds to unit
        index <= (len(unit_operations_data[unit][parameter]) - 1)): # Checks that index is in list
        
        #  Access the dictionaries using keys and access list using index
        return print(f'{unit}_{parameter}_{unit_operations_data[unit][parameter][index]}')
    else:
        # If any input is incorrect, return error message
        return print('Invalid input')
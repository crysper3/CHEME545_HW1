def calculate_solution_weights(molecular_weights, solutions_needed):
    '''Function to calculate weight in 1L solution given a dictonary and list.'''
    # Check if solution exists in dictionary of mol weights
    for solution in solutions_needed:
        idx = solutions_needed.index(solution)

        # Need to parse the chemical name from the str
        chemical = solutions_needed[idx].split('-')[0]

        # Check that chemical is in dictionary
        if chemical in molecular_weights.keys():
            # Takes substring between hyphen and M, then convert to float
            molarity = float((solutions_needed[idx].split('-')[1]).split('M')[0])
            molecular_weight = molecular_weights[chemical] # Find mol weight
            weight = molarity * molecular_weight * 1       # Calculate weight needed
            output = f'{chemical}-{molarity}-{weight:.2f}' # Format new string
            solutions_needed[idx] = output
        else:
            solutions_needed[idx] = 'unknown'
    return solutions_needed
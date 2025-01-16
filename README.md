# CHEME545_HW1
This repo contains Python scripts made for the first homework assignment in CHEME 545. 

## Approach to defining these functions
1. For `extract_parameter`, I noticed the dictionary provided was actually two dictionaries. Once `unit` was used as a key, the values were keys to a subsequent dictionary of parameters.
I took advantage of this in my if statement to check for membership of the variables taken in using the `.keys()` function. Finally, I also added the requirement for the index to 
be less than or equal to len(list)-1, so the if statement could determine whether it is out of bounds. 

2. For `calculate_solution_weight`, I started with a loop that would check membership in the `molecular_weights` dictionary. However, in order to do so, I needed to extract the chemical 
name from the larger string using split. If the chemical is not in the dictionary, it uses the given chemicals index to replace its entry in `solutions_needed` with "unknown". If the chemical 
is indeed in the dictionary, I used the same principle to isolate the molarity and turn it into a float so it could be used for weight calculation.

## Running this Python files
To run these files, they must be in the users current working directory. If using in a Jupyter notebook, remember to import the function from the Python file: `from python_file.py import function`.  


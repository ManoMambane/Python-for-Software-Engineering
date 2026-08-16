# Function to print dictionary values given the keys
# Fix 1: Changed `dictionary[k]` to `dictionary[key]` to match the loop variable name.
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {
    "lisa": "BAAAAAART!", 
    "bart": "Eat My Shorts!", 
    "marge": "Mmm~mmmmm", 
    "homer": "d'oh!", 
    "maggie": "(Pacifier Suck)"
}

# Fix 2: Passed keys as a list `['lisa', 'bart', 'homer']` instead of individual positional arguments, matching the expected `keys` parameter in the function definition.
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
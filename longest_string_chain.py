# Python Code for Finding the Longest String Chain
# ROSZHAN RAJ MEENAKSHI SUNDHRESAN, PARASTO TOOSIE, DEEPTHIMAYI PEASALA


def longest_string_chain(strings):
    # Step 1: Sort the strings by length
    strings.sort(key=len)
    
    # Step 2: Create a dictionary to store the longest chain ending at each string
    longest_chain = {}
    
    # Initialize variables to keep track of the longest chain found
    max_chain_length = 0
    max_chain_end = None
    
    for string in strings:
        # Initialize the chain length for the current string
        longest_chain[string] = [string]
        
        # Step 3: Try to form chains by removing one character at a time
        for i in range(len(string)):
            predecessor = string[:i] + string[i+1:]  # Remove one character
            
            if predecessor in longest_chain:
                # If a valid predecessor is found, check if we can form a longer chain
                if len(longest_chain[predecessor]) + 1 > len(longest_chain[string]):
                    longest_chain[string] = longest_chain[predecessor] + [string]
        
        # Step 4: Update the maximum chain length and end if found
        if len(longest_chain[string]) > max_chain_length:
            max_chain_length = len(longest_chain[string])
            max_chain_end = string
    
    # Step 5: Return the longest chain in descending order, or an empty list if no valid chain exists
    if max_chain_length > 1:
        return longest_chain[max_chain_end][::-1]  # Reverse the chain for descending order
    else:
        return []

# Sample input
strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

# Get the longest string chain
result = longest_string_chain(strings)

# Print the output
print(result)
# ROSZHAN RAJ MEENAKSHI SUNDHRESAN, PARASTO TOOSIE, DEEPTHIMAYI PEASALA

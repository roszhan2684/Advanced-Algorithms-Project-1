#Task A: Shipping Two Items
#input: a list P = {(𝑝, 𝑠): 𝑝 ∈ 𝑛, 𝑠 𝑖𝑠 𝑎 𝑠𝑡𝑟𝑖𝑛𝑔} of n products, where each p is a price (in dollars) and s is a string indicating the product
# name (ie each element of the list is a tuple, containing the price and the name of the product).
#Output: two products (𝑝!, 𝑠!), (𝑝", 𝑠") P such that 𝑝! + 𝑝"= 2500; or NIL if no such pair exists
#baseline goal: an algorithm that runs in 𝑂(𝑛") time
#improvement goal: speed up to (𝑛𝑙𝑜𝑔𝑛), or (𝑛) expected time


#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK A: BASELINE SOLUTION

# Baseline O(n²) solution for finding two products whose prices sum up to 2500
def find_pair_baseline(products):
    """
    Finds two products whose prices add up to 2500 dollars using a baseline approach.

    This approach checks every possible pair of products in the list.
    It runs in O(n²) time because for each product, we compare it with every other product.

    :param products: List of tuples where each tuple contains (price, product_name).
    :return: Two products whose prices sum to 2500, or NIL if no such pair exists.
    """
    # Get the number of products in the list
    n = len(products)

    # Outer loop: iterate through each product in the list.
    # The variable 'i' represents the index of the first product we are checking.
    for i in range(n):

        # Unpack the price and name of the first product (at index i)
        price1, product1 = products[i]

        # Inner loop: for the current product (at index i), check it against every other product
        # in the list that comes after it (from index i+1 onwards).
        for j in range(i + 1, n):  # j starts at i+1 to avoid checking the same pair twice and comparing the product with itself

            # Unpack the price and name of the second product (at index j)
            price2, product2 = products[j]

            # Check if the sum of the two prices equals 2500
            if price1 + price2 == 2500:
                # If we find two products whose prices sum to 2500, return them as a tuple.
                return (price1, product1), (price2, product2)

    # If no such pair is found after all comparisons, return "NIL".
    return "NIL"

#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK A: BASELINE SOLUTION

# Example usage: a list of products where each product has a price and a name.
products = [(1000, "Product1"), (1500, "Product2"), (500, "Product3"), (2000 , "Product4")]

# Call the function to find two products whose prices sum to 2500
result = find_pair_baseline(products)

# Print the result. If a pair is found, it prints the two products. If not, it prints "NIL".
print(result)  # Output: ((1000, 'Product1'), (1500, 'Product2'))

#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK A: BASELINE SOLUTION
# Example usage: a list of products where each product has a price and a name.
products = [(10000, "Product1"), (150, "Product2"), (5000, "Product3"), (7000 , "Product4")]

# Call the function to find two products whose prices sum to 2500
result = find_pair_baseline(products)

# Print the result. If a pair is found, it prints the two products. If not, it prints "NIL".
print(result)  # Output: NIL

"""Question one using sorting algorithm.
Improvement O(n(log n)) solution for finding two products whose prices sum up to 2500


"""

#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK A: IMPROVEMENT SOLUTION
# Improvement O(n(log n)) solution for finding two products whose prices sum up to 2500

def find_pair_with_sorting(products):
    """
    Finds two products whose prices add up to 2500 dollars using sorting and two-pointer technique.

    :param products: List of tuples where each tuple contains (price, product_name)
    :return: Two products whose prices sum to 2500 or NIL if no such pair exists
    """

    # Step 1: Sort the products by price (the first element in the tuple).
    # Sorting is done in ascending order of prices, which takes O(nlogn) time.
    products_sorted = sorted(products, key=lambda x: x[0])

    # Step 2: Initialize two pointers.
    # 'left' starts from the beginning of the sorted list (cheapest product).
    # 'right' starts from the end of the sorted list (most expensive product).
    left = 0
    right = len(products_sorted) - 1

    # Define the target sum that we are trying to find (2500 dollars).
    target_sum = 2500

    # Step 3: Use the two-pointer technique to find the pair of products.
    # The two pointers will move towards each other until they meet or we find a pair.
    while left < right:
        price1, product1 = products_sorted[left]
        price2, product2 = products_sorted[right]
        current_sum = price1 + price2

        if current_sum == target_sum:
            return (price1, product1), (price2, product2)
        elif current_sum < target_sum:
            left += 1  # Move the left pointer to the right to increase the sum

        # Step 6: If the current sum is greater than the target sum,
        # move the 'right' pointer one step to the left to try a cheaper product.
        else:
            right -= 1  # Move the right pointer to the left to decrease the sum

    # If no pair is found, return NIL
    return "NIL"

#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK A: IMPROVEMENT SOLUTION
# Example usage
products = [(1000, "Product1"), (500, "Product2"), (450, "Product3"), (2000, "Product4")]
result = find_pair_with_sorting(products)
print(result)  # Output: ((1000, 'Product1'), (1500, 'Product2'))

#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK A: IMPROVEMENT SOLUTION
# Example usage
products = [(10000, "Product1"), (500, "Product2"), (4500, "Product3"), (3000, "Product4")]
result = find_pair_with_sorting(products)
print(result)  # Output: ((1000, 'Product1'), (1500, 'Product2'))

"""QUESTION 1)
Task B: Joining Databases
input: a list 𝐿 = {(𝑘, 𝑥): 𝑘, 𝑥 ∈ ℕ} where each k is distinct; and another list 𝑅 = {(𝑘, 𝑠): 𝑘 ∈
ℕ, 𝑠 𝑖𝑠 𝑎 𝑠𝑡𝑟𝑖𝑛𝑔} where each k is distinct; define 𝑛 = 𝑚𝑎𝑥( |𝐿|, |𝑅| )
output: a list 𝐽 = {(𝑘, 𝑥, 𝑠) ∶ (𝑘, 𝑥) ∈ 𝐿 𝑎𝑛𝑑 (𝑘, 𝑠) ∈ 𝑅}
baseline goal: an algorithm that runs in 𝑂(𝑛 " ) time
improvement goal: speed up to (𝑛𝑙𝑜𝑔𝑛), or (𝑛) expected time
"""

#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK B: BASELINE GOAL SOLUTION

def join_databases_baseline(L, R):
    """
    Join two lists of tuples based on their shared key (k) using a baseline O(n²) approach.

    :param L: List of tuples (k, x) where k is a unique key and x is a number
    :param R: List of tuples (k, s) where k is a unique key and s is a string
    :return: A new list of tuples (k, x, s) where k exists in both L and R
    """
    # Initialize an empty list to store the result
    J = []

    # Outer loop: iterate through each element in List L
    for k1, x in L:
        # Inner loop: iterate through each element in List R
        for k2, s in R:
            # Check if the keys match
            if k1 == k2:
                # If the keys match, append the tuple (k, x, s) to the result list
                J.append((k1, x, s))

    # Return the joined list
    return J

#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK B: BASELINE GOAL SOLUTION
# Example usage:
L = [(1, 100), (2, 200), (3, 300)]
R = [(1, 'A'), (3, 'C'), (4, 'D')]

# Call the baseline function
result_baseline = join_databases_baseline(L, R)
print(result_baseline)  # Output: [(1, 100, 'A'), (3, 300, 'C')]

"""Time improvement goal: speed up to (𝑛𝑙𝑜𝑔𝑛), or (𝑛) expected time code for task b"""

#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK B: TIME IMPROVEMENT GOAL SOLUTION
def join_databases_sorted(L, R):
    """
    Join two lists of tuples based on their shared key (k) using sorting and two-pointer technique.

    :param L: List of tuples (k, x) where k is a unique key and x is a number
    :param R: List of tuples (k, s) where k is a unique key and s is a string
    :return: A new list of tuples (k, x, s) where k exists in both L and R
    """
    # Step 1: Sort both lists by their keys
    L_sorted = sorted(L, key=lambda x: x[0])  # Sort list L by key (k)
    R_sorted = sorted(R, key=lambda x: x[0])  # Sort list R by key (k)

    # Initialize pointers for both lists
    i, j = 0, 0
    nL, nR = len(L_sorted), len(R_sorted)

    # Initialize the result list
    J = []

    # Step 2: Use two-pointer technique to match keys between the two sorted lists
    while i < nL and j < nR:
        kL, x = L_sorted[i]
        kR, s = R_sorted[j]

        if kL == kR:
            # If keys match, add (k, x, s) to the result
            J.append((kL, x, s))
            i += 1
            j += 1
        elif kL < kR:
            # If the key in L is smaller, move to the next element in L
            i += 1
        else:
            # If the key in R is smaller, move to the next element in R
            j += 1

    return J

#Project 1
#CPSC 535 – Advanced Algorithm Fall 2024 -section 2
#TEAM MEMBERS : Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan
#THIS IS THE EXECUTABLE PYTHON CODE FOR PROJECT 1 - Question 1 ,TASK B: TIME IMPROVEMENT GOAL SOLUTION
# Example usage:
L = [(1, 100), (2, 200), (3, 300)]
R = [(1, 'A'), (3, 'C'), (4, 'D')]

# Call the sorting-based function
result_sorted = join_databases_sorted(L, R)
print(result_sorted)  # Output: [(1, 100, 'A'), (3, 300, 'C')]
"""
 Write a program to create a list of 5 odd integers. Replace the third element with a list of 4 even integers. Flatten, sort and print the list.



"""

# Step 1 Create a list of 5 odd integers
odd_integers = [1, 3, 5, 7, 9]

# Step 2 Replace the third element with a list of 4 even integers
odd_integers[2] = [2, 4, 6, 8]

# Step 3 Flatten the list
flattened_list = []
for element in odd_integers:
    if isinstance(element, list):
        flattened_list.extend(element)
    else:
        flattened_list.append(element)

# Step 4 Sort the flattened list
flattened_list.sort()

# Step 5 Print the list
print(flattened_list)

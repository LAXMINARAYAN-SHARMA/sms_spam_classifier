# === LIST ===
my_list = [1, 2, 3, 4, 5]
print(len(my_list))            # Length of the list
print(my_list[0])              # Access by index
print(my_list[-1])             # Access last element
my_list.append(6)              # Add an element
my_list.remove(3)              # Remove an element
print(my_list.pop())           # Remove and return last element
my_list.sort()                 # Sort the list
my_list.reverse()              # Reverse the list
print(3 in my_list)            # Check if an element exists
print(my_list.index(4))        # Get index of an element
print(my_list.count(2))        # Count occurrences of an element

# === TUPLE ===
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))           # Length of the tuple
print(my_tuple[0])             # Access by index
print(my_tuple[-1])            # Access last element
print(3 in my_tuple)           # Check if an element exists
print(my_tuple.index(4))       # Get index of an element
print(my_tuple.count(2))       # Count occurrences of an element

# === STRING ===
my_string = "hello world"
print(len(my_string))          # Length of the string
print(my_string[0])            # Access by index
print(my_string[-1])           # Access last character
print(my_string.upper())       # Convert to uppercase
print(my_string.lower())       # Convert to lowercase
print(my_string.split())       # Split into list of words
print(my_string.replace("world", "Python"))  # Replace substring
print(my_string.find("o"))     # Find first occurrence of character
print(my_string.count("o"))    # Count occurrences of a character
print(my_string[::-1])         # Reverse the string
" ".join(iterable_data_structure)# convert iterable_data_structure to string with " " as separator

# === SET ===
my_set = {1, 2, 3, 4, 5}
my_set.add(6)                  # Add an element
my_set.remove(3)               # Remove an element
print(len(my_set))             # Length of the set
print(4 in my_set)             # Check if an element exists
another_set = {4, 5, 6, 7}
print(my_set.union(another_set))          # Union of sets
print(my_set.intersection(another_set))   # Intersection of sets
print(my_set.difference(another_set))     # Difference of sets
print(my_set.symmetric_difference(another_set)) # Symmetric difference

# === DICTIONARY ===
my_dict = {"a": 1, "b": 2, "c": 3}
print(len(my_dict))            # Length of the dictionary
print(my_dict["a"])            # Access value by key
my_dict["d"] = 4               # Add a new key-value pair
my_dict.pop("b")               # Remove a key-value pair
print(my_dict.keys())          # Get all keys
print(my_dict.values())        # Get all values
print(my_dict.items())         # Get all key-value pairs
print("a" in my_dict)          # Check if key exists
print(my_dict.get("c"))        # Get value for a key, return None if key doesn’t exist
my_dict.update({"e": 5})       # Merge another dictionary
my_dict.clear()                # Clear the dictionary

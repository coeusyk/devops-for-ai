"""
A sample python program that runs all list methods
(hard-coded for pipeline execution)
"""

lst = [5, 3, 1, 9, 3, 2]
print(f"The list: {lst}")

# Executing the append() method:
print("""
"append()" method:
-----------------""")

lst.append(8)
print(f"Appending \'8\' to the list...\nUpdated list: {lst}")

# Executing the extend() method:
print("""
"extend()" method:
-----------------""")

lst.extend([7, 4, 6])
print(f"Extending the list with 7, 4 and 6 ...\nUpdated list: {lst}")

# Executing the copy() method:
print("""
"copy()" method:
---------------""")

lst_copy = lst.copy()
print("Creating a shallow copy of the list...\nNew copy of \'lst\': \'lst_copy\'")

# Executing the clear() method:
print("""
"clear()" method:
----------------""")

lst_copy.clear()
print(f"Removing all elements from the shallow copy \'lst_copy\'...\nUpdated shallow copy: {lst_copy}")

# Executing the count() method:
print("""
"count()" method:
----------------""")

print(f"Counting the times the number \'3\' occurs in the list (\'lst\')...\nNumber of occurrences of \'3\': {lst.count(3)}")

# Executing the index() method:
print("""
"index()" method:
----------------""")

print(f"Finding the first occurrence of the number \'3\'...\nFirst occurrence of \'3\': at index {lst.index(3)}")

# Executing the insert() method:
print("""
"insert()" method:
-----------------""")

lst.insert(1, 8)
print(f"Inserting the number \'8\' at index \'1\'...\nUpdated list: {lst}")

# Executing the pop() method:
print("""
"pop()" method:
--------------""")

last_element = lst.pop()
print(f"Removing and obtaining the last element of the list...\nRemoved element (stored in \'last_element\'): "
      f"{last_element}\nUpdated list: {lst}")

# Executing the remove() method:
print("""
"remove()" method:
-----------------""")

lst.remove(3)
print(f"Removing the first occurrence of \'3\' in the list...\nUpdated list: {lst}")

# Executing the reverse() method:
print("""
"reverse()" method:
------------------""")

lst.reverse()
print(f"Reversing the list...\nUpdated list: {lst}")

# Executing the min() function:
print(f"""
"min()" function:
----------------
The minimum element in the list: {min(lst)}""")

# Executing the max() function:
print(f"""
"max()" function:
----------------
The maximum element in the list: {max(lst)}""")

# Executing the sort() method:
print("""
"sort()" method:
---------------""")

lst.sort()
print(f"Sorting the list...\nUpdated list: {lst}")
